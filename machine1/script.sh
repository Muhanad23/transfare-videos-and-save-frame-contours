#!/bin/bash

echo "Enter number of consumers:"
read n
python producer.py &
n_2=$(($n/2))
if [ $((n%2)) -ne 0 ]
then
    n_2=$(($n_2+1))
fi
for (( c=0; c<$n_2; c++ ))
do
    python collector.py $c &
done

for (( c=0; c<$n; c++ ))
do
    python consumer.py $c &
done
wait