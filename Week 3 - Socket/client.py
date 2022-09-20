import socket

PORT = 1235
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((socket.gethostname(), PORT))

full_message = '' 
while True:
    message = s.recv(8) 
    if len(message) <= 0:
        break
    full_message += message.decode(FORMAT)

if len(full_message) > 0:
    print(full_message)