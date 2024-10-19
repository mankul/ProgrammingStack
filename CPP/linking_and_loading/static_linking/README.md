g++ -fPIC -static -c example.cpp -o example.o
# for mac archive the object file to lib file
ar -rc libexample.a example.o
g++ test1.cpp -L. -lexample -o test1.out
