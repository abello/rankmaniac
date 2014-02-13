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

seenNodes = set() # nodes we already have shits of
nodes     = set() # all nodes (even those without parents)

# read a line of input
for orig_line in sys.stdin:
    line = orig_line.split()[1]

    # if line starts with '_' it's adj info; pass it along but also save its 
    # node so that at the end we'll have a full list of nodes - INCLUDING nodes
    # that do not have any parents!
    if line[0] == '_':
        sys.stdout.write(orig_line) # (doesn't need newline)

        # decode (unescape) and un-pickle the line
        line = line.decode('string-escape')
        unpickled = pickle.loads(line[1:])

        # record the node in our set
        nodes.add(unpickled[1])

    # else line starts with '+' and it's contrib info; grab it
    elif line[0] == '+':
        sys.stdout.write(orig_line)

        # decode (unescape) and un-pickle the line
        line = line.decode('string-escape')
        info = pickle.loads(line[1:])

        # save each value the line holds
        iteration = info[0]
        node      = info[1]
        contrib   = info[2]

        seenNodes.add(node)
    else:
        #victor
        pass

# find every node in the graph without parents
# and initialize its pagerank to zero
for n in nodes:
    if n not in seenNodes:
        out = '+' + pickle.dumps([iteration, n, 1 - ALPHA])
        out = out.encode('string-escape')
        print out # (newline needed)

