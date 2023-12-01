import base64
import json
from pwn import xor

text = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5ofnh8e354bjY='

ar = {
    "showpassword" : "yes",
    "bgcolor" : "#ffffff"
}
json_text = json.dumps(ar)


# print(json.dumps(ar))

# print(t1)

t1 = base64.b64decode(text)


xor_text = xor(json_text, t1)

print(xor_text)


key = 'KNHL'


json_text_new = xor(json_text, key)

print(json_text_new)
json_text_b64 = base64.b64encode(json_text_new)

print(json_text_b64)



