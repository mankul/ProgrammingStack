.PHONY: all
all: main

.PHONY: main
main: test1.cpp libmathLIB.a
	g++ test1.cpp -L. -lmathLIB -o test1.out


libmathLIB.a: example.o
	ar -rc libmathLIB.a example.o

example.o: example.cpp
	g++ -fPIC -static -c example.cpp -o example.o
.PHONY: clean
clean:
	rm *.a *.o *.out
