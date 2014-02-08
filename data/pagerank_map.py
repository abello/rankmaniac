#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

result = {}
for line in sys.stdin:
    # each line is of the format:  NodeId:0\t1.0,0.0,83,212,302...
    # 0 is current node id
    # 1.0 is current pagerank
    # 0.0 is previous page
    # 83, 212, 302, ... etc are children of node

    # break up line into manageable chunks
    split_line = line.split()
    if len(split_line) <= 1:
        sys.stdout.write(str(int(split_line[0]) + 1) + "\n")
        continue
    attributes = split_line[1].split(',')

    # save elements from strings
    parent = int(split_line[0][7:])
    rank_curr = float(attributes[0])
    rank_prev = float(attributes[1])
    children = [int(x) for x in attributes[2:]]

    # create entry in result dict with attributes of node 'parent'
    result[parent] = {'rank_curr':rank_curr,
                      'rank_prev':rank_prev,
                      'children':children}

    # Original placeholder code:
    if rank_prev == 0.0:
        sys.stdout.write("0\n")

