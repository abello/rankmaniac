#!/usr/bin/env python

import sys
import numpy as np

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


    # This is adj information, pass it along
    if line[0] == '_':
        # this is the case that we are reading the total list of nodes
        # use this to fill out our dictionary
#         data = line[1:]
# 
#         nodes = data.split(',')
# 
#         for n in nodes[:-1]:
#             if int(n) not in result.keys():
#                 result[int(n)] = 0
        sys.stdout.write(line)

    # If it starts with +, it's contribs
    # TODO: Make this an else while we show that this works
    elif line[0] == '+':
        # this is the case that we are reading the total list of nodes
        info = pickle.loads(line[1:])

        iteration = info[0]
        node = info[1]
        contribution = info[2]

        if node in result.keys():
            result[node] += contribution
        else:
            result[node] = contribution
    
for node in result.keys():
    out = '+' + pickle.dumps(np.array(iteration), node, result[node]) 
    sys.stdout.write(out)
#     sys.stdout.write('+' + str(iteration) + ':' + str(r) + ':' + str(result[r]) + '\n')
    



