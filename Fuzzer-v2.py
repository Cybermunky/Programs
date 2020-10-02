#!/usr/bin/env python2

import socket

RHOST = "172.16.1.54"
RPORT = 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buf = ""
buf += "Exploit Security"
buf += "\n"

s.send(buf)

print "Sent: {0}".format(buf)

data = s.recv(1024)

print "Received: {0}".format(data)
