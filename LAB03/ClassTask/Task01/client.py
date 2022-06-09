import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # host ip address
ADDR = (SERVER, PORT)  # SOCKET ADDRESS
FORMAT = 'utf-8'   # for encoding/decoding
DISCONNECT_MESSAGE = 'END'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send(f"Client's ip address is {SERVER} and Client's device name is {socket.gethostname()}")
send(DISCONNECT_MESSAGE)