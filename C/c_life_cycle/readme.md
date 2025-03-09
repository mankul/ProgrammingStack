steps to run c
gcc -E sample.c -o sample.i
gcc -S sample.i -o sample.s
gcc -c sample.s -o sample.o
