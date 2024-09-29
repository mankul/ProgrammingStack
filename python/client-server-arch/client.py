import socket


def client_socket(host='localhost',port=16000, data="Client Socket"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(("{}".format(data)).encode())
        data=s.recv(1024)
        print(data.decode())


def main():
    data="Heylo Crispy:"
    client_socket(data=data)

if __name__ == "__main__":
    main()
