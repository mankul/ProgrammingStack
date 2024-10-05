
from abc import ABC, abstractmethod

class Parent(ABC):
    def __init__(self):
        print("parent")

    def func1(self):
        print("parent func1")


    @abstractmethod
    def func2(self):
        print("abstract method")


    @abstractmethod
    def func3(self):
        pass

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("child")

    def func1(self):
        super().func1()
        print("child func1")
    def func2(self):
        print("func2")

    def func3(self):
        print("func3")

def main():
    c = Child()
    c.func1()
    c.func2()
    c.func3()
if __name__ == "__main__":
    main()
