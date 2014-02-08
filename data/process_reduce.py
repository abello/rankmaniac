#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for i in range(20):
    rank = 20 - i + 0.1
    sys.stdout.write('FinalRank:' + str(rank) + '\t' + str(i) + '\n')

