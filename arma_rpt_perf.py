#!/usr/bin/env python3

import re
from statistics import stdev, mean
from sigfig import round

# TODO: take filename from command line
f = open("/home/gameserver/arma_servers/logs/server1-1579700481.rpt","r")
rpt = f.read().split("\n")
# TODO: split based on mission load
f.close()
# 15 is magic number - where '\d\d:\d\d:\d\d "FPS: ' ends
fps = list(map(lambda s: float(s[15:-1]), filter(lambda s: bool(re.match(r'^\d\d:\d\d:\d\d "FPS: .*"', s)), rpt)))
print(str(round(mean(fps),sigfigs=3)) + " +/- " + str(round(stdev(fps),sigfigs=3)) + " FPS")
