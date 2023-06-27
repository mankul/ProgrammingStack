
def initializeKey(key):
    print("initialized new key")
    return key+10


class Memoize:
    def __init__(self, func):
        print("Memoize function initialized")
        self.memo_dictionary={}
        self.memo_dictionary[key] = initializeKey(key)


    def __call__(self, func):
        print("calling dictionary")

        def Wrapper(key):
            if(key not in self.memo_dictionary.keys()):
                self.memo_dictionary[key] = initializeKey(key)

            return self.memo_dictionary[key]

        return Wrapper
    
        
@Memoize
def getResourceManager(key):
    print("get Rersource manager")

# getResourceManager = Memoize(getResourceManager(key))
# now getResourceManager will be called and __call__ function will be invoked.



memzo = getResourceManager(10)
memzo2 = getResourceManager(20)
memzo(30)
memzo(40)
