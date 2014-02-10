import sys
import numpy as np
import cPickle as pickle

def firstIteration():
    # list of the nodes in the system to pass to reduce
    nodes = set()
    G = {}
    for line in sys.stdin:
        # each line is of the format:  NodeId:0\t1.0,0.0,83,212,302...
        # Or, if it's a subsequent iteration (say iteration 2):
        # each line will be of the format 2NodeId:0\t1.0,0.0,83,212,302...

        # 0 is current node id
        # 1.0 is current pagerank
        # 0.0 is previous page
        # 83, 212, 302, ... etc are children of node

        # save elements from strings
        # TODO: Is a 0 initial pagerank optimal?
        
        # break up line into manageable chunks
        split_line = line.split()
        attributes = split_line[1].split(',')

        iteration = 0
        node = int(split_line[0][7:])
        rank_curr = float(attributes[0])
        rank_prev = float(attributes[1])
        outLinks = np.array([int(x) for x in attributes[2:]])
        
        # add the node to our list
        nodes.add(node)

            
        # what we want to emit to collector is information of node, and
        # contribution this node provides to its pagerank
        # the nodes will be each node in the outLinks, and the contribution
        # of this node is its current pagerank divided by its outDegree
        # This can be seen by looking at the pi' = pi*G rule of iteration
        # pagerank

        if len(outLinks) == 0:
            result = '+' + pickle.dumps(np.array([iteration, node, rank_curr]))
            result = result.encode('string-escape')
            print result
        else:
            contribution = rank_curr / len(outLinks)
            
            for link in outLinks:
                # (child, contribution) pairs start with a '+'
                result = '+' + pickle.dumps(np.array([iteration, link, contribution]))
                result = result.encode('string-escape')
                print result


        # The adjlist stuff starts with _
        adj = '_' + pickle.dumps((iteration, node, rank_curr, rank_prev, outLinks))
        adj = adj.encode('string-escape')
        print adj


def midIteration():
    # list of the nodes in the system to pass to reduce
    nodes = set()
    # Expected format of line:
    # np.array(iteration, node, rank_curr, rank_prev, np.array(outLinks))
    for line in sys.stdin:
        decoded = line.decode('string-escape')
        info = pickle.loads(decoded)

        iteration = info[0]
        node = info[1]
        rank_curr = info[2]
        rank_prev = info[3]
        outLinks = info[4]
        
        # add the node to our list
        nodes.add(node)
            
        # what we want to emit to collector is information of node, and
        # contribution this node provides to its pagerank
        # the nodes will be each node in the outLinks, and the contribution
        # of this node is its current pagerank divided by its outDegree
        # This can be seen by looking at the pi' = pi*G rule of iteration
        # pagerank
        if len(outLinks) == 0:
            result = '+' + pickle.dumps(np.array([iteration, node, rank_curr]))
            result = result.encode('string-escape')
            print result
        else:
            contribution = rank_curr / len(outLinks)
            
            for link in outLinks:
                # (child, contribution) pairs start with a '+'
                result = '+' + pickle.dumps(np.array([iteration, link, contribution]))
                result = result.encode('string-escape')
                print result

        # The adjlist stuff starts with _
#        adj = '_' + pickle.dumps((iteration, node, rank_curr, rank_prev, outLinks))
#        adj = adj.encode('string-escape')
#        print adj
        adj = '_' + line.decode('string-escape')
        adj = adj.encode('string-escape')
        sys.stdout.write(adj)



# stdin filepointer
stdin = sys.stdin

# Get first line, backup original position 
initial_pos = stdin.tell()
sample = stdin.readline()

if sample[0] == 'N':
    stdin.seek(initial_pos)
    firstIteration()
else:
    stdin.seek(initial_pos)
    midIteration()
        
