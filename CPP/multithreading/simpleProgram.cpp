#include<iostream>
#include<thread>
#include<chrono>

#define MAX_ITERATIONS 10

void worker(){
    for(int i = 0; i < MAX_ITERATIONS; i++){
        std::cout<<"Loop "<<i<<std::endl;
    }
}

// void worker(int num){
//     for(int i = 0; i < num; i++){
//         std::cout<<"Loop "<<i<<std::endl;
//     }
// }


int main(){


    std::thread t1;
    std::thread t2;

    try{
        t1(worker);
        t2(worker);
    }
    catch(...){
        std::cout<<"some exception happened"<<std::endl;
    }


    t1.join();
    t2.join();



    return 0;
}