#!/bin/bash

python data/pagerank_map.py < input.txt | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py > output.txt
