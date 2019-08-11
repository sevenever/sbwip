#!/bin/bash

AS=$1
whois -h whois.radb.net -- "-i origin ${AS}" | grep '^route:' |cut -d':' -f 2- | tr -d ' '
