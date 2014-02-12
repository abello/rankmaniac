#!/usr/bin/env python

import sys
import numpy as np
import cPickle as pickle

result = {} # dictionary will hold pairs of {node: sum_pagerank_of_node}
ALPHA = 0.85

# read a line of input
for line in sys.stdin:
    index = line.find('\t')
    line = line[index+1:]
 
    # if line starts with '_' it's adj info; pass it along as is
    if line[0] == '_':
        sys.stdout.write(line) # (doesn't need newline)

    # else line starts with '+' and it's contrib info; grab it
    else:
        # decode (unescape) and un-pickle the line
        line = line.decode('string-escape')
        info = pickle.loads(line[1:])

        # save each value the line holds
        iteration = info[0]
        node      = info[1]
        contrib   = info[2]

        if node in result.keys():
            # increment node's pagerank in {result} with another contribution
            result[node] += contrib
        else:
            # initialize node's pagerank entry in {result}
            result[node] = contrib

# loop over every node with pagerank and emit it
for node in result.keys():
    # (node, rank) pair lines start with a '+'
    out = '+' + pickle.dumps((iteration, node, ALPHA * result[node]  + (1 - ALPHA)
))
    out = out.encode('string-escape')
    print out # (needs newline)
