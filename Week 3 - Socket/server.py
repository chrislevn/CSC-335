import socket
# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

PORT = 1235
SENDING_MESSAGE = "Hello, this is a message from the server"
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT))
print("Okay, I'm listening on port {PORT} \n")

print("Waiting for a connection... \n")
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint. 
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes(SENDING_MESSAGE, FORMAT))
    clientsocket.close()