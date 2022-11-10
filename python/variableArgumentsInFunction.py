

def multipleArgs(*args, **kargs):
    for arg in args:
        print("Argument ", arg)
    for key, arg in kargs.items():
        print("key:",key, " ,Argument:",arg)


seperate=1
multipleArgs("Hi","Hello",["find","truth",1], seperate, bar="fantastic", seperate=seperate)