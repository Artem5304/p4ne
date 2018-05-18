#!/usr/bin/python3

import glob
a = glob.glob("*.txt")
#print(a)

#import os
#k = os.listdir('/home/velikan/Documents/How to/Python/config_files')
#print(k)

import re

#l = sorted(list(set(list(open(’*.txt')))))
#print(l))
q = 0
iplist = []
for i in a:
    with open(i) as f:
        for l in f:
            if l.find("ip address") == -1:
                q = q+1
            else:
                a = l.replace("ip address", "").strip()
                if bool(re.match(r"^(([0-9]{1,3}\.){3}[0-9]{1,3}) (([0-9]{1,3}\.){3}[0-9]{1,3})$", a)):
                    if a not in iplist:
                        iplist.append(a)

print(iplist)

#print(q)
#m = re.match(r"^(([0-9]{1,3}\.){3}[0-9]{1,3}) (([0-9]{1,3}\.){3}[0-9]{1,3})$", "10.12.234.239 255.255.255.128")
#print(bool(m))
#print(m.group(0))