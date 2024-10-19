.PHONY: all
all: main

.PHONY: main
main: test1.cpp libmathlib.so
	g++ test1.cpp -L. -lmathlib -o test.out
.PHONY: libmathlib.so
libmathlib.so: example.cpp
	g++ -fPIC -shared example.cpp -o libmathlib.so

.PHONY: clean
clean:
	rm *.so *.o *.out
