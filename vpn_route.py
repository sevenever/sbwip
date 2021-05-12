#!/usr/bin/python

import subprocess
import os
import sys
from socket import inet_ntoa
from struct import pack

curdir = sys.argv[1]

allroutes = []

'''
blocks = [\
        '_netblocks.google.com', \
        '_netblocks2.google.com', \
        '_netblocks3.google.com', \
        '_thirdparty.twitter.com'\
        ]

def handleBlock(block):
  incs = []
  routes = []
  for x in subprocess.check_output(['/usr/bin/dig', '@8.8.8.8', 'TXT','+short', block]).split():
    if x.startswith('ip4'):
      y = x[4:].split('/')
      routes.append((x[4:].split('/'), block))
    elif x.startswith('include:'):
      incs.append(x[8:])

  return incs, routes

while len(blocks) > 0:
  block = blocks.pop()
  incs, routes = handleBlock(block)
  for inc in incs:
      if inc in blocks:
          blocks.append(inc)
  allroutes.extend(routes)
'''
for x in open(os.path.join(curdir, 'twitter.blocks')):
  allroutes.append((x.split('/'), 'twitter'))

for x in open(os.path.join(curdir, 'facebook.blocks')):
  allroutes.append((x.split('/'), 'facebook'))

for x in open(os.path.join(curdir, 'google.blocks')):
  allroutes.append((x.split('/'), 'google'))

for x in open(os.path.join(curdir, 'telegram.blocks')):
  allroutes.append((x.split('/'), 'telegram'))

#for x in open(os.path.join(curdir, 'netflix.blocks')):
#  allroutes.append((x.split('/'), 'netflix'))

#github
#allroutes.append((['192.30.252.0', '22'], 'github'))

# dns
allroutes.append((['8.8.8.8', '32'], ''))
allroutes.append((['8.8.4.4', '32'], ''))
allroutes.append((['4.3.2.1', '32'], ''))
allroutes.append((['208.67.222.222', '32'], ''))
#allroutes.append((['9.9.9.9', '32'], ''))

# reddit
allroutes.append((['151.101.0.0', '16'], ''))
# pbs.twimg.com cdn
allroutes.append((['72.21.0.0', '16'], ''))
# openvpn.net
allroutes.append((['104.20.194.50', '32'], ''))
allroutes.append((['104.20.195.50', '32'], ''))
# pornhub
allroutes.append((['64.210.158.0', '24'], ''))
# github.io
allroutes.append((['185.199.0.0', '16'], ''))
# github.com
allroutes.append((['192.30.255.112', '32'], ''))
allroutes.append((['192.30.255.113', '32'], ''))
# yahoo.co.jp
allroutes.append((['183.79.0.0', '16'], ''))
# www.as-books.jp
allroutes.append((['211.125.68.12', '32'], ''))
# quora.com
allroutes.append((['18.214.110.0', '24'], 'quora.com'))


for l in open(os.path.join(curdir, 'ips')):
  ip, domain = l.strip().split(' ', 1)
  allroutes.append(([ip, '32'], domain))

if '-sb' in sys.argv:
  for y, block in allroutes:
    print '%s %s'%(y[0], inet_ntoa(pack('>I', 0xffffffff ^ (1 << 32 - int(y[1])) - 1)) if len(y) > 1 else '')
else:
  for y, block in allroutes:
    print 'route %s %s    # %s'%(y[0], inet_ntoa(pack('>I', 0xffffffff ^ (1 << 32 - int(y[1])) - 1)) if len(y) > 1 else '', block)
