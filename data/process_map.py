#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

ALPHA = 0.8

result = {}
nodeIds = []
iteration = 0

for line in sys.stdin:
    if line[0] == 'n':
        # this is the case that we are reading the total list of nodes
        # use this to fill out ourdictionary
        data = line[1:]

        nodes = data.split(',')

        for n in nodes[:-1]:
            nodeIds.append(int(n))
    elif line[0] == 'p':
        # should be formatted as 'p3:0:5.0' where
        # 3 is the iteration
        # 0 is the node
        # 5.0 is total contribution from alpha*P

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

for n in nodeIds:
    if n not in result.keys():
        result[n] = 0

numNodes = len(result.keys())
for r in result.keys():
    result[r] = ALPHA * result[r] + (1 - ALPHA) / numNodes
    sys.stdout.write('p' + str(iteration) + ':' + str(r) + ':' + str(result[r]) + '\n')

