#!/usr/bin/env python

import sys
import heapq as h
import numpy as np

max_iter = 50

def midIteration():
    nodeData = {}
    result = ''
    for line in sys.stdin:
        stripped = line.strip()
        split_line = stripped.split(':')

        iteration = int(split_line[0])
        node = int(split_line[1])
        pagerank = float(split_line[2])

        result += (str(iteration + 1) + ':' + str(node) + ':' + str(pagerank) + '\n')

    sys.stdout.write(result)

def lastIteration():
    # this will hold information of the pageranks
    result = []

    for line in sys.stdin:
        # lines will be formatted as:
        # 3:0:1.5
        # where 3 is the iteration
        # 0 is the node identifier
        # 1.5 is the pagerank

        stripped = line.strip()
        split_line = stripped.split(':')

        iteration = int(split_line[0])
        node = int(split_line[1])
        pagerank = float(split_line[2])

        h.heappush(result, (-pagerank, node))

    finalRanks = ''
    for i in range(20):
        try:
            (pr, n) = h.heappop(result)
            finalRanks += ('FinalRank:' + str(-pr) + '\t' + str(n) + '\n')
        except:
#TODO
            print 'fail'
            pass
            
    sys.stdout.write(finalRanks)

def main():
    nodeData = {}

    # this will hold information of pageranks is we are on last iteration
    result = []

    iteration = 0

    for line in sys.stdin:
        if line[0] == 'N':
            split_line = line.split()
            attributes = split_line[1].split(',')

            node = int(split_line[0][7:])
            outLinks = np.array([int(x) for x in attributes[2:]])

            nodeData[node] = outLinks
        elif line[0] == 'p':
            stripped = line[1:].strip()
            split_line = stripped.split(':')

            iteration = int(split_line[0])
            node = int(split_line[1])
            pagerank = float(split_line[2])

            if iteration < max_iter:
                toPrint = str(iteration + 1) + ':' + str(node) + ':' + str(pagerank) + ','
                for i in nodeData[node]:
                    toPrint += (str(i) + ',')
                sys.stdout.write(toPrint + '\n')
            else:
                h.heappush(result, (-pagerank, node))
        else:
            stripped = line.strip()
            split_line = stripped.split(':')
            attributes = split_line[2].split(',')

            node = int(split_line[1])
            outLinks = np.array([int(x) for x in attributes[1:-1]])

            nodeData[node] = outLinks

    if iteration >= max_iter:
        finalRanks = ''
        for i in range(20):
            try:
                (pr, n) = h.heappop(result)
                finalRanks += ('FinalRank:' + str(-pr) + '\t' + str(n) + '\n')
            except Exception, e:
#TODO
                print e
                pass
            
        sys.stdout.write(finalRanks)
                


if __name__ == "__main__":
    main()
