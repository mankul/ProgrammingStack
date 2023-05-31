#include<iostream>

using namespace std;

int main(){
	static double zero = 0;
	int fudging = 0;
	if(fudging) cout<<"fudging id set"<<endl;
	else cout<<"fudging is 0"<<endl;
	cout<<"not a number in cpp"<<endl;
	cout<<zero/zero<<endl;
	return 0;
}
