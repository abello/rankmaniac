#!/usr/bin/env python

import sys
import cPickle as pickle

#
# This program simply represents the identity function.
#

ALPHA = 0.85

result = {}
nodes = set()
iteration = 0

for line in sys.stdin:
    if line[0] == '_':
        # this is the case that we are reading the total list of nodes
        # use this to fill out ourdictionary

        # Emit adjlist
        sys.stdout.write(line)

        # adj = '_' + pickle.dumps(np.array(iteration, node, rank_curr, rank_prev, outLinks))
        line = line.decode('string-escape')
        unpickled = pickle.loads(line[1:])
        nodes.add(unpickled[1])

    # TODO: Change this to else eventually
    elif line[0] == '+':
        line = line.decode('string-escape')
        info = pickle.loads(line[1:])

        iteration = info[0]
        node = info[1]
        contribution = info[2]

        if node in result.keys():
            result[int(node)] += contribution
        else:
            result[int(node)] = contribution


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

