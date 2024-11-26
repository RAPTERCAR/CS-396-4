import socket
from threading import Thread
import pickle

def main():
    Host = '127.0.0.1'
    Ports = [15002,15003,15004,15005,15006,15007,15008,15009,150010,15011]
    connect(Host, Ports[0])
    #threads for testing purposes
    for i in range(1):
        server_thread = Thread(target=connect, args=(Host, Ports[i]))
        #threads.append(server_thread)
        server_thread.start()
    #test = [1,4,2,5]
    #test2 = [1,3,5,6]
    #x = multiply(test, test2)
    #print(x)

    

def connect(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    while True:
        conn, addr = server_socket.accept()
        while True:
            try:
                print(f"Connected to {addr}")
                data = conn.recv(1024)
                data2 = conn.recv(1024)
                row = pickle.loads(data)
                collumn = pickle.loads(data2)
                prod = str(multiply(row,collumn))
                conn.send(prod.encode('utf-8'))
                #print(array)
            except Exception as e:
                print(f"Error: {e}")
                break  # Exit if there is an error with the client connection

        

def multiply(a1, a2):
    x = 0
    for i in range(len(a1)):
        x += a1[i] *a2[i]
    return x
 
if __name__ == "__main__":
    main()