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
ppps=(10000000 100000000 1000000000)
ps=(1 2 4 8 16 32 64)
for i in "${ppps[@]}"
do
	:
	for j in "${ps[@]}"
	do
		:
		n=$((${i}*${j}))
		srun -n $j ./erato $n
	done
done