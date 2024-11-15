import socket
host = '127.0.0.1'
genPort =15000
def main():
    choice = input("What size matrices would you like to multiply")
    client_socket = connect(host, genPort) #connect to the matrix generator
    client_socket.send(choice.encode('utf-8')) 
    matrix1 = client_socket.recv(1024).decode('utf-8')
    matrix2 = client_socket.recv(1024).decode('utf-8')
    
    
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

if __name__ == "__main__":
    main()