Quanttp
=======

An HTTP API that wraps [ComScire quantum random number generator API](https://comscire.com/downloads/qwqngdoc/).

Running
-------

1. Install ComScire driver from https://comscire.com/downloads/
2. Run the following commands
   ```
   pip install -r requirements.txt
   python -m quanttp
   ```

Usage Example
-------------

### REST API

	http://localhost:62456/api/randint32
	< -1741405968

	http://localhost:62456/api/randuniform
	< 0.20340009994

	http://localhost:62456/api/randnormal
	< 1.02206840644

	http://localhost:62456/api/randbytes?length=16
	< ���E��s_�b����G�


### WebSocket API
	
	ws://localhost:62456/ws
	> RANDINT32
	< 585865374

	> RANDUNIFORM
	< 0.70137183786

	> RANDNORMAL
	< -1.6120135370

	> RANDBYTES 32
	< �����9L).�!:���@Nh������d����_q�

	> SUBSCRIBEINT32
	< 1361330636
	< -604581511
	< 1510923919
	< ...
	> UNSUBSCRIBE
	< UNSUBSCRIBED

	> SUBSCRIBEUNIFORM
	< 0.54623951886
	< 0.67567578799
	< 0.09746421443
	< ...
	> UNSUBSCRIBE
	< UNSUBSCRIBED

	> SUBSCRIBENORMAL
	< -1.6120135370
	< 0.02943381135
	< -0.9883458007
	< ...
	> UNSUBSCRIBE
	< UNSUBSCRIBED

	> SUBSCRIBEBYTES 8
	< �K����{�
	< I]������
	< ���.�t�U
	< ...
	> UNSUBSCRIBE
	< UNSUBSCRIBED

License
-------

    Copyright (c) 2020 Andika Wasisto

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.