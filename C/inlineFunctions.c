#include<stdio.h>


inline void printStatements(int a){

	printf("Print Statement is an inline function, variable is int : %d\n",a);
}


int main(){
	int a = 10;

	printStatements(a);
return 0;
}
