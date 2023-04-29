from functools import wraps


def Singleton(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls.singleton == None:
            print("singleton constructor")
            cls.singleton = cls(*args, **kwargs)
            return cls.singleton
            # return cls <--- this is class returned --->
        else:
            print("Singleton already initialized")
    cls.singleton = None
    return wrapper


@Singleton
class A:
    def __init__(self):
        print("A class initialized")
    def __call__(self):
        print("call constructor of A")
        
@Singleton
class B:
    def __init__(self):
        print("class B initialized")




def main():
    a = A()
    b = B()
    print(a)
    c = A()
    print(c)
    c = a()
    print(c)
if __name__ == "__main__":
    main()
