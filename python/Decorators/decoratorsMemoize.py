from functools import wraps
import os

def memoize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("wrapper function")
        key = frozenset(args)
        func._cache[key] = func
        func(*args, **kwargs)
    func._cache = {}
    return wrapper


def Singleton(cls):
    cls.singleton = None
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls.singleton == None:
            cls.singleton = cls(*args, **kwargs)
        return cls.singleton
    return wrapper


class Server:
    def __init__(self, pid, serverName):
        self.pid = pid
        self.serverName = serverName


# only one server queue created on the machine. irrespective of the process and servers.
@Singleton
class ServerQueue:
    def __init__(self):
        print("server queue is initialized")
        self.queusize = 100
        self.queue={}

    def addServerToQueue(self, pid, serverName):
        print("server added to queue")
        try:
            server  = self.queue[pid]
        except AttributeError:
            server = Server(pid, serverName)
            self.queue[server] = Server
    
    def removeServerFromQueue(self, pid):
        try:
            server = self.queue[pid]
            self.queue.pop(pid)
            print("server removed from queue")
        except AttributeError:
            print("server already removed from the queue")


@memoize
def getServiceByProcessID(serverName):
    pid = os.getpid()
    print("initialize the process server name by pid")