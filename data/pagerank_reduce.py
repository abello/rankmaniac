#!/usr/bin/env python

import sys
#import numpy as np
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

# dictionary will hold {node: sum_pagerank_of_node}
result = {} 

for line in sys.stdin:

    # case for contribution line
    if line[0] == '+':

        # break up input into key and value
        key, value = line.split()
        values = value.split(',')

        # save information of this node
        n = key[1:]
        iteration, contrib = values

        # ititialize or increment this node's rank in results dictionary
        result[n] = contrib if n not in result.keys() else result[n] + contrib

    # case for adjacency line
    elif line[0] == '_':

        # pass the line right along to output
        sys.stdout.write(line)

    # case for unknown line
    else:

        # make a note in the error log and continue
        sys.stderr.write("elsecase pagerank_reduce\n")
        pass


# loop over every node that was given pagerank
# INCLUDES
#   nodes with parents
#   nodes without children
# DOESN'T INCLUDE
#   nodes without parents but with children

for node in result.keys():

    # calculate and emit the ALPHA scaled rank
    rank = (ALPHA*result[node]) + (1-ALPHA)
    out = node + '\t' + str(iteration) + ',' + rank
    print out