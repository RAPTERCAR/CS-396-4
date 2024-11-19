import socket
from threading import Thread

def main():
    Host = '127.0.0.1'
    Ports = [15002,15003,15004,15005,15006,15007,15008,15009,150010,15011]
    
    for Port in Ports:
        server_thread = Thread(target=connect, args=(Host, Port))
        server_thread.start()

def connect(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected to {addr}")

def multiply(a1, a2):
    x = 0
    for i in range(len(a1)):
        x += a1[i] *a2[i]
    return x

if __name__ == "__main__":
    main()