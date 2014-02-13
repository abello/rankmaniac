#!/usr/bin/env python

import sys

#'''
#Format of INPUT contribution lines:
#    +node \t iteration,contrib
#
#Format of INPUT and OUTPUT adjacency lines:
#    _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
#
#Format of OUTPUT rank lines:
#    +node \t iteration,rank
#'''

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
        if n not in result.keys():
            result[n] = float(contrib)
        else:
            result[n] += float(contrib)

    # case for adjacency line
    else:

        # pass the line right along to output
        sys.stdout.write(line)


# loop over every node that was given pagerank
# INCLUDES
#   nodes with parents
#   nodes without children
# DOESN'T INCLUDE
#   nodes without parents but with children

for node in result.keys():

    # calculate and emit the ALPHA scaled rank
    rank = (ALPHA*result[node]) + (1-ALPHA)
    out = '+' + node + '\t' + str(iteration) + ',' + str(rank)
    print out
