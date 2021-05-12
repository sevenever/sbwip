#!/usr/bin/python3

'''
usage:
whois -h whois.radb.net -- '-i origin AS15169' | tee AS15169.google
cat AS15169.google |grep '^route:' | tr -s ' '| cut -d ' ' -f 2 |sort -n | python3 compress_as.py > google.blocks
'''

import sys
import ipaddress

def main():
    pre = None
    for l in sys.stdin:
        cur = ipaddress.ip_network(l.rstrip())
        if pre:
            if pre.overlaps(cur):
                continue
            if pre.supernet().overlaps(cur):
                pre = pre.supernet()
                continue
            print(pre)
        pre = cur
        pass
    if pre == cur:
        print(pre)

if __name__ == '__main__':
    main()
