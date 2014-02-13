#!/usr/bin/env python


import sys

def firstIteration(firstLine):
    '''
    Format of INPUT adjacency lines:
        NodeID:node \t rank_curr,rank_prev,c,h,i,l,d,r,e,n

    Format of OUTPUT contribution lines:
        +node \t iteration,contrib

    Format of OUTPUT adjacency lines:
        _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
    '''

    #----------------------#
    #  Process first line  #
    #----------------------#

    # break up input into key and value
    key, value = firstLine.split()
    values     = value.split(',')

    # save information of this node
    node      = key[7:]
    iteration = 0
    rank_curr = float(values[0])
    rank_prev = float(values[1])
    if values[2:] == ['']:
        outLinks = []
        assert(False)
    else:
        outLinks  = values[2:]

    # if current node has one or more children, split its pagerank equally
    # and distribute to each of them:
    if len(outLinks) > 0:
        contrib = rank_curr / len(outLinks)
        for child in outLinks:
            # +child \t iteration,contrib
            result = '+' + child + '\t' + str(iteration) + ',' + str(contrib)
            print result

    # else if current node has no children, keep its pagerank in a block and
    # assign it to itself:
    else:
        # +node \t iteration,rank_curr
        result = '+' + node + '\t' + str(iteration) + ',' + str(rank_curr)
        print result

    # print a line passing along adj information
    # _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
    adj = ('_' + node + '\t' + str(iteration) + ',' + str(rank_curr) + ',' +
           str(rank_prev) + ',' + ','.join(outLinks))
    print adj

    #---------------------------#
    #  Process all other lines  #
    #---------------------------#

    # get line of input
    for line in sys.stdin:
        
        # break up input into key and value
        key, value = line.split()
        values     = value.split(',')

        # save information of this node
        node      = key[7:]
        iteration = 0
        rank_curr = float(values[0])
        rank_prev = float(values[1])
        if values[2] == '':
            outLinks = []
            assert(False)
        else:
            outLinks  = values[2:]

        # if current node has one or more children, split its pagerank equally
        # and distribute to each of them:
        if len(outLinks) > 0:
            contrib = rank_curr / len(outLinks)
            for child in outLinks:
                # +child \t iteration,contrib
                result = '+' + child + '\t' + str(iteration) + ',' + str(contrib)
                print result

        # else if current node has no children, keep its pagerank in a block and
        # assign it to itself:
        else:
            # +node \t iteration,rank_curr
            result = '+' + node + '\t' + str(iteration) + ',' + str(rank_curr)
            print result

        # print a line passing along adj information
        # _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
        adj = ('_' + node + '\t' + str(iteration) + ',' + str(rank_curr) + ',' +
               str(rank_prev) + ',' + ','.join(outLinks))
        print adj



def midIteration(firstLine):
    '''
    Format of INPUT adjacency lines:
        _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n

    Format of OUTPUT contribution lines:
        +node \t iteration,contrib

    Format of OUTPUT adjacency lines:
        _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
    '''

    #----------------------#
    #  Process first line  #
    #----------------------#

    # break up input into key and value
    key, value = firstLine.split()
    values     = value.split(',')

    # save information of this node
    node       = key[1:]
    iteration  = int(values[0])
    rank_curr  = float(values[1])
    rank_prev  = float(values[2])
    if values[3:] == ['']:
        outLinks = []
        assert(False)
    else:
        outLinks  = values[3:]

    # if current node has one or more children, split its pagerank equally
    # and distribute to each of them:
    if len(outLinks) > 0:
        contrib = rank_curr / len(outLinks)
        for child in outLinks:
            # +child \t iteration,contrib
            result = '+' + child + '\t' + str(iteration) + ',' + str(contrib)
            print result

    # else if current node has no children, keep its pagerank in a block and
    # assign it to itself:
    else:
        # +node \t iteration,rank_curr
        result = '+' + node + '\t' + str(iteration) + ',' + str(rank_curr)
        print result

    # print a line passing along adj information
    # _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
    adj = ('_' + node + '\t' + str(iteration) + ',' + str(rank_curr) + ',' +
           str(rank_prev) + ',' + ','.join(outLinks))
    print adj

    #---------------------------#
    #  Process all other lines  #
    #---------------------------#

    for line in sys.stdin:
        
        # break up input into key and value
        key, value = line.split()
        values     = value.split(',')

        # save information of this node
        node       = key[1:]
        iteration  = int(values[0])
        rank_curr  = float(values[1])
        rank_prev  = float(values[2])
        if values[3:] == ['']:
            outLinks = []
            assert(False)
        else:
            outLinks  = values[3:]

        # if current node has one or more children, split its pagerank equally
        # and distribute to each of them:
        if len(outLinks) > 0:
            contrib = rank_curr / len(outLinks)
            for child in outLinks:
                # +child \t iteration,contrib
                result = '+' + child + '\t' + str(iteration) + ',' + str(contrib)
                print result

        # else if current node has no children, keep its pagerank in a block and
        # assign it to itself:
        else:
            # +node \t iteration,rank_curr
            result = '+' + node + '\t' + str(iteration) + ',' + str(rank_curr)
            print result

        # print a line passing along adj information
        # _node \t iteration,rank_curr,rank_prev,c,h,i,l,d,r,e,n
        adj = ('_' + node + '\t' + str(iteration) + ',' + str(rank_curr) + ',' +
               str(rank_prev) + ',' + ','.join(outLinks))
        print adj


#stdin filepointer
stdin = sys.stdin

# Get first line and back up original position 
sample = stdin.readline()

# Choose iteration type
firstIteration(sample) if sample[0]=='N' else midIteration(sample)
