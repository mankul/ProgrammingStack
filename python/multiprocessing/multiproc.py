import multiprocessing
import time


def worker(count):
    print("new proc {}".format(count))
    time.sleep(count)
    print("Returning worker process {}".format(count))


def main():
    multiproc_count = int(input())
    process_q = [] 
    for count in range(multiproc_count):
        try:
            proc = multiprocessing.Process(target = worker, args=(count,))
            process_q.append(proc)
            proc.start()
        except Exception as e:
            print("Error is ",e)
            raise e
    
    for proc in process_q:
        proc.join()

    print("All processes finished")
if __name__ == "__main__":
	main()
