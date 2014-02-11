#!/usr/bin/env python

import sys
import numpy as np
import cPickle as pickle

# this dictionary will hold information of the pagerank contributions of
# each node
result = {}
iteration = 0

# read a line of input
for line in sys.stdin:
 
    # if line starts with '_' it's adj info; pass it along as is
    if line[0] == '_':
        sys.stdout.write(line) # (doesn't need newline)

    # else line starts with '+' and it's contrib info; grab it
    else:
        # decode (unescape) and un-pickle the line
        line = line.decode('string-escape')
        info = pickle.loads(line[1:])

        # save each value in the line
        iteration = info[0]
        node      = info[1]
        contrib   = info[2]

        if node in result.keys():
            # increment node's pagerank in {result} with another contribution
            result[int(node)] += contrib
        else:
            # initialize node's pagerank entry in {result}
            result[int(node)] = contrib

# loop over every node with pagerank and emit it
for node in result.keys():
    # (node, rank) pair lines start with a '+'
    out = '+' + pickle.dumps(np.array([iteration, node, result[int(node)]]))
    out = out.encode('string-escape')
    print out # (needs newline)