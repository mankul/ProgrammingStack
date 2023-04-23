#include<iostream>

using namespace std;


auto functionReturnInt(int item){
    return item;
}

auto functionReturnInitializerList(int item , int item1, int item2){
    auto list =  {item1, item2, item};
    return list;
}


int main(){


    auto item = 27;
    const auto citem = item;
    const auto & ritem = item;


    auto list = functionReturnInitializerList(item, citem, ritem);
    for (auto it : list){
        cout<<"item is "<<it;
    }

    return 0;
}