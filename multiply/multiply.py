import socket
from threading import Thread
import pickle
Host = '127.0.0.1'
Ports = [15002,15003,15004,15005,15006,15007,15008,15009,150010,15011]
prodPort = 15012
buffer = []
def main():
    
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
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        conn, addr = server_socket.accept()
        while True:
            try:
                print(f"Connected to {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                #temp = pickle.loads(data)
                buffer.append(data)
                #cords = temp[2]
                #print(temp)
                #prod = multiply(temp[0],temp[1])
                #arr = [prod, cords[0], cords[1]]
                #sendProd(arr)
            except Exception as e:
                print(f"Error: {e}")
                break  # Exit if there is an error with the client connection
        manageBuffer()

def sendProd(arr):
    prod_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    prod_socket.connect(("127.0.0.1", prodPort))
    temp = pickle.dumps(arr)
    prod_socket.send(temp)
    prod_socket.close()

def manageBuffer():
    for data in buffer:
        temp = pickle.loads(data)
        cords = temp[2]
        print(temp)
        prod = multiply(temp[0],temp[1])
        arr = [prod, cords[0], cords[1]]
        sendProd(arr)

def multiply(a1, a2):
    x = 0
    for i in range(len(a1)):
        x += a1[i] *a2[i]
    return x
 
if __name__ == "__main__":
    main()