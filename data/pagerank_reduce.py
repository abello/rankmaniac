#!/usr/bin/env python

import sys
import numpy as np

result = {} # dictionary will hold pairs of {node: sum_pagerank_of_node}
ALPHA = 0.85

# read a line of input
for orig_line in sys.stdin:
    line = orig_line.split()[1]
 
    # if line starts with '_' it's adj info; pass it along as is
    if line[0] == '_':
        sys.stdout.write(orig_line)

    # else line starts with '+' and it's contrib info; grab it
    else:
    #elif line[0] == '+':
        info = line[1:].split(',')

        # save each value the line holds
        iteration = int(info[0])
        node      = int(info[1])
        contrib   = float(info[2])

        if node in result.keys():
            # increment node's pagerank in {result} with another contribution
            result[node] += contrib
        else:
            # initialize node's pagerank entry in {result}
            result[node] = contrib

# loop over every node with pagerank and emit it
for node in result.keys():
    # (node, rank) pair lines start with a '+'
    rank = ALPHA * result[node] + (1 - ALPHA)
    print str(node) + '\t+' + str(iteration) + ',' + str(node) + ',' + str(rank)

