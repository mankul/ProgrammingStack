#include"copyConstructor.h"


CopyConstructor::CopyConstructor(const CopyConstructor & obj){
    this->id = obj.id;
    this->name = obj.name;
    this->tree = obj.tree;
}

CopyConstructor::CopyConstructor( CopyConstructor & obj){
    //  shallow copy constructor
}

CopyConstructor CopyConstructor::operator=(const CopyConstructor & obj){
    // assignment operator
    CopyConstructor A;
    A.id = obj.id;
    A.name = obj.name;
    A.tree = obj.tree;
}
CopyConstructor::operator delete(){

}

