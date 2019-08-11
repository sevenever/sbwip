#!/usr/bin/python

import subprocess
import sys
from socket import inet_ntoa
from struct import pack

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
for x in open('twitter.blocks'):
  allroutes.append((x.split('/'), 'twitter'))

for x in open('facebook.blocks'):
  allroutes.append((x.split('/'), 'facebook'))

for x in open('google.blocks'):
  allroutes.append((x.split('/'), 'google'))

#for x in open('netflix.blocks'):
#  allroutes.append((x.split('/'), 'netflix'))

#github
#allroutes.append((['192.30.252.0', '22'], 'github'))

# dns
allroutes.append((['8.8.8.8', '32'], ''))
allroutes.append((['8.8.4.4', '32'], ''))
allroutes.append((['4.3.2.1', '32'], ''))
allroutes.append((['208.67.222.222', '32'], ''))
# mitbbs.com
allroutes.append((['104.20.62.7', '32'], ''))
allroutes.append((['104.20.63.7', '32'], ''))
allroutes.append((['107.23.37.111', '32'], ''))
# ipfs.io
allroutes.append((['147.135.130.181', '32'], ''))
allroutes.append((['217.182.195.23', '32'], ''))
# 
allroutes.append((['104.20.6.63', '32'], ''))
allroutes.append((['104.20.7.63', '32'], ''))
# huobi
allroutes.append((['47.91.205.147', '32'], ''))
allroutes.append((['119.188.35.95', '32'], ''))
allroutes.append((['13.115.29.220', '32'], ''))
# archive.org
allroutes.append((['207.241.225.186', '32'], ''))
allroutes.append((['207.241.224.26', '32'], ''))
# thepiratebay
allroutes.append((['104.27.217.28', '32'], ''))
allroutes.append((['104.27.216.28', '32'], ''))
# t66y.com
allroutes.append((['104.25.31.112', '32'], ''))
allroutes.append((['104.25.32.112', '32'], ''))
# wikipedia
allroutes.append((['198.35.26.96', '32'], ''))
# reddit
allroutes.append((['151.101.0.0', '16'], ''))
# pbs.twimg.com cdn
allroutes.append((['72.21.0.0', '16'], ''))
# openvpn.net
allroutes.append((['104.20.194.50', '32'], ''))
allroutes.append((['104.20.195.50', '32'], ''))
# pornhub
allroutes.append((['66.254.114.41', '32'], ''))
# wikileaks
allroutes.append((['95.211.113.154', '32'], ''))
# slideshare
allroutes.append((['108.174.10.19', '32'], ''))
# telegram
allroutes.append((['149.154.167.99', '32'], ''))
# esu.wiki
allroutes.append((['104.18.39.28', '32'], ''))
allroutes.append((['104.18.38.28', '32'], ''))
# github.io
allroutes.append((['185.199.0.0', '16'], ''))
# bit.ly
allroutes.append((['67.199.248.10','32'], ''))
# yahoo.co.jp
allroutes.append((['183.79.0.0', '16'], ''))


if len(sys.argv) > 1 and sys.argv[1] == "-sb":
  for y, block in allroutes:
    print '%s %s'%(y[0], inet_ntoa(pack('>I', 0xffffffff ^ (1 << 32 - int(y[1])) - 1)) if len(y) > 1 else '')
else:
  for y, block in allroutes:
    print 'route %s %s    # %s'%(y[0], inet_ntoa(pack('>I', 0xffffffff ^ (1 << 32 - int(y[1])) - 1)) if len(y) > 1 else '', block)
