#!/usr/bin/env python

import sys
import numpy as np

ALPHA = 0.8

#
# This program simply represents the identity function.
#

# this dictionary will hold information of the pagerank contributions of
# each node
result = {}
iteration = 0

for line in sys.stdin:
    # lines will be formatted as:
    # 3:0:1.5
    # where 3 is the iteration
    # 0 is the node identifier
    # 1.5 is the contribution of pagerank
    # we will get a list of these

    if line[0] == 'n':
        # this is the case that we are reading the total list of nodes
        # use this to fill out our dictionary
        data = line[1:]

        nodes = data.split(',')

        for n in nodes[:-1]:
            if int(n) not in result.keys():
                result[int(n)] = 0
    elif line[0] == 'c':
        split_line = line[1:].split(':')

        iteration = int(split_line[0])
        node = int(split_line[1])
        contribution = float(split_line[2])

        if node in result.keys():
            result[node] += contribution
        else:
            result[node] = contribution
    else:
         sys.stdout.write(line)
    
for r in result.keys():
    result[r] = ALPHA * result[r] + (1 - ALPHA) / len(result.keys())
    sys.stdout.write('p' + str(iteration) + ':' + str(r) + ':' + str(result[r]) + '\n')
    
