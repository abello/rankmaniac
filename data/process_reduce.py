#!/usr/bin/env python

import sys
import heapq as h
import numpy as np
import cPickle as pickle

max_iter = 50

def main():
    adjacency = {}
    pageRanks = {}

    # this will hold information of pageranks is we are on last iteration
    result = []

    iteration = 0

    for line in sys.stdin:
        if line[0] == '_':
            # this is the case that we are reading the total list of nodes
            # use this to fill out ourdictionary

            # adj = '_' + pickle.dumps(np.array(iteration, node, rank_curr, rank_prev, outLinks))
            unpickled = pickle.loads(line[1:])
            iteration = unpickled[0]

            # if iteration is our max iteration, we just stop, no need to process this
            if iteraton == max_iter:
                continue

            node = unpickled[1]
            outLinks = unpickled[4]
            adjacency[node] = np.array([iteration + 1, node, outLinks])
        elif line[0] == '+':
            info = pickle.loads(line[1:])

            iteration = info[0]
            node = info[1]
            pr = info[2]

            if iteration == max_iter:
                h.heappush(result, (-pr, node))
            else:
                pageRanks[node] = pr


    if iteration == max_iter:
        finalRanks = ''
        for i in range(20):
            try:
                (pr, n) = h.heappop(result)
                finalRanks += ('FinalRank:' + str(-pr) + '\t' + str(n) + '\n')
            except Exception, e:
                print e
        sys.stdout.write(finalRanks)
    else:
        for n in adjacency.keys():
            a = adjacency[n]
            result = pickle.dumps(np.array([a[0], a[1], pageRanks[n], a[2]]))
            sys.stdout.write(result)


if __name__ == "__main__":
    main()
