from functools import partial



class Memoize(object):
    def __init__(self, func):
        print("initializer")
        self.func = func

    def __get__(self, obj, objtype):
        print("getter")
        return partial(self.func, serverID=1)
        if(obj is None):
            return self.func
        return partial(self, obj)

    def __call__(self, *args , **kwds):
        print("caller")
        obj = args[0]
        try:
            cache = obj._cache
        except AttributeError:
            try:
                cache = obj._cache = {}
            except AttributeError:
                print("caller function called and the variable doesnt belongs to class")
                res = self.func(*args, **kwds)
                return res

        
        key = (self.func, args[1:], frozenset(kwds.items()))
        try:
            res = cache[key]
        except KeyError:
            res = cache[key] = self.func(*args, **kwds)
        return res
        

class ResourceManager(object):
    def __init__(self) :
        print("Resource Manager object initialized")

    @Memoize
    def getResourceManager(self, serverID):
        print("get Reource Manager")
        return serverID+10


serverID = 10
rm = ResourceManager()
resourceID = rm.getResourceManager(serverID)
print(resourceID)


@Memoize
def getResources(serverID = 0):
    print("function get Resources")
    return serverID + 400


resourceID = getResources(serverID)
print(resourceID)

exit(1)

class Power(object):
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kw):
        for arg in args:
            print(arg)

class ResourceManager:

    @Power
    def decoratorFunction(age, name):
        print("decorator function")

rm = ResourceManager()
rm.decoratorFunction(10,"M")








exit(1)


class Memoize(object):
    def __init__(self, func):
        print("Memoize instance initialized")
        self.func = func
        
    # def __get__(self, obj, objtype=None):
    #     if (obj is None):
    #         return self.func
    #     else:
    #         partial(self, obj)#, age=0, name="man")

    def __call__(self, *args, **kwargs):
        print("Memoize call instance")
        try:
            obj = args[0]
        except:
            print("index out of range")
        try:
                if(obj is None):
                    self.func(args[1], args[2])
                else:
                    print("normal decorator function")
                    print(obj)
        except:
            print("arguments out of index")



def initialize():
    print("outer method")
    return 0

class ResourceManager:
    def __init__(self):
        print("resource manager class initialized")

    @Memoize
    def decoratorFunction(self, age, name):
        print("decorator function inside class")


@Memoize
def decoratorFunction(age, name):
    print("decorator function")

decoratorFunction(age=19,name="M")


# class PartialClass:
#     memo = Memoize(initialize)

#     def __init__(self):
#         print("partial function class")

#     def getPartial(self):
#         print("get partial method")
#         return self.memo


# partialFunction = PartialClass()
rm = ResourceManager()
rm.decoratorFunction(age=0,name="M")
# decoratorFunction(age=10, name="mankul")


# print(partialFunction.getPartial())

