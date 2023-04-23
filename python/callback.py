

def printFunction(argument, callback):
	print("print function")
	callback(argument)

def callback1(argument):
	print("callback1, ", argument)


def callback2(argument):
	print("callback2 :",argument)



printFunction("Hello ", callback1)
printFunction("World ", callback2)
