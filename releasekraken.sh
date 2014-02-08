#!/bin/bash

FILE1=$1

python data/pagerank_map.py < $FILE1 | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py