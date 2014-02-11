#!/usr/bin/env python

import sys
import cPickle as pickle

ALPHA = 0.85

result = {} # dictionary will hold pairs of {node: sum_pagerank_of_node}
nodes = set() # set will hold ALL node id's (even those without parents)

# read a line of input
for line in sys.stdin:

    # if line starts with '_' it's adj info; pass it along but also save its 
    # node so that at the end we'll have a full list of nodes - INCLUDING nodes
    # that do not have any parents!
    if line[0] == '_':
        sys.stdout.write(line) # (doesn't need newline)

        # decode (unescape) and un-pickle the line
        line = line.decode('string-escape')
        unpickled = pickle.loads(line[1:])

        # record the node in our set
        nodes.add(unpickled[1])

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

# find every node in the graph without parents
# and initialize its pagerank to zero
for n in nodes:
    if n not in result.keys():
        result[n] = 0

# for every node in the graph
for r in result.keys():

    # scale node's pagerank so that it's always nonzero
    result[r] = ALPHA * result[r] + (1 - ALPHA)

    # (node, rank) pair lines start with a '+'
    out = '+' + pickle.dumps([iteration, r, result[r]])
    out = out.encode('string-escape')
    print out # (newline needed)