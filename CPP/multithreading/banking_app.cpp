#include<iostream>
#include<mutex>
#include<thread>
#include<vector>

using namespace std;

mutex bank_balance;

bool debitMoney(int & balance, int deduction, int minBalance){   
	if(balance < minBalance){
        return false;    
	}
    else{
        balance -= deduction;
    }
    return true;
}

bool creditMoney(int & balance, int incr){
    balance += incr;
    return true;
}

// multi threading
int main(){
    int balance = 500;
    vector<thread> all_threads;
    vector<int> transactions = {3000,-1000,10000,-15000};
    bool res;
    for(auto iter : transactions){
        thread t;
	// by default copy constructor is not allowed for threads. This is by design. Use move.
        //all_threads.push_back(t);
        all_threads.push_back(std::move(t));
        std::cout<<"Current Balance is "<<balance<<std::endl;
        if (iter <= 0){
            std::cout<<"Debiting money "<<-iter<<std::endl;
            res = debitMoney(balance, -1 * (iter), 0);
        }
        else{
            std::cout<<"Crediting Money "<<iter<<std::endl;
            res = creditMoney(balance, iter);
        }
        if(res == false)
            exit(1);
    }
    for(const thread &  t: all_threads){
        t.join();
    }
    return 0;
}


/*
// linear process.
int main(){
    int balance = 500;
    vector<thread> all_threads;
    vector<int> transactions = {3000,-1000,10000,-15000};
    bool res;
    for(auto iter : transactions){
        std::cout<<"Current Balance is "<<balance<<std::endl;
        if (iter <= 0){
            std::cout<<"Debiting money "<<-iter<<std::endl;
            res = debitMoney(balance, -1 * (iter), 0);
        }
        else{
            std::cout<<"Crediting Money "<<iter<<std::endl;
            res = creditMoney(balance, iter);
        }
        if(res == false)
            exit(1);
    }
	return 0;
}
*/
