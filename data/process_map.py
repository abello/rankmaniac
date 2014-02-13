#!/usr/bin/env python

import sys

ALPHA = 0.85

seenNodes = set() # set of nodes we already have shits of
nodes = set() # set will hold ALL node id's (even those without parents)

# read a line of input
for orig_line in sys.stdin:
    line = orig_line.split()[1]

    # if line starts with '_' it's adj info; pass it along but also save its 
    # node so that at the end we'll have a full list of nodes - INCLUDING nodes
    # that do not have any parents!
    if line[0] == '_':
        sys.stdout.write(orig_line) # (doesn't need newline)

        info = line[1:].split(',')

        # record the node in our set
        nodes.add(int(info[1]))

    # else line starts with '+' and it's contrib info; grab it
    else:
#elif line[0] == '+':
        sys.stdout.write(orig_line)

        # decode (unescape) and un-pickle the line
        info = line[1:].split(',')

        # save each value the line holds
        iteration = int(info[0])
        node      = int(info[1])
        contrib   = float(info[2])

        seenNodes.add(node)

# find every node in the graph without parents
# and initialize its pagerank to zero
for n in (nodes - seenNodes):
    print str(n) + '\t+' + str(iteration) + ',' + str(n) + ',' + str(1.0 - ALPHA)

