#!/usr/bin/env python

import sys
import heapq as h
import numpy as np
import cPickle as pickle

# 12 gives correct results for local graph
# TODO: Dynamically figure this out
MAX_ITER = 15 # maximum number of iterations of pagerank mapreduce to run

def main():

    adjacency    = {}   # dict records node information and graph structure
    pageRanks    = {}   # dict records node pagerank
    iteration    = 0    # tracks which iteration is being run
    threshold_pr = 0    # the smallest pagerank stored in result_heap

    # result_heap will record top 20 pageranks of all MAX_ITER runs.  we push 20
    # (-1, -1) pairs into it at the start to define its size:
    result_heap = []
    for i in range(20):
        h.heappush(result_heap, (-1, -1))

    # get a line of input
    for line in sys.stdin:
        index = line.find('\t')
        line = line[index+1:]


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

        # else line starts with '+' & it's contrib info; grab it for processing
        elif line[0] == '+':
            
            # decode (unescape) and un-pickle the line
            line = line.decode('string-escape')
            info = pickle.loads(line[1:])

            # begin saving each value the line holds ("pr" means page rank)
            iteration = info[0]
            node      = info[1]
            pr        = info[2]

            # if this isn't the last iteration:
            if iteration != MAX_ITER:

                # save the pagerank to be output for the next iteration
                pageRanks[node] = pr

            # else this is the last iteration:
            else:

                # if pagerank is larger than the smallest-pr-in-heap
                if pr > threshold_pr:

                    # remove smallest-pr-from-the heap and push the new pr into
                    # it (note that size of heap is maintained)
                    h.heappush(result_heap, (pr, node))
                    h.heappop(result_heap)

                    # update the threshold value to the new smallest-pr-in-heap
                    threshold_pr, _ = h.nsmallest(1, result_heap)[0]
        else:
            #victor
            print "elsecase: " + line

    # if not every iteration has run yet
    if iteration != MAX_ITER:

        # for every node in the graph, pickle, encode and print its adj info.
        # NOTE: we do not prepend '_' here; this output is for the consumption
        # of pagerank_map.midIteration() only.
        for n in adjacency.keys():
            a = adjacency[n]
            out = pickle.dumps((a[0], a[1], pageRanks[n], a[2], a[3]))
            out = out.encode('string-escape')
            out = str(a[1]) + '\t' + out
            print out # (newline required)

    # else if the last iteration has finished running
    else:

        top_prs = h.nlargest(20, result_heap)   # get list from heap
        top_prs = sorted(top_prs, reverse=True) # sort list from large to small

        # create a string containing lines for all top 20 nodes and their ranks.
        finalRanks = ''
        for i in range(20):
            try:
                pr, n = top_prs[i]
                finalRanks += ('FinalRank:' + str(pr) + '\t' + str(n)+ '\n')
            except Exception, e:
                print e

        # send the final result to the output
        sys.stdout.write(finalRanks)


if __name__ == "__main__":
    main()
