import threading
import time

threadLock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("running thread ", self.name, " with ID ", self.threadID)
        self.multiFunctions()


    def multiFunctions(self):
        threadLock.acquire()
        print("threadLock acquired for thread ", self.threadID)
        time.sleep(5)
        threadLock.release()
        print("threadLock released for thread ", self.threadID)






