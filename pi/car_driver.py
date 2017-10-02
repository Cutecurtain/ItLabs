import socket
import threading
from nav import g


def run():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((socket.gethostname(), 3000))
        server_socket.listen(5)

        while True:
            (client_socket, address) = server_socket.accept()
            new_client(client_socket)
    except IOError as e:
        print(e)


def new_client(client_socket):
    client_thread = threading.Thread(target=run_client, args=(client_socket,))
    client_thread.run()

def nop(args): pass
def mov(args): g.outspeedcm = int.from_bytes(args(1), "big")
def trn(args): g.steering = int.from_bytes(args(1), "big")
def acc(args): int.from_bytes(args(1), "big") # ...
def brk(args): raise StopIteration


instr = {
    0x00: nop,
    0x01: mov,
    0x02: trn,
    0x03: acc,
    0xFF: brk,
}


def run_client(client_socket):
    try:
        while True:
            instruction = int.from_bytes(client_socket.recv(1), "big")
            instr[instruction](client_socket.recv)
    except StopIteration: pass
