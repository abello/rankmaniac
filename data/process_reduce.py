#!/usr/bin/env python

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from rankmaniac import Rankmaniac

#
# This program simply represents the identity function.
#

for i in range(20):
	sys.stdout.write('FinalRank:1\t' + str(i) + '\n')


#for line in sys.stdin:   
#    sys.stdout.write(line)

