import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # host ip address
ADDR = (SERVER, PORT)  # SOCKET ADDRESS
FORMAT = 'utf-8'   # for encoding/decoding
DISCONNECT_MESSAGE = 'END'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET= IPV4, SOCK_STREAM = Which protocols is being used
server.bind(ADDR)

server.listen()
print(f"[LISTENING] server is listening")
conn, addr = server.accept()
#print("[LISTENING} server is listening")

connected = True
while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT) # msg is containing clients message
        if msg == DISCONNECT_MESSAGE:
            connected = False
            conn.send('Goodbye'.encode(FORMAT))
        else:
            count = 0
            hours = int(msg)
            if hours <= 40:
                salary = hours*200
                conn.send(f"Total salary {salary} tk".encode(FORMAT))
            else:
                extraHours = hours-40
                salary = 8000+(extraHours*300)
                conn.send(f"Total salary {salary} tk".encode(FORMAT))

conn.close()