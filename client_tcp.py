import socket

Host = "192.168.29.83"
port = 5555

client_sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with client_sockets:
    try: 
        client_sockets.connect((Host,port))
        message = (b"Hi Server")
        print("sending:",message.decode('utf-8'))
        client_sockets.send(message)
        response = client_sockets.recv(4096)
        print("received msg:", response.decode('utf-8'))  
    except Exception as e:
        print(e)
