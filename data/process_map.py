#!/usr/bin/env python

import sys
#import cPickle as pickle

'''
Format of INPUT contribution lines:
    +node \t iteration,contrib

Format of INPUT and OUTPUT adjacency lines:
    _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n

Format of OUTPUT rank lines:
    +node \t iteration,rank
'''

ALPHA = 0.85

seenNodes = set() # nodes with known and scaled ranks
allNode   = set() # all nodes (includes nodes without parents but with children)


for line in sys.stdin:

    # case for contribution line
    if line[0] == '+':

        # get node and save in set of nodes with known rank
        node = line.split()[0][1:]
        seenNodes.add(node)

        # pass the original line along to output
        sys.stdout.write(line)

    # case for adjacency line
    elif line[0] == '_':

        # get node and save in set of all nodes
        node = line.split()[0][1:]
        node.add(node)

        # pass the original line along to output
        sys.stdout.write(line)

    # case for unknown line
    else:

        # make a note in the error log and continue
        sys.stderr.write("elsecase process_map\n")
        pass


# find nodes of unknown rank (they contributed all their rank to child nodes but
# have no parent nodes to get rank from)
# TODO this loop is fucking expensive you know
for node in nodes:
    if node not in seenNodes:

        # emit a line giving this node (1-ALPHA) rank
        out = '+' + node + '\t' + str(iteration) + ',' + str(1 - ALPHA)
        print out