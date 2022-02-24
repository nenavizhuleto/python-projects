import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
HOST = "169.254.120.87"
ADDR = (HOST, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

connected = True


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - (len(send_length)))
    client.send(send_length)
    client.send(message)


while connected:
    msg = input("Type message: ")
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        connected = False
