# class A():

#     def __init__(self, value=0, name="var") :
#         print("descriptor instance initialized")
#         self.val = value
#         self.name = name

#     def __get__(self, obj, objtype):
#         print("retrieving" ,self.name)
#         # return self.val
#         return self.val
#     def __set__(self, obj, value):
#         print("setting value")
#         self.val = value
    

# class B(object):
#     a = A(50,name="cars")
#     b=10
#     def __init__(self):
#         print("B initialized")
# b = B()
# c= B()
# print(b.b)
# print(b.a)
# b.a = 20
# print(b.a)
# b.a=1100
# print(b.a)
# print(c.a)
# print(c.a)
# print(c.a)

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
	print("Instance initialized")
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        self.val = val

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5


m = MyClass()

# Getter will be called.
print(m.x) 

# setter will be called.
m.x = 25
newM = MyClass()
print(newM.x)
