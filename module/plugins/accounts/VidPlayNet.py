# -*- coding: utf-8 -*-

from module.plugins.internal.XFSPAccount import XFSPAccount


class VidPlayNet(XFSPAccount):
    __name__    = "VidPlayNet"
    __type__    = "account"
    __version__ = "0.01"

    __description__ = """VidPlay.net account plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Walter Purcaro", "vuolter@gmail.com")]


    HOSTER_NAME = "vidplay.net"
