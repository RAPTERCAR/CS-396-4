import socket
import random
from threading import Thread
import pickle

host = '127.0.0.1'
multPorts = [15002,15003,15004,15005,15006,15007,15008,15009,150010,15011]
class Conn: #not sure whether to handle socketes as a class instance or through threads

    def __init__(self,) -> None:
        pass
    
def main():
    choice = int(input("What size matrices would you like to multiply: "))
    #client_socket = connect(host, genPort) #connect to the matrix generator
    #client_socket.send(choice.encode('utf-8')) 
    matrix1 = generateMatrix(choice)
    matrix2 = generateMatrix(choice)
    print("\n".join([" ".join(map(str, row)) for row in matrix1]))
    print("\n")
    print("\n".join([" ".join(map(str, row)) for row in matrix2]))
    arr = getCollumn(matrix1,0,choice)
    print(arr)

    #client_socket = connect(host,multPorts[0])
    #data = pickle.dumps(matrix1[0]) #changes array to a form that can be sent over sockets
    #client_socket.send(data)
    
    
def connect(host, port):
    try:
        # Attempt to create a socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        return client_socket  # Return the connected socket
    except (ConnectionRefusedError, socket.error):
        # If connection fails, print error and try the next server
        print(f"Server {host}:{port} unavailable. Trying next server...")

def generateMatrix(size):
    matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] =random.randint(0, 9)
    return matrix
#gets collumn of matrix
def getCollumn(matrix,collumn, size):
    arr = [0] * size 
    for i in range(size):
        arr[i] = matrix[i][collumn]
    return arr



if __name__ == "__main__":
    main()