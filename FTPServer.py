#!/usr/bin/env python2
from __future__ import print_function, division, absolute_import

# Import twisted things

from twisted.protocols.ftp import FTPFactory
from twisted.protocols.ftp import FTP
from twisted.protocols.ftp import FTPRealm
from twisted.protocols.policies import TimeoutMixin, ThrottlingFactory, WrappingFactory, ThrottlingProtocol
from twisted.internet import reactor
from twisted.cred.portal import Portal
from twisted.cred.checkers import AllowAnonymousAccess


p = Portal(FTPRealm("test/"), [AllowAnonymousAccess()])
#f = ThrottlingFactory(FTPFactory, readLimit=1000, writeLimit=1000)
#p = Tho(p)

f = FTPFactory(p)
#factory = FTPFactory()
#wrapper = ThrottlingFactory(FTPFactory(p), readLimit=1, writeLimit=1)

#f = f.wrappedFactory(p)
f.timeOut = None
#f = ThrottlingFactory(f, readLimit=1, writeLimit=1)
#f = FileServerFactory()

reactor.listenTCP(5504, f)
reactor.run()
