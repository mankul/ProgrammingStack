#include"copyConstructor.h"


CopyConstructor::CopyConstructor(const CopyConstructor & obj){
    this->id = obj.id;
    this->name = obj.name;
    this->tree = obj.tree;
}

CopyConstructor::CopyConstructor( CopyConstructor & obj){
    //  shallow copy constructor
}

