#!/usr/bin/env python

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from rankmaniac import Rankmaniac

#
# This program simply represents the identity function.
#

i = 0
for line in sys.stdin:   
    if int(line) == 2:
        for i in range(20):
            sys.stdout.write('FinalRank:1\t' + str(i) + '\n')
        break
    else:
        sys.stdout.write(str(int(line) + 1) + '\n')

