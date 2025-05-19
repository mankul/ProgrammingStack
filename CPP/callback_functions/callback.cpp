#include<iostream>

// template <typename T>
void * callback_socket(int a, int b){
    // int c = a + b;
    // std::cout<<c<<std::endl;
    // return (void *) &c; // returning address to stack variable. Which will go out of scope once the function exits. Therefore it is not safe. and may lead to undefined behaviour.

    int * c = new int[1];
    c[0] = a+b;
    return (void *) c;
}

template <typename T>
void template_callback (T a){
    std::cout<<"Template callback"<<std::endl;
}


void socket_invoke(int s, void * (* callback_function)(int , int ), int a, int b){
    if (s > 10){
        void * address_to_output_var = callback_function(a, b);
        int * output_addr = (int *) address_to_output_var;
        std::cout<<output_addr<<std::endl;
    }
}


void socket_template_function(int s, void (* callback_function)(int)){
    if (s>10){
        callback_function(100);
    }
}

int main(){
    socket_invoke(11, callback_socket, 10,30);
    socket_template_function(15, template_callback);
    return 0;
}