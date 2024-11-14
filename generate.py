import socket
from threading import Thread
import random
import os

def main():
    Host = '127.0.0.1'
    Ports = [15000,15001]

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
        size = conn.recv(1024).decode('utf-8')
        matrix = generateMatrix(size)
        conn.send(matrix.encode('utf-8'))
        conn.close()

def generateMatrix(size):
    matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] =random.randint(0, 9)
    return matrix
if __name__ == "__main__":
    main()