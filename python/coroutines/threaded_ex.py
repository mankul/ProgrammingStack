import types
import queue
from threading import Thread



def coroutine(func):
    print("coroutine decoration of func {}".format(func.__name__))
    def inner(*args, **kwargs):
        # func.__next__(*args, **kwargs)
        cr = func(*args, **kwargs)
        cr.__next__()
        print("coroutine function is initialized")
        return cr
    return inner

@coroutine
def threaded_func(target):
    print("Threaded function:")
    messages = queue.Queue()
    def run_inner():
        while True:
            item = messages.get()
            if item == GeneratorExit:
                target.close()
            else:
                target.send(item)
    # def run_inner():
    #     while True:
    #         item = (yield)
    #         if item == GeneratorExit:
    #             target.close()
    #         else:
    #             target.send(item)
    Thread(target = run_inner).start()
    try:
        while True:
            item = (yield)
            messages.put(item)
    except GeneratorExit:
        messages.put(GeneratorExit)


# @types.coroutine
@coroutine
def print_fun():
    try:
        while True:
            message = (yield)
            print(message)
    except GeneratorExit:
        print("Exiting print coroutine")

message = "Hi World!"
print_ = print_fun()
main_func = threaded_func(print_)

for i in range(4):
    main_func.send(message)


