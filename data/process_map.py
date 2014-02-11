#!/usr/bin/env python

import sys
import cPickle as pickle

ALPHA = 0.85

result = {} # dictionary will hold pairs of {node: sum_pagerank_of_node}
nodes = set()

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

    # TODO: Change this to else eventually
    # else line starts with '+' and it's contrib info; grab it
    elif line[0] == '+':
        line = line.decode('string-escape')
        info = pickle.loads(line[1:])

        iteration = info[0]
        node      = info[1]
        contrib   = info[2]

        if node in result.keys():
            result[node] += contrib
        else:
            result[node] = contrib
    else:
        assert False


for n in nodes:
    if n not in result.keys():
        result[n] = 0

numNodes = len(result.keys())
sumRanks = sum(result.values())
for r in result.keys():
    result[r] = ALPHA * result[r] + (1 - ALPHA)
    out = '+' + pickle.dumps([iteration, r, result[r]])
    out = out.encode('string-escape')
    print out

