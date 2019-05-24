#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# #!/usr/bin/env python2

# import xmlrpclib


from xmlrpc import client as xmlrpclib

xmlrpc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
evil = 'Bert'

print(xmlrpc.system.listMethods())
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']

print(xmlrpc.system.methodHelp('phone'))
print(xmlrpc.phone(evil))
