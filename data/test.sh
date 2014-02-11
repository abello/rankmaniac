#!/bin/bash

i=1
let stop=$1+i

# input2 will be intermediate input
cp input.txt input2.txt

input='input2.txt'
output='output.txt'

while [ $i -lt $stop ]
do
    python pagerank_map.py < $input | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > $output


    # Swap input with output, to go to next iter
    rm input2.txt
    cp output.txt input2.txt
    
    echo $i
    let i=i+1
done

# cleanup
rm input2.txt
