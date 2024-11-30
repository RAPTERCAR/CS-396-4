import socket
from threading import Thread
import pickle

host = '0.0.0.0'
port = 15012
matrixHold = []
size = 1
flag = False
def main():
    connect()
    buildMatrix()
    #print("\n".join([" ".join(map(str, row)) for row in final]))
    


def connect():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    while True:
        if (flag == True):
            break
        conn, addr = server_socket.accept()
        while True:
            try:
                print(f"Connected to {addr}")
                data = conn.recv(1024)
                data2 = pickle.loads(data)
                addInfo(data2)
                break
                
            except Exception as e:
                print(f"Error: {e}")
                break  # Exit if there is an error with the client connection
    server_socket.close()

def addInfo(array):
    global size
    arr = array
    #print(arr)
    matrixHold.append(arr)
    if (arr[1] >= size or arr[2] >= size):
        size += 1
    #if(arr[2] > size):
    #    size = arr[2]
    eval(arr)

def buildMatrix():
    aggArray = [[0]*size for _ in range(size)]
    print(size)
    for i in matrixHold:
        print(i)
        aggArray[i[1]][i[2]] = i[0]
    #print("\n".join([" ".join(map(str, row)) for row in aggArray]))
    result = ''
    for row in aggArray:
        result += " ".join(map(str, row)) + "\n"
    result.strip()
    print(result)



def eval(array):
    global size
    global flag
    if (array[1] > 0):
        if ((size - 1) == array[1] and array[1] == array[2]):
            flag = True
            
if __name__ == "__main__":
    main()