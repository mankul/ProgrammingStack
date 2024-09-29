import socket
import threading
import logging

def read_worker(conn, addr):
    with conn:
        print("Connected by {}".format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("data received is {}".format(data))
            conn.sendall(data)


def server_socket(host = 'localhost', port = 16000):
    thread_queue = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            logging.info("new thread launched")
            t1 = threading.Thread(target=read_worker, args=(conn, addr))
            thread_queue.append(t1)
            try:
                t1.start()
            except:
                logging.info("Thread couldn't start")
                thread_queue.remove(t1)

def main():
    server_socket()

if __name__ == "__main__":
    main()
