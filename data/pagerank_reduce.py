#!/usr/bin/env python

import sys
import numpy as np
import cPickle as pickle

# this dictionary will hold information of the pagerank contributions of
# each node
result = {}
iteration = 0

numLinks = 0
numAdj = 0

for line in sys.stdin:
 
    # This is adj information, pass it along
    if line[0] == '_':
        numAdj += 1
        sys.stdout.write(line)
        sys.stderr.write("test " + line)

    # If it starts with +, it's contribs
    # TODO: Make this an else while we show that this works
    elif line[0] == '+':
        numLinks += 1
        line = line.decode('string-escape')
        info = pickle.loads(line[1:])

        iteration = info[0]
        node = info[1]
        contribution = info[2]

        sys.stderr.write('INFO: ' + str(iteration) + ', ' + str(node) + '\n')
        if node in result.keys():
            result[int(node)] += contribution
        else:
            result[int(node)] = contribution
    else:
         sys.stderr.write('AAAAAAAAAAAAAAAAAAAAAAAA\n')

sys.stderr.write('iteration: ' + str(iteration) + ',' + str(numLinks) + '\n')
sys.stderr.write('iteration: ' + str(iteration) + ',' + str(numAdj) + '\n')
    
for node in result.keys():
    out = '+' + pickle.dumps(np.array([iteration, node, result[int(node)]]))
    out = out.encode('string-escape')
    print out
#     sys.stdout.write('+' + str(iteration) + ':' + str(r) + ':' + str(result[r]) + '\n')
    



