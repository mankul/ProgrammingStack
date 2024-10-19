g++ -fPIC -shared example.cpp -o libexample.so
g++ test1.cpp -L. -lexample -o test1.out
