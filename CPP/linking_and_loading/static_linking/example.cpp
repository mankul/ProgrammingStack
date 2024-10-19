#include"example.hpp"


Integer::Integer(int val){
	data = val;
}

Integer Integer::add(const Integer & I){
	return data + I.data;
}

void Integer::display(){
	std::cout<<data<<std::endl;
}
