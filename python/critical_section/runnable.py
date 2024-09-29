import threading
import time

db_lock = threading.Lock()

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.acct_lock = threading.Lock()

    def credit_money(self, money):
        with self.acct_lock:
            with db_lock:
                self.balance += money
                print("Balance is {}".format(self.balance))
                time.sleep(10)
    def debit_money(self, money):
        with db_lock:
            with self.acct_lock:
                self.balance -= money
                print("Balance is {}".format(self.balance))

def credit_money(acct, money):
    acct.credit_money(money)

def debit_money(acct, money):
    acct.debit_money(money)


def main():
    acct = BankAccount(1000)
    t1 = threading.Thread(target = credit_money, args = (acct, 1000))
    t2 = threading.Thread(target = debit_money, args = (acct, 2000))

    # may arise deadlock situation::. 
    # if race conditions are arised. for example between starting 2 threads if both threads take one lock because they
    # are launched simultaneously.


    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
