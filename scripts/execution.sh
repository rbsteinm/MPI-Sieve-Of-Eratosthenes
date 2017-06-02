#!/bin/bash
#SBATCH --reservation phpc2017
#SBATCH --account phpc2017
#SBATCH --time 00:15:00

# load the correct modules for the cluster
module load gcc
module load mvapich2

# compile the code
mpicc erato_parallel.cpp -lm -lstdc++ -o erato

echo "Strong Scaling: "
ns=(50000000 100000000 200000000 500000000 1000000000 2000000000 5000000000 10000000000)
ps=(1 2 4 8 16 32 64)
for n in "${ns[@]}"
do
	:
	for i in "${ps[@]}"
	do
	   :
	   #mpirun -np $i ./erato $n
	   srun -n $i ./erato $n
	done
done

'
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
'