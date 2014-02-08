#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
#     rank = 20 - i + 0.1
#     sys.stdout.write('FinalRank:' + str(rank) + '\t' + str(i) + '\n')
    pass

s = ""
for i in range(20):
    s += "FinalRank:1" + "\t" + str(i) + "\n"


print s
