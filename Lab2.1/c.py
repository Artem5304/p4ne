#!/usr/bin/python3
import glob

import requests

from time import sleep

a = glob.glob("cards")
q = 0
k = 'https://lookup.binlist.net/'
for i in a:
    with open(i) as f:
        for l in f :
            if l.find("CardNumber") == -1:
                q = q + 1
            else:
                w = l.replace('            "CardNumber": ', "").strip()
                sleep(1)
                r = requests.get(k+w)
                print("\r\n"+'Card ' + w + ': ')
                if 200<=r.status_code<300:
                    print(r.json()['bank'])
                else:
                    print('Card not found!')
