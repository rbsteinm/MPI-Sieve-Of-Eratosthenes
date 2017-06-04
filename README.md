### running the code locally

* To compile the code:
_mpicc erato_parallel.cpp -lm -lstdc++ -o erato_

* To run the code:
_mpirun -np < p > ./erato < n > < DEBUG >_

    - _n_ is the value up to which we execute the sieve
    - _p_ is the number of threads to allocate
    - _DEBUG_: If set to 1, displays the status of the program and slows it down (Optional, default: 0).
	
	
### running the code on the bellatrix cluster

* loading modules:
_module load gcc_
_module load mvapich2_

* compiling the code:
_mpicc erato_parallel.cpp -lm -lstdc++ -o erato_

* running the code:
_srun -n < p > ./erato < n >_

### Scripts
In the _scripts_ folder there are two bash scripts that are designed to run the sieve with different inputs and # of cores. One script performs a strong scaling and the other one a weak scaling.

### Plots
The results of the strong scaling and the weak scaling are stored in a text file in the _plots_ folder. In the same folder there are two python scripts to plot the values and store the resulting plots as two PNG files.
