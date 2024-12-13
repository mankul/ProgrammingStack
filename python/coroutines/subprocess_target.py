import pickle

def coroutine(func):
    def wrapper(*args, **kwargs):
        print("Wrapped function")
        f = func(*args, **kwargs)
        f.__next__()
        return f
    return wrapper

@coroutine
def send_to(f):
    try:
        while True:
            item = (yield)
            pickle.dump(item, f)
            f.flush()
    except GeneratorExit:
        print("Exiting send_to coroutine")

def recv_from(f,target):
    try:
        while True:
            data = pickle.load(f)
            target.send(data)
    except EOFError:
        target.close()
@coroutine
def print_f():
    try:
        while True:
            item = (yield)
            print(item)
    except GeneratorExit:
        print("Exiting...")

f = open("./temp.txt","wb")
print_ = print_f()
send = send_to(f)
for i in range(10):
    send.send("Hi this is Integer {}".format(i))
f.close()
f=open("./temp.txt","rb")
recv_from(f, print_)
