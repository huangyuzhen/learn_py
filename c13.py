#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import xmlrpclib

xmlrpc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
evil = 'Bert'

print xmlrpc.system.listMethods()
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']

print xmlrpc.system.methodHelp('phone')
print xmlrpc.phone(evil)
