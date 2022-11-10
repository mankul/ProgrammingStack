#include<iostream>
#include<vector>
using namespace std;


// a function to be evaluated by compiler as const expression. contains only return statement.
constexpr int evaluateFunction(const int constant){
	return constant;
}


double sum(vector<int> &list ){
	return 1.9;
}


// const won;t be changed by function
double constSum(const vector<int> &list ){// access references. unnecessary copy of data is avoided
	// list.push_back(20);// const object won;t be updated
	return 1.9;
}


int main(){

	int variable = 10;
	const int constVariable = 20; 
	
	// constexpr evaluated at compile time.
	constexpr int constexpression = constVariable * constVariable; // (error < c++11)
	constexpr int constexpressionFromFunction = evaluateFunction(constVariable); // >= c++11 returns constexpr. error on returning const


	vector<int> vec = {1,2,3};
	double db = sum(vec);
	const double cb = constSum(vec);
	// constexpr double ceb = constSum(vec);

	int array[10] = {1,2};// two places initialized by 1, 2 rest by 0s
	for(int i = 0; i < 10; i++){
		cout<<array[i]<<"\t";
	}
	cout<<endl;

	for(auto i: array){
		cout<<i<<endl;
	}
	for(auto item: {1,2,3,4,5}){
		cout<<item<<endl;
	}
return 0;
}
