#!/usr/bin/env python


import sys
import numpy as np
import cPickle as pickle

def firstIteration(firstLine):
    '''
    This only runs on the first iteration of the computation. Because of this,
    it's designed to parse default-formatted lines from an input.txt file using
    the sys.stdin buffer. It outputs two kinds of strings:

        Of the form "+:node\titeration:contribution"
            There is one line for every time a given parent contributes rank to
            a given node.
            
        Of the form "_:node\titeration:rank_curr:rank_prev:c:h:i:l:d:r:e:n"
            There is one line for every line in the original input.txt (because
            we need to preserve all adjacency information).
    '''

    iteration = 0

    # Each input line will be formatted as:
    # NodeId:node \t rank_curr,rank_prev,c,h,i,l,d,r,e,n

    # break up first line into manageable chunks
    key, value = firstLine.split('\t')
    values = value.split(',')

    # save elements from strings
    node      = key[7:]
    rank_curr = float(values[0])
    rank_prev = float(values[1])
    outLinks  = np.array(values[2:])

    # if current node has one or more children, split its pagerank equally
    # and distribute to each of them:
    if len(outLinks) > 0:
        contrib = rank_curr / len(outLinks)
        for child in outLinks:
            # (node, rank) pair lines start with a '+'
            result = '+:' + child + '\t' + str(iteration) + ':' + str(contrib)
            print result

    # else if current node has no children, keep its pagerank in a block and
    # assign it to itself:
    else:
        # (node, rank) pair lines start with a '+'
        result = '+:' + node + '\t' + str(iteration) + ':' + str(rank_curr)
        print result

    # make a record of this node, its rank(s), and its children, in order to
    # pass on the structure of the graph as many times as the function runs.
    # adjacency information lines start with a '_'
    adj = ('_:' + node + '\t' + str(iteration) + ':' + str(rank_curr) + ':' + 
           str(rank_prev) + ':' + ':'.join(outLinks))
    print adj


    # get line of input
    for line in sys.stdin:

        iteration = 0

        # Each input line will be formatted as:
        # NodeId:node \t rank_curr,rank_prev,c,h,i,l,d,r,e,n

        # break up line into manageable chunks
        key, value = line.split('\t')
        values = value.split(',')

        # save elements from strings
        node      = key[7:]
        rank_curr = float(values[0])
        rank_prev = float(values[1])
        outLinks  = np.array(values[2:])

        # if current node has one or more children, split its pagerank equally
        # and distribute to each of them:
        if len(outLinks) > 0:
            contrib = rank_curr / len(outLinks)
            for child in outLinks:
                # (node, rank) pair lines start with a '+'
                result = '+:' + child + '\t' + str(iteration) + ':' + str(contrib)
                print result

        # else if current node has no children, keep its pagerank in a block and
        # assign it to itself:
        else:
            # (node, rank) pair lines start with a '+'
            result = '+:' + node + '\t' + str(iteration) + ':' + str(rank_curr)
            print result

        # make a record of this node, its rank(s), and its children, in order to
        # pass on the structure of the graph as many times as the function runs.
        # adjacency information lines start with a '_'
        adj = ('_:' + node + '\t' + str(iteration) + ':' + str(rank_curr) + ':' + 
               str(rank_prev) + ':' + ':'.join(outLinks))
        print adj



def midIteration(firstLine):
    '''
    This runs on every iteration of the computation but the first. Because of
    this, it's designed to parse formatted lines from an input.txt file using
    the sys.stdin buffer. It outputs two kinds of strings:

        Of the form "+:node\titeration:contribution"
            There is one line for every time a given parent contributes rank to
            a given node.
            
        Of the form "_:node\titeration:rank_curr:rank_prev:c:h:i:l:d:r:e:n"
            There is one line for every line in the original input.txt (because
            we need to preserve all adjacency information).
    '''

    # Each input line will be formatted like the following example:
    #   np.array[iteration, node, rank_curr, rank_prev, np.array[outLinks]]

    # decode (unescape) and un-pickle the line
    index = firstLine.find('\t')
    firstLine = firstLine[index+1:]
    temp = firstLine.decode('string-escape')
    info = pickle.loads(temp)

    # save each value the line holds
    iteration = info[0]
    node      = info[1]
    rank_curr = info[2]
    rank_prev = info[3]
    outLinks  = info[4]

    # if current node has one or more children, split its pagerank equally
    # and distribute to each of them:
    if len(outLinks) > 0:
        contrib = (float(rank_curr)/len(outLinks))
        for link in outLinks:
            # (node, rank) pair lines start with a '+'
            result = '+' + pickle.dumps((iteration, link, contrib))
            result = result.encode('string-escape')
            result = str(link) + '\t' + result
            print result # (needs newline)

    # else if current node has no children, keep its pagerank in a block and
    # assign it to itself:
    else:
        # (node, rank) pair lines start with a '+'
        result = '+' + pickle.dumps((iteration, node, rank_curr))
        result = result.encode('string-escape')
        result = str(node) + '\t' + result
        print result # (needs newline)

    # make a record of this node, its rank(s), and its children, in order to
    # pass on the structure of the graph as many times as the function runs.
    # adjacency information lines start with a '_'
    adj = '_' + firstLine.decode('string-escape')[:-1]
    adj = adj.encode('string-escape')
    adj = 'adj\t' + adj
    print adj # (needs newline)

    for line in sys.stdin:
        # Each input line will be formatted like the following example:
        #   np.array[iteration, node, rank_curr, rank_prev, np.array[outLinks]]

        # decode (unescape) and un-pickle the line
        index = line.find('\t')
        line = line[index+1:]
        temp = line.decode('string-escape')
        info = pickle.loads(temp)

        # save each value the line holds
        iteration = info[0]
        node      = info[1]
        rank_curr = info[2]
        rank_prev = info[3]
        outLinks  = info[4]

        # if current node has one or more children, split its pagerank equally
        # and distribute to each of them:
        if len(outLinks) > 0:
            contrib = (float(rank_curr)/len(outLinks))
            for link in outLinks:
                # (node, rank) pair lines start with a '+'
                result = '+' + pickle.dumps((iteration, link, contrib))
                result = result.encode('string-escape')
                result = str(link) + '\t' + result
                print result # (needs newline)

        # else if current node has no children, keep its pagerank in a block and
        # assign it to itself:
        else:
            # (node, rank) pair lines start with a '+'
            result = '+' + pickle.dumps((iteration, node, rank_curr))
            result = result.encode('string-escape')
            result = str(node) + '\t' + result
            print result # (needs newline)

        # make a record of this node, its rank(s), and its children, in order to
        # pass on the structure of the graph as many times as the function runs.
        # adjacency information lines start with a '_'
        adj = '_' + line.decode('string-escape')[:-1]
        adj = adj.encode('string-escape')
        adj = 'adj\t' + adj
        print adj # (needs newline)



#stdin filepointer
stdin = sys.stdin

# Get first line and back up original position 
sample = stdin.readline()

# Choose iteration type
firstIteration(sample) if sample[0]=='N' else midIteration(sample)
