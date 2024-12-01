import socket
import random
from threading import Thread, Lock
import pickle
import sys
import time


host = 'multiply'
#host = '127.0.0.1'
multPorts = [15002,15003,15004,15005,15006,15007,15008,15009,150010,15011]
mutex = Lock()
mutex2 = Lock()
threads = []

# holds aggregate array as well as the next row and collumn to multiply
class Tracker:

    def __init__(self, size):
        self.r = 0
        self.c = 0
        self.size = size
        self.done = 0 
        self.aggArray = [[0]*size for _ in range(size)]

    def increment(self,):
        x = [self.c,self.r]
        if(self.c == self.size -1 and self.r == self.size -1):
            self.done = 1
        elif(self.c == self.size - 1):
            self.c = 0
            self.r += 1
        else:
            self.c += 1
        #print(x)
        return x
    
    def place(self, prod, row, collumn):
        self.aggArray[row][collumn] = prod

    def getArr(self):
        return self.aggArray

    
def main():
    #if len(sys.argv) < 2:
        #print("Please provide the matrix size as a command-line argument.")
        #sys.exit(1)
    choice = 3
    #choice = int(input("What size matrices would you like to multiply: "))
    #client_socket = connect(host, genPort) #connect to the matrix generator
    #client_socket.send(choice.encode('utf-8')) 
    matrix1 = generateMatrix(choice)
    matrix2 = generateMatrix(choice)
    track = Tracker(choice)
    print("\n".join([" ".join(map(str, row)) for row in matrix1]))
    print("\n")
    print("\n".join([" ".join(map(str, row)) for row in matrix2]))
    print(matrix1[0])
    #arr = getCollumn(matrix1,0,choice)
    #print(arr)
    for i in range(1):
        server_thread = Thread(target=connect, args=(host, multPorts[i],matrix1,matrix2,track))
        threads.append(server_thread)
        server_thread.start()

    #for thread in threads:
    #    thread.join()

    #client_socket = connect(host,multPorts[0])
    #data = pickle.dumps(matrix1[0]) #changes array to a form that can be sent over sockets
    #client_socket.send(data)

    
    

def connect(host, port, m1, m2, tracker):
    retries = 10
    while retries > 0:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")
            while tracker.done == 0:
                mutex.acquire()
                x = tracker.increment()
                mutex.release()
                hold = [m1[x[0]], getCollumn(m2, x[1]), x]
                #print(hold)
                hold2 = pickle.dumps(hold)
                client_socket.sendall(hold2)
            return
        except (ConnectionRefusedError, socket.error):
            print(f"Connection failed to {host}:{port}. Retrying...")
            retries -= 1
            time.sleep(5)  # Wait 5 seconds before retrying
    print(f"Failed to connect to server at {host}:{port} after retries.")


def generateMatrix(size):
    matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] =random.randint(0, 9)
    return matrix
#gets collumn of matrix
def getCollumn(matrix,collumn):
    arr = [0] * len(matrix[0]) 
    for i in range(len(matrix[0])):
        arr[i] = matrix[i][collumn]
    return arr



if __name__ == "__main__":
    main()