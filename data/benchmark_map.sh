#!/bin/zsh

for i in {1..10}; do time python pagerank_map.py < input.txt >/dev/null ; done
