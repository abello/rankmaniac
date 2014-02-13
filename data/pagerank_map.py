#!/usr/bin/env python


import sys
import numpy as np

def firstIteration(firstLine):
    '''
    This only runs on the first iteration of the computation. Because of this,
    it's designed to parse default-formatted lines from an input.txt file using
    the sys.stdin buffer. It outputs pickled strings that are faster to process.

    There are two kinds of pickled output strings:
        Of the form "+" + pickledString:
            These contain [iter, child, contrib] np.arrays.  There is one line
            for every time a given parent contributes rank to a given child.
        Of the form "_" + pickledString:
            These contain [iter, node, rank_curr, rank_prev, [children]]
            np.arrays.  There is one line for every line in the original
            input.txt (because we need to preserve all adjacency information).
    '''


    # Each input line will be formatted like the following example
    #   NodeId:0\t1.0,0.0,83,212,302...
    # Mapping of values:
    #   0                   node id
    #   1.0                 current pagerank
    #   0.0                 previous pagerank
    #   83, 212, 302, ...   children ids

    
    # break up line into manageable chunks
    split_line = firstLine.split()
    attributes = split_line[1].split(',')

    # save elements from strings
    iteration = 0
    node      = int(split_line[0][7:])
    rank_curr = float(attributes[0])
    rank_prev = float(attributes[1])
    outLinks  = np.array([int(x) for x in attributes[2:]])

    # if current node has one or more children, split its pagerank equally
    # and distribute to each of them:
    if len(outLinks) > 0:
        contrib = float(rank_curr) / len(outLinks)
        for child in outLinks:
            # (node, rank) pair lines start with a '+'
            print str(child) + '\t' + '+' + str(iteration) + ',' + str(child) + ',' + str(contrib)
            #print result # (needs newline)

    # else if current node has no children, keep its pagerank in a block and
    # assign it to itself:
    else:
        # (node, rank) pair lines start with a '+'
        print str(node) + '\t' + '+' + str(iteration) + ',' + str(node) + ',' + str(rank_curr)
        #print result # (needs newline)

    # make a record of this node, its rank(s), and its children, in order to
    # pass on the structure of the graph as many times as the function runs.
    # adjacency information lines start with a '_'
    print 'adj\t_' + str(iteration) + ',' + str(node) + ',' + str(rank_curr) + ',' + str(rank_prev) + ',' + ','.join(attributes[2:])
#    for link in outLinks:
#        adj += (',' + str(link))
#    print adj # (needs newline)


    for line in sys.stdin:

        # Each input line will be formatted like the following example
        #   NodeId:0\t1.0,0.0,83,212,302...
        # Mapping of values:
        #   0                   node id
        #   1.0                 current pagerank
        #   0.0                 previous pagerank
        #   83, 212, 302, ...   children ids

        # TODO: Is a 0 initial pagerank optimal?
        
        # break up line into manageable chunks
        split_line = line.split()
        attributes = split_line[1].split(',')

        # save elements from strings
        iteration = 0
        node      = int(split_line[0][7:])
        rank_curr = float(attributes[0])
        rank_prev = float(attributes[1])
        outLinks  = np.array([int(x) for x in attributes[2:]])

        # if current node has one or more children, split its pagerank equally
        # and distribute to each of them:
        if len(outLinks) > 0:
            contrib = float(rank_curr) / len(outLinks)
            for child in outLinks:
                # (node, rank) pair lines start with a '+'
                print str(child) + '\t' + '+' + str(iteration) + ',' + str(child) + ',' + str(contrib)
                #print result # (needs newline)

        # else if current node has no children, keep its pagerank in a block and
        # assign it to itself:
        else:
            # (node, rank) pair lines start with a '+'
            print str(node) + '\t' + '+' + str(iteration) + ',' + str(node) + ',' + str(rank_curr)
            #print result # (needs newline)

        # make a record of this node, its rank(s), and its children, in order to
        # pass on the structure of the graph as many times as the function runs.
        # adjacency information lines start with a '_'
        print 'adj\t_' + str(iteration) + ',' + str(node) + ',' + str(rank_curr) + ',' + str(rank_prev) + ',' + ','.join(attributes[2:])
