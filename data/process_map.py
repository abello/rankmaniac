#!/usr/bin/env python

import sys
import cPickle as pickle

#
# This program simply represents the identity function.
#

ALPHA = 0.8

result = {}
nodes = set()
iteration = 0

for line in sys.stdin:
    if line[0] == '_':
        # this is the case that we are reading the total list of nodes
        # use this to fill out ourdictionary

        # Emit adjlist
        print line

        # adj = '_' + pickle.dumps(np.array(iteration, node, rank_curr, rank_prev, outLinks))
        line = line.decode('string-escape')
        unpickled = pickle.loads(line[1:])
        nodes.add(unpickled[1])

        for n in unpickled[4]:
            nodes.add(n)

    # TODO: Change this to else eventually
    elif line[0] == '+':
        line = line.decode('string-escape')
        info = pickle.loads(line[1:])

        iteration = info[0]
        node = info[1]
        contribution = info[2]

        if node in result.keys():
            result[node] += contribution
        else:
            result[node] = contribution

resultKeys = result.keys()
for n in nodes:
    if n not in resultKeys:
        result[n] = 0

numNodes = len(result.keys())
for r in resultKeys:
    result[r] = ALPHA * result[r] + (1 - ALPHA) / numNodes
    out = '+' + pickle.dumps([iteration, r, result[r]])
    out = out.encode('string-escape')
    print out
#     sys.stdout.write('p' + str(iteration) + ':' + str(r) + ':' + str(result[r]) + '\n')

