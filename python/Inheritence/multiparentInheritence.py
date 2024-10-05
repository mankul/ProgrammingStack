
class Parent:
    pass


class Parent1(Parent):
    def __init__(self):
        super(Parent1, self).__init__()
        print("parent1")

    def func1(self):
        print("Parent1 : func1")


class Parent2(Parent):
    def __init__(self):
        super(Parent2, self).__init__()
        print("parent2")

    def func1(self):
        print("Parent2 : func1")

class Parent3:
    def __init__(self):
        super(Parent3, self).__init__()


class Parent4(Parent):
    def __init__(self):
        super(Parent4, self).__init__()
        print("parent4")


# Parent4 included. mro of Child is
# [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class '__main__.Parent3'>, <class '__main__.Parent4'>, <class '__main__.Parent'>, <class 'object'>]

# Parent4 commented, mro of Child is 
# [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class '__main__.Parent'>, <class '__main__.Parent3'>, <class 'object'>]



class Child(Parent1, Parent2, Parent3):#, Parent4):
    def __init__(self):
        super(Child, self).__init__()
        print("child")

    def func1(self):
        super().func1()



def main():
    c = Child()
    
    #c.func1()
    print(Child.mro())

if __name__ == "__main__":
    main()
