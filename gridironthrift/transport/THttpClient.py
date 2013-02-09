#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

from TTransport import *
from cStringIO import StringIO
import urlparse
import httplib
import warnings
import socket
import struct
import base64

class THttpClient(TTransportBase):
    """Http implementation of TTransport base."""
    first_time = 1
    seqId = 0
    serviceTag = ''
    auth_string = None
    tunnel_host = None
    tunnel_port = None
    response = None

    def __init__(self, uri_or_host, proxy_uri = None, username = None, password = None):
        self.serviceTag = 'api'
        parsed = urlparse.urlparse(uri_or_host)
        if proxy_uri:
            parsed_proxy = proxy_uri.split(':')
        if proxy_uri:
            self.port = parsed_proxy[1]
            self.host = parsed_proxy[0]
            self.path = parsed.path
            self.tunnel_host = parsed.hostname
            self.tunnel_port = parsed.port
            if username:
                self.auth_string = base64.encodestring(username + ':' + password)
        else:
            self.scheme = parsed.scheme
            if not self.scheme in ('http', 'https'):
                raise AssertionError
                self.port = self.scheme == 'http' and (parsed.port or httplib.HTTP_PORT)
            elif self.scheme == 'https':
                self.port = parsed.port or httplib.HTTPS_PORT
            self.host = parsed.hostname
            self.path = parsed.path
        if parsed.query:
            self.path += '?%s' % parsed.query
        self.__wbuf = StringIO()
        self.__http = None
        self.__timeout = None

    def open(self):
        self.__http = httplib.HTTPSConnection(self.host, self.port)

    def close(self):
        self.__http.close()
        self.__http = None

    def isOpen(self):
        return self.__http != None

    def setTimeout(self, ms):
        if not hasattr(socket, 'getdefaulttimeout'):
            raise NotImplementedError
        if ms is None:
            self.__timeout = None
        else:
            self.__timeout = ms / 1000.0

    def read(self, sz):
        return self.response.read(sz)

    def generateGIHeader(self):
        clientId = 'PyManagementSDK\x00'
        serviceTag = self.serviceTag + '\x00'
        protocol = 'T'
        platform = 7
        protver = 65636
        self.seqId += 1
        values = (clientId,
         serviceTag,
         protocol,
         platform,
         protver,
         self.seqId)
        s = struct.Struct('> 40s 50s 1s I I I')
        return s.pack(*values)

    def write(self, buf):
        self.__wbuf.write(self.generateGIHeader())
        self.__wbuf.write(buf)

    def __withTimeout(f):

        def _f(*args, **kwargs):
            orig_timeout = socket.getdefaulttimeout()
            socket.setdefaulttimeout(args[0].__timeout)
            result = f(*args, **kwargs)
            socket.setdefaulttimeout(orig_timeout)
            return result

        return _f

    def flush(self):
        if self.isOpen():
            self.close()
        self.open()
        if self.tunnel_host:
            if self.auth_string:
                self.__http.set_tunnel(self.tunnel_host, self.tunnel_port, {'Proxy-Authorization': 'Basic %s' % self.auth_string})
            else:
                self.__http.set_tunnel(self.tunnel_host, self.tunnel_port)
        data = self.__wbuf.getvalue()
        self.__wbuf = StringIO()
        self.__http.putrequest('POST', self.path)
        self.__http.putheader('Host', self.host)
        self.__http.putheader('Content-Type', 'application/x-thrift')
        self.__http.putheader('Content-Length', str(len(data)))
        self.__http.endheaders()
        self.__http.send(data)
        self.response = self.__http.getresponse()
        self.code = self.response.status
        self.message = self.response.reason
        self.headers = self.response.msg

    if hasattr(socket, 'getdefaulttimeout'):
        flush = __withTimeout(flush)
