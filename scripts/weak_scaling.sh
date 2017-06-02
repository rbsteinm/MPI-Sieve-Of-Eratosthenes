#!/bin/bash
#SBATCH --reservation phpc2017
#SBATCH --account phpc2017

# load the correct modules for the cluster
module load gcc
module load mvapich2

# compile the code
mpicc erato_parallel.cpp -lm -lstdc++ -o erato


echo "Weak Scaling: "
#number of problems per process
ppps=(1000 100000 1000000)
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