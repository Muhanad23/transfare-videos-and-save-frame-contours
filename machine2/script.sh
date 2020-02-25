#!/bin/bash
read n
read ipp
portnum=6999
START=1
for (( c=$START; c<=$n; c++ ));
do
	
	if [[ $(( $c  % 2 )) -ne 0 ]]
	then
	  portnum=$((portnum+1))
	fi

	python consumer2.py $portnum $ipp &

done

python resultcollector.py &

wait
