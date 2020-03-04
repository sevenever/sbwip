#!/bin/bash

#{
#	curl https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt | base64 -d |grep '^||' | sed s/'^..'//g | sort | uniq
#} | while read -r DOMAIN;do
#	dig +noall +answer ${DOMAIN} | tr '\t' ' '| tr -s ' ' | cut -d ' ' -f 4- | grep '^A' | cut -d ' ' -f 2 | while read -r ip;do
#		echo ${ip} ${DOMAIN}
#	done 
#done | sort | uniq

{
	curl https://raw.githubusercontent.com/gfwlist/tinylist/master/tinylist.txt | base64 -d |grep '^||' | sed s/'^..'//g
	cat $1
} | sort | uniq | python3 <(cat <<EOF
import sys
import json
import urllib.request

def dig(name):
    try:
        j = json.load(urllib.request.urlopen("https://dns.google/resolve?name=%s&type=a&cd=1&do=0" % name))
        if "Answer" in j:
            for a in j["Answer"]:
                if a['type'] == 1:
                    print(' '.join([a["data"], name]))
    except:
#        print(name)
#        raise
        pass

for l in sys.stdin:
    dig(l.strip())

EOF
) | sort | uniq
