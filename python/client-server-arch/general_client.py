import socket
import pickle
from sample import Sample

def client_socket_object(host='localhost',port=16000, data="Client Socket"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)
    print("Data is transfered")


def main():
    s = Sample("Sample Code","Challenge")
    data = pickle.dumps(s)
    client_socket_object(data=data)

if __name__ == "__main__":
    main()
