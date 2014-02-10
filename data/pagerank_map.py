import sys
import numpy as np

def firstIteration():
    # list of the nodes in the system to pass to reduce
    nodes = set()
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
        for link in outLinks:
            contribution = rank_curr / len(outLinks)
            result = 'c' + str(iteration) + ':' + str(link) + ':' + str(contribution) + '\n'
            sys.stdout.write(result)

        sys.stdout.write(line)

    # output the nodes in this
    nodeString = 'n'
    for n in nodes:
        nodeString += (str(n) + ',')
    sys.stdout.write(nodeString + '\n')


def midIteration():
    # list of the nodes in the system to pass to reduce
    nodes = set()
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
        
        # lines will be formatted as:
        # 3:0:2.0,10,20,30
        # where 3 is the iteration
        # 0 is the node identifier
        # 2.0 is current rank
        # the rest are the nodes that 0 links to

        split_line = line.split(':')
        data = split_line[2].split(',')

        iteration = int(split_line[0])
        node = int(split_line[1])
        rank_curr = float(data[0])
        outLinks = np.array([int(x) for x in data[1:-1]])
        
        # add the node to our list
        nodes.add(node)
            
        # what we want to emit to collector is information of node, and
        # contribution this node provides to its pagerank
        # the nodes will be each node in the outLinks, and the contribution
        # of this node is its current pagerank divided by its outDegree
        # This can be seen by looking at the pi' = pi*G rule of iteration
        # pagerank
        for link in outLinks:
            contribution = rank_curr / len(outLinks)
            result = 'c' + str(iteration) + ':' + str(link) + ':' + str(contribution) + '\n'
            sys.stdout.write(result)

        sys.stdout.write(line)

    # output the nodes in this
    nodeString = 'n'
    for n in nodes:
        nodeString += (str(n) + ',')
    sys.stdout.write(nodeString + '\n')



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
        
