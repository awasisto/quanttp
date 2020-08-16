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


class QngWrapperWindows:

    def __init__(self):
        import win32com.client
        self.qng = win32com.client.Dispatch("QWQNG.QNG")

    def randint32(self):
        try:
            return self.qng.RandInt32
        except:
            self.qng.Reset()
            return self.qng.RandInt32

    def randuniform(self):
        try:
            return self.qng.RandUniform
        except:
            self.qng.Reset()
            return self.qng.RandUniform

    def randnormal(self):
        try:
            return self.qng.RandNormal
        except:
            self.qng.Reset()
            return self.qng.RandNormal

    def randbytes(self, length):
        try:
            return self._randbytes_arbitrary_length(length)
        except:
            self.qng.Reset()
            return self._randbytes_arbitrary_length(length)

    def _randbytes_arbitrary_length(self, length):
        if length <= 8192:
            return bytes(self.qng.RandBytes(length))
        else:
            data = bytearray()
            for x in range(length // 8192):
                data.extend(bytearray(self.qng.RandBytes(8192)))
            bytes_needed = length % 8192
            if bytes_needed != 0:
                data.extend(bytearray(self.qng.RandBytes(bytes_needed)))
            return bytes(data)

    def clear(self):
        self.qng.Clear()
