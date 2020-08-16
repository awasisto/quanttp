# Copyright (c) 2020 Andika Wasisto
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from ctypes import cdll, c_void_p, c_int, c_double, POINTER, c_char


class QngWrapperLinux:

    def __init__(self):
        self.libqwqng_wrapper = cdll.LoadLibrary('./libqwqng-wrapper.so')
        self.libqwqng_wrapper.GetQwqngInstance.restype = c_void_p
        self.libqwqng_wrapper.RandInt32.argtypes = [c_void_p]
        self.libqwqng_wrapper.RandInt32.restype = c_int
        self.libqwqng_wrapper.RandUniform.argtypes = [c_void_p]
        self.libqwqng_wrapper.RandUniform.restype = c_double
        self.libqwqng_wrapper.RandNormal.argtypes = [c_void_p]
        self.libqwqng_wrapper.RandNormal.restype = c_double
        self.libqwqng_wrapper.RandBytes.argtypes = [c_void_p, c_int]
        self.libqwqng_wrapper.RandBytes.restype = POINTER(c_char)
        self.libqwqng_wrapper.Clear.argtypes = [c_void_p]
        self.libqwqng_wrapper.Reset.argtypes = [c_void_p]
        self.qng = self.libqwqng_wrapper.GetQwqngInstance()

    def randint32(self):
        try:
            return self.libqwqng_wrapper.RandInt32(self.qng)
        except:
            self.libqwqng_wrapper.Reset(self.qng)
            return self.libqwqng_wrapper.RandInt32(self.qng)

    def randuniform(self):
        try:
            return self.libqwqng_wrapper.RandUniform(self.qng)
        except:
            self.libqwqng_wrapper.Reset(self.qng)
            return self.libqwqng_wrapper.RandUniform(self.qng)

    def randnormal(self):
        try:
            return self.libqwqng_wrapper.RandNormal(self.qng)
        except:
            self.libqwqng_wrapper.Reset(self.qng)
            return self.libqwqng_wrapper.RandNormal(self.qng)

    def randbytes(self, length):
        try:
            return self._randbytes_arbitrary_length(length)
        except:
            self.libqwqng_wrapper.Reset(self.qng)
            return self._randbytes_arbitrary_length(length)

    def _randbytes_arbitrary_length(self, length):
        if length <= 8192:
            return self.libqwqng_wrapper.RandBytes(self.qng, length)[:length]
        else:
            data = bytearray()
            for x in range(length // 8192):
                data.extend(self.libqwqng_wrapper.RandBytes(self.qng, 8192)[:8192])
            bytes_needed = length % 8192
            if bytes_needed != 0:
                data.extend(self.libqwqng_wrapper.RandBytes(self.qng, bytes_needed)[:bytes_needed])
            return bytes(data)

    def clear(self):
        self.libqwqng_wrapper.Clear(self.qng)