#        for link in outLinks:
#            adj += (',' + str(link))
#        print adj # (needs newline)



def midIteration(firstLine):
    '''
    This runs on evey iteration of the computation BUT the first.  Because of
    this, it's designed to parse custom pickled lines gotten from sys.stdin.  It 
    also outputs pickled strings.  NOTE: the output strings are formatted
    slightly differently; input strings don't have '_' and '+' prepended chars,
    and they are only adjacency lines - not contribution lines.

    There are two kinds of pickled output strings:
        Of the form "+" + pickledString:
            These contain [iter, child, contrib] np.arrays.  There is one line
            for every time a given parent contributes rank to a given child.
        Of the form "_" + pickledString:
            These contain [iter, node, rank_curr, rank_prev, [children]]
            np.arrays.  There is one line for every line in the original
            input.txt (because we need to preserve all adjacency information).
    '''

    # Each input line will be formatted like the following example:
    #   np.array[iteration, node, rank_curr, rank_prev, np.array[outLinks]]

    # decode (unescape) and un-pickle the line
    attributes = firstLine.split()[1].split(',')

    # save each value the line holds
    iteration = int(attributes[0])
    node      = int(attributes[1])
    rank_curr = float(attributes[2])
    rank_prev = float(attributes[3])
    outLinks  = np.array([int(x) for x in attributes[4:]])

    # if current node has one or more children, split its pagerank equally
    # and distribute to each of them:
    if len(outLinks) > 0:
        contrib = (float(rank_curr)/len(outLinks))
        for link in outLinks:
            # (node, rank) pair lines start with a '+'
            print str(link) + '\t' + '+' + str(iteration) + ',' + str(link) + ',' + str(contrib)
#print result # (needs newline)

    # else if current node has no children, keep its pagerank in a block and
    # assign it to itself:
    else:
        # (node, rank) pair lines start with a '+'
        print str(node) + '\t' + '+' + str(iteration) + ',' + str(node) + ',' + str(rank_curr)
        #print result # (needs newline)

    # make a record of this node, its rank(s), and its children, in order to
    # pass on the structure of the graph as many times as the function runs.
    # adjacency information lines start with a '_'
    print 'adj\t_' + str(iteration) + ',' + str(node) + ',' + str(rank_curr) + ',' + str(rank_prev) + ',' + ','.join(attributes[4:])
#    for link in outLinks:
#        adj += (',' + str(link))
#    print adj # (needs newline)

    for line in sys.stdin:
        # Each input line will be formatted like the following example:
        #   np.array[iteration, node, rank_curr, rank_prev, np.array[outLinks]]

        attributes = line.split()[1].split(',')

        # save each value the line holds
        iteration = int(attributes[0])
        node      = int(attributes[1])
        rank_curr = float(attributes[2])
        rank_prev = float(attributes[3])
        outLinks  = np.array([int(x) for x in attributes[4:]])

        # if current node has one or more children, split its pagerank equally
        # and distribute to each of them:
        if len(outLinks) > 0:
            contrib = (float(rank_curr)/len(outLinks))
            for link in outLinks:
                # (node, rank) pair lines start with a '+'
                print str(link) + '\t' + '+' + str(iteration) + ',' + str(link) + ',' + str(contrib)

        # else if current node has no children, keep its pagerank in a block and
        # assign it to itself:
        else:
            # (node, rank) pair lines start with a '+'
            print str(node) + '\t' + '+' + str(iteration) + ',' + str(node) + ',' + str(rank_curr)

        # make a record of this node, its rank(s), and its children, in order to
        # pass on the structure of the graph as many times as the function runs.
        # adjacency information lines start with a '_'
        print 'adj\t_' + str(iteration) + ',' + str(node) + ',' + str(rank_curr) + ',' + str(rank_prev) + ',' + ','.join(attributes[4:])
#        for link in outLinks:
#            adj += (',' + str(link))
#        print adj # (needs newline)



#stdin filepointer
stdin = sys.stdin

# Get first line and back up original position 
sample = stdin.readline()

# Choose iteration type
if sample[0] == 'N':
    firstIteration(sample)
else:
    midIteration(sample)
