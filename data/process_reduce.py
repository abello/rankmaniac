#!/usr/bin/env python

import sys
import heapq as h
import numpy as np
import cPickle as pickle

MAX_ITER = 21 # maximum number of iterations of pagerank mapreduce to run

def main():
    adjacency = {}   # dict records node information and graph structure
    pageRanks = {}   # dict records node pagerank
    result_heap = [] # heap records sorted pagerank information from MAX_ITER

    iteration = 0

    # get a line of input
    for line in sys.stdin:

        # if line starts with '_' it's adj info; grab it and store the data in
        # our adjacency dictionary.
        if line[0] == '_':
            
            # decode (unescape) and un-pickle the line
            line = line.decode('string-escape')
            info = pickle.loads(line[1:])

            # begin saving each value the line holds
            iteration = info[0]
            # (if iteration is MAX_ITER, just stop, no need to process the rest)
            if iteration == MAX_ITER:
                continue
            node      = info[1]
            rank_curr = info[2]
            outLinks  = info[4]
            
            # record node info in adjacency dictionary
            adjacency[node] = (iteration + 1, node, rank_curr, outLinks)

        # else line starts with '+' and it's contrib info; grab it and store the
        # data in our pageRanks dictionary if we're not done, or in our heap if
        # we are done.
        else:
            
            # decode (unescape) and un-pickle the line
            line = line.decode('string-escape')
            info = pickle.loads(line[1:])

            # begin saving each value the line holds ("pr" means page rank)
            iteration = info[0]
            node      = info[1]
            pr        = info[2]

            if iteration == MAX_ITER:
                # if this contrib info is from the last iteration, push it into
                # our pagerank-sorted heap. (By pushing a negative pagerank, we
                # ensure that the first value popped from the heap is actually
                # our largest pagerank, etc.)
                h.heappush(result_heap, (-pr, node))
            else:
                # otherwise, update corresponding entry in the pagerank dict.
                pageRanks[node] = pr

    # if the data for the max iteration has been completely collected
    if iteration == MAX_ITER:

        # create a string of FinalRanks by popping the top 20 "most negative"
        # values from the result heap.
        finalRanks = ''
        for i in range(20):
            try:
                (pr, n) = h.heappop(result_heap)
                finalRanks += ('FinalRank:' + str(-pr) + '\t' + str(n)+ '\n')
            except Exception, e:
                print e
        print finalRanks

    # else if not every iteration has been run yet
    else:

        # for every node in the graph, pickle, encode and print its adj info.
        # NOTE: we do not prepend '_' here; this output is for the consumption
        # of paegrank_map.midIteration() only.
        for n in adjacency.keys():
            a = adjacency[n]
            out = pickle.dumps((a[0], a[1], pageRanks[n], a[2], a[3]))
            out = out.encode('string-escape')
            print out # (newline required)


if __name__ == "__main__":
    main()
