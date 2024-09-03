#include<iostream>



using namespace std;


class Constructors{

	int x;
	int * arr = nullptr;

    Constructors(){
        x = 0;
        std::cout<<"Default constructor is initialized"<<std::endl;
    }
    Constructors(const int size){
        this.arr = new int[size];
        x = 0;
    }

    // copy constructor
    Constructors(const Constructors& con){
        this->x = con.x;
        this.arr = new int[con.size];
        for(int i = 0; i < con.size; i++){
            this->arr[i] = con.arr[i];
        }
    }

    // move constructor
    Constructors(Constructors & con){
        con.swap(*this);
    }

    // copy assignment
    Constructors operator= (const Constructors & con){
        this->x = con.x;
        this->arr = conn.arr;
        return *this;
    }
    // move assignment
    Constructors operator= (Constructors & con){
        con.swap(*this);
        return *this;
    }

    // move assignment

    void swap(Constructors & con){
        std::swap(this->x, con.x);
        std::swap(this->arr, con.arr);
    }
};
