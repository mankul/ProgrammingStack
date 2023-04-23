# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import threadingClass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


    threadList = []
    threadCounter = 0
    for i in range(5):
        thread = threadingClass.MyThread(threadCounter, "counter"+str(threadCounter))
        threadList.append(thread)
        threadCounter+=1

    for thread in threadList:
        thread.start()


    for thread in threadList:
        thread.join()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
