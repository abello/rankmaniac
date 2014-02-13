#!/usr/bin/env python

import sys

#'''
#Format of INPUT and OUTPUT rank lines:
#    +node \t iteration,rank
#
#Format of INPUT and OUTPUT adjacency lines:
#    _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
#'''

ALPHA = 0.85

seenNodes = set() # nodes with known and scaled ranks
allNodes  = set() # all nodes (includes nodes without parents but with children)
iteration = -1

for line in sys.stdin:

    # case for contribution line
    if line[0] == '+':

        # get node and save in set of nodes with known rank
        key, value = line.split()
        node = key[1:]
        seenNodes.add(node)

        # set iteration value
        iteration = value[0]

        # pass the original line along to output
        sys.stdout.write(line)

    # case for adjacency line
    else:

        # get node and save in set of all nodes
        key, value = line.split()
        node = key[1:]
        allNodes.add(node)

        # set iteration value
        iteration = value[0]

        # pass the original line along to output
        sys.stdout.write(line)


# find nodes of unknown rank (they contributed all their rank to child nodes but
# have no parent nodes to get rank from)
# TODO this loop is fucking expensive you know
for node in allNodes.difference(seenNodes):
    # emit a line giving this node (1-ALPHA) rank
    print '+' + node + '\t' + str(iteration) + ',' + str(1 - ALPHA)
