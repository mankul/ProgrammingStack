# wrap functions with functions which return functions

count = 50

def loggingWithArgument(arg1, arg2):
    print(arg1, count)
    def wrapper(func):
        print("inside wrapper")
        def wrapped_function(*args, **kargs):
            print("inside wrapped_function")
            func(*args, **kargs)
        return wrapped_function
    return wrapper

@loggingWithArgument("myfunction", count)
def function1(listOfNumbers):
    sum = 0
    for item in listOfNumbers:
        sum += item
    print("sum is ", sum)
    # return sum

# the function is converted to
# function1 = loggingWithArgument("myfunction", count)(function1(listOfNumbers)
# now the above will be written as
# function1 = loggingWithArgument.wrapper(func) , where func = function1(listOfNumbers)
# function1 = logginWithArgument.wrapper.wrapped_function(listOfNumbers)



def logging(func):
    def wrapped_logging(* args, ** kargs):
        print("wrapped function")
        newargs=[]
        # func(*args, **kargs)
        for i in range(len(args) ):
            newargs.append( args[i] + 100)
        for key, value in kargs.items():
            print(key, value)
        func(*newargs, **kargs)
    return wrapped_logging



@logging
def foo(bar, baz):
    print("bar baz is ", bar + baz)


list1 = []
for i in range(1000):
    list1.append(i)
function1(list1)
# sumOfArguments = function1(list1)
# print(sumOfArguments)


# print(foo.__name__)
# foo(29, 39)
