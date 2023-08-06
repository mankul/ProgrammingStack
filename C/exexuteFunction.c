#include<stdio.h>

#include"headerinlinefunction.h"


int main(){

	int a = 1;
	int b = 3;
	int c = inlineFunction(a,b);
	printf("Inline function addition output is %d \n",c);
	return 0;
}
