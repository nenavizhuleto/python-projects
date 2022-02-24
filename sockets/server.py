from http import server
from socket import socket


import socket
import threading


HEADER = 64
PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

history = {}

def handle_client(conn, addr):
    print(f"New connection {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}]: {msg}")
            history[addr] 
    
    conn.close()

def broadcast_msg(msg):


def start():
    server.listen()
    print(f"[LISTENING]: Server is listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")


print('Server is starting...')
start()