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
    elif line[0] == '_':

        # get node and save in set of all nodes
        key, value = line.split()
        node = key[1:]
        allNodes.add(node)

        # set iteration value
        iteration = value[0]

        # pass the original line along to output
        sys.stdout.write(line)

    # case for unknown line
    else:

        # make a note in the error log and continue
        sys.stderr.write("elsecase process_map\n")
        sys.stderr.write('\t' + line + '\n')
        pass


# find nodes of unknown rank (they contributed all their rank to child nodes but
# have no parent nodes to get rank from)
# TODO this loop is fucking expensive you know
for node in allNodes:
    if node not in seenNodes:

        # emit a line giving this node (1-ALPHA) rank
        out = '+' + node + '\t' + `iteration` + ',' + `1 - ALPHA`
        print out
