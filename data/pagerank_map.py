import sys
import numpy as np
import cPickle as pickle

def firstIteration():
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
        node = int(split_line[0][7:])
        rank_curr = float(attributes[0])
        rank_prev = float(attributes[1])
        outLinks = np.array([int(x) for x in attributes[2:]])

        # if current node has one or more children, split its pagerank equally
        # and distribute to each of them:
        if len(outLinks) > 0:
            contrib = float(rank_curr) / len(outLinks)
            for child in outLinks:
                # (node, rank) pair lines start with a '+'
                result = '+' + pickle.dumps(np.array([iteration, child, contrib]))
                result = result.encode('string-escape')
                print result

        # else if current node has no children, keep its pagerank in a block and
        # assign it to itself:
        else:
            # (node, rank) pair lines start with a '+'
            result = '+' + pickle.dumps(np.array([iteration, node, rank_curr]))
            result = result.encode('string-escape')
            print result

        # make a record of this node, its rank(s), and its children, in order to
        # pass on the structure of the graph as many times as the function runs.
        # adjacency information lines start with a '_'
        adj = '_' + pickle.dumps((iteration, node, rank_curr, rank_prev, outLinks))
        adj = adj.encode('string-escape')
        print adj



def midIteration():
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

    for line in sys.stdin:
        # Each input line will be formatted like the following example:
        #   np.array[iteration, node, rank_curr, rank_prev, np.array[outLinks]]

        # decode (unescape) and un-pickle the line
        temp = line.decode('string-escape')
        info = pickle.loads(temp)

        # save each value in the line
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
                result = '+' + pickle.dumps(np.array([iteration, link, contrib]))
                result = result.encode('string-escape')
                print result

        # else if current node has no children, keep its pagerank in a block and
        # assign it to itself:
        else:
            # (node, rank) pair lines start with a '+'
            result = '+' + pickle.dumps(np.array([iteration, node, rank_curr]))
            result = result.encode('string-escape')
            print result

        # make a record of this node, its rank(s), and its children, in order to
        # pass on the structure of the graph as many times as the function runs.
        # adjacency information lines start with a '_'
        adj = '_' + line.decode('string-escape')[:-1]
        adj = adj.encode('string-escape')
        print adj



#stdin filepointer
stdin = sys.stdin

# Get first line and back up original position 
initial_pos = stdin.tell()
sample = stdin.readline()

# Choose iteration type
stdin.seek(initial_pos)
firstIteration() if sample[0]=='N' else midIteration()
