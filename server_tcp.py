import socket
import sys
Host = "192.168.29.83"
port = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


with server_socket:
    server_socket.bind((Host,port))
    server_socket.listen()
    print(f'listening on ip {Host} and ports {port}')

    
    while True:
        try:
            client_socket, address = server_socket.accept()
            
        except KeyboardInterrupt:
            print("closing the socket")
            server_socket.close()
            sys.exit()
        with client_socket:
            request = client_socket.recv(4096)
            print("received the message from client:", request.decode('utf-8'))
            message = (b'Hello client')
            client_socket.send(message)
