#!/usr/bin/env python2.5

import sys
import heapq as h

# 12 gives correct results for local graph
# TODO: Dynamically figure this out
MAX_ITER = 15 # maximum number of iterations of pagerank mapreduce to run
ALPHA = 0.85

def main():
    '''
    Format of INPUT and OUTPUT rank lines:
        +node \t iteration,rank

    Format of INPUT and OUTPUT adjacency lines:
        _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
    '''

    adjacency    = {}   # dict records node information and graph structure
    pageRanks    = {}   # dict records node pagerank
    iteration    = 0    # tracks which iteration is being run
    threshold_pr = 0    # the smallest pagerank stored in result_heap

    # result_heap will record top 20 pageranks of all MAX_ITER runs.  we push 20
    # (-1, -1) pairs into it at the start to define its size:
    result_heap = []
    for i in range(20):
        h.heappush(result_heap, (-1, -1))


    #----------------------------#
    #  Reduce all passed input:  #
    #----------------------------#

    for line in sys.stdin:

        # case for contribution line
        if line[0] == '+':

            # break up input into key and value
            key, value = line.split()
            values     = value.split(',')

            # save information of this node
            node      = key[1:]
            iteration = int(values[0])
            pr        = float(values[1])

            # if this isn't the last iteration
            if iteration != MAX_ITER:

                # save the pagerank to be output for the next iteration
                pageRanks[node] = pr

            # else this is the last iteration
                # if pagerank is larger than the smallest-pr-in-heap
            elif pr > threshold_pr:


                # remove smallest-pr-from-the heap and push the new pr into
                # it (note that size of heap is maintained)
                h.heapreplace(result_heap, (pr, node))

                # update the threshold value to the new smallest-pr-in-heap
                threshold_pr, _ = h.nsmallest(1, result_heap)[0]

        # case for adjacency line
        else:

            # break up input into key and value
            key, value = line.split()
            values     = value.split(',')

            # save information of this node
            iteration = int(values[0])
            # if the last iteration, just stop, no need to process the rest
            if iteration == MAX_ITER: continue
            node = key[1:]
            rank_curr = float(values[1])
            rank_prev = float(values[2])
            outLinks  = values[3:]

            # record node in adjacency dictionary
            adjacency[node] = (iteration+1, rank_curr, rank_prev, outLinks)            


    #----------------------------------------------------------#
    #  Now either loop for another iteration or print output:  #
    #----------------------------------------------------------#

    # if not every iteration has run yet
    if iteration != MAX_ITER:

        # For every node in the graph, emit its adj info.  The new rank_curr is
        # retrieved from our pageRanks dict, and the old rank_curr replaces the
        # old rank_prev.
        for node in adjacency:
            rank_curr = pageRanks[node]
            iteration, rank_prev, _, outLinks = adjacency[node]

            outLinks[:] = [x for x in outLinks if x != '']

            if len(outLinks) == 0:
                print ('_' + node + '\t' + str(iteration) + ',' + str(rank_curr) +
                      ',' + str(rank_prev))
            else:
                print ('_' + node + '\t' + str(iteration) + ',' + str(rank_curr) +
                      ',' + str(rank_prev) + ',' + ','.join(outLinks))


    # else the last iteration has completed
    else:

        top_prs = h.nlargest(20, result_heap)   # get list from heap
        top_prs = sorted(top_prs, reverse=True) # sort list from large to small

        # create one string with lines for each of the top 20 nodes and their
        # ranks, delimiting them with newline characters.
        finalRanks = ''
        for i in range(20):
            pr, node = top_prs[i]
            #sys.stderr.write('pagerank: ' + str(pr) + '\n')
            #sys.stderr.write('node id:  ' + str(node) + '\n')
            finalRanks += ('FinalRank:' + str(pr) + '\t' + str(node) + '\n')

        # send the final result to the output
        sys.stdout.write(finalRanks)



if __name__ == "__main__":
    main()
