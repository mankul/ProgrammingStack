#include<iostream>

int main(){
    const int c = 10;
    const int r = 20;
    const int * d = &r;
    try{
        d=&c; // A runtime error will be raised.
        throw std::runtime_error("Can not reinitialize const pointer");
    }
    catch (std::runtime_error & e)
    {
        std::cout<<"Error Exception "<<e.what()<<std::endl;
    }

    return 0;
}

