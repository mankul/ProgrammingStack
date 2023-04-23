decltype(auto) function1(){
    int x = 0;
    return x; // returns int. because (x) deduces to variable.
}

decltype(auto) function2(){
    int x =0;
    return (x); // returns reference to x int&. because ((x)) deduces to reference.
}