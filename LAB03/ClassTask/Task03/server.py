import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # host ip address
ADDR = (SERVER, PORT)  # SOCKET ADDRESS
FORMAT = 'utf-8'   # for encoding/decoding
DISCONNECT_MESSAGE = 'END'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET= IPV4, SOCK_STREAM = Which protocols is being used
server.bind(ADDR)

#server.listen()
#print("[LISTENING} server is listening")

def handle_client(conn, addr):

    print("Client connected\n")
    #conn, addr = server.accept()
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
                for char in msg:
                    if char in "aeiouAEIOU":
                        count+=1
                if count == 0:
                    conn.send("Not enough vowels".encode(FORMAT))
                elif count <= 2:
                    conn.send("Enough vowels I guess".encode(FORMAT))
                else:
                    conn.send("Too many vowels".encode(FORMAT))
    conn.close()

def start():
    #server.listen()
    server.listen()
    print(f"[LISTENING] server is listening")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Total client's connected currently:  {threading.activeCount()-1}")


start()
