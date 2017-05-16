#!/bin/bash

# compile the code
mpicc erato_parallel.cpp -lm -lstdc++ -o erato

echo "Strong Scaling: "
ns=(10000 100000 1000000 10000000)
ps=(1 2 3 4)
for n in "${ns[@]}"
do
	:
	for i in "${ps[@]}"
	do
	   :
	   mpirun -np $i ./erato $n
	done
done

echo "Weak Scaling: "
#number of problems per process
ppps=(10000 20000 30000)
ps=(1 2 3)
for i in "${ppps[@]}"
do
	:
	for j in "${ps[@]}"
	do
		:
		n=$((${i}*${j}))
		mpirun -np $j ./erato $n
	done
done