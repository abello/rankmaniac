#!/usr/bin/env python

import sys
import numpy as np

#
# This program simply represents the identity function.
#

result = {}
for line in sys.stdin:
    # each line is of the format:  NodeId:0\t1.0,0.0,83,212,302...
    # Or, if it's a subsequent iteration (say iteration 2):
    # each line will be of the format 2NodeId:0\t1.0,0.0,83,212,302...

    # 0 is current node id
    # 1.0 is current pagerank
    # 0.0 is previous page
    # 83, 212, 302, ... etc are children of node

    # break up line into manageable chunks
    split_line = line.split()
    attributes = split_line[1].split(',')

    # save elements from strings
    # TODO: Is a 0 initial pagerank optimal?
    
    # If we're at first iteration
    if line[0] == 'N':
        iteration = 0
        parent = int(split_line[0][7:])
        rank_curr = float(attributes[0])
        rank_prev = float(attributes[1])
        children = np.array([int(x) for x in attributes[2:]])
    else:
        # TODO: Implement this
        iteration = 99999999999
        parent = int(split_line[0][7:])
        rank_curr = float(attributes[0])
        rank_prev = float(attributes[1])
        children = np.array([int(x) for x in attributes[2:]])
        

    # create entry in result dict with attributes of node 'parent'
    # TODO: Use a fixed-size hashtable instead of dict for memory optimization
    result[parent] = {'iteration':iteration,
                      'rank_curr':rank_curr,
                      'rank_prev':rank_prev,
                      'children':children}


    

    # Original placeholder code:
    sys.stdout.write(line)

