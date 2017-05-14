This is a parallel implementation of the sieve of Eratosthenes using MPI

### running the code

* To compile the code: mpicc erato_parallel.cpp -lm -o erato

* To run the code: mpirun -np < p > ./erato < n > < DEBUG >

    - n is the value up to which we execute the sieve
    - p is the number of threads to allocate
    - DEBUG: If set to 1, displays the status of the program and slows it down (Optional, default: 0).
