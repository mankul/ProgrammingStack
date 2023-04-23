#ifndef COPYCONSTRUCTOR
#define COPYCONSTRUCTOR

#include<string>
#include"treeStruct.h"


class CopyConstructor{
 

	public:
		int id;
		std::string name;
		TreeStruct * tree;
		


		CopyConstructor( CopyConstructor &);
		CopyConstructor(const CopyConstructor & );
		void operator delete (void * pointer);
		void operator delete [] (void * pointer);
		CopyConstructor operator= (const CopyConstructor &);

};


#endif
