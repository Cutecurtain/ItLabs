import socket
import threading
import speed_controll

is_acc = False

def run():
	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.bind(("", 3000))
		server_socket.listen(5)
		while True:
			(client_socket, address) = server_socket.accept()
			new_client(client_socket)
	except IOError as e:
		from sys import stderr
		print(e, file=stderr)

def new_client(client_socket):
	def run(client_socket):
		stream = SocketStream(client_socket)
		for op in stream:
			instr[op](stream)
	client_thread = threading.Thread(target=run, args=(client_socket,))
	client_thread.run()
	return client_thread

def instr(): # Scoping
	from nav import g
	def nop(stream): pass
	def mov(stream): g.outspeedcm = stream(signed=True)
	def trn(stream): g.steering =  stream(signed=True)
	def acc(stream):
		is_acc = bool(stream()) # Just to consume a byte for now.
		if is_acc:
			acc_thread = threading.Thread(target=acc, args=())
			acc_thread.run()
	def brk(stream): pass # For eventual deinitialization, will only be called once.
	return {
		0x00: nop,
		0x01: mov,
		0x02: trn,
		0x03: acc,
		0xFF: brk
	}
instr = instr()

def acc():
	while is_acc:
		adjust_to_optimal_speed()
        sleep(0.1)


class SocketStream:
	def __init__(self, client):
		self.client = client
		self.active=True

	def __call__(self, *, size=1, signed=False, endian="big"):
		return int.from_bytes(self.client.recv(size), endian, signed=signed)

	def __next__(self):
		if not self.active: raise StopIteration
		r = self(signed=False)
		if r == 0xFF: self.active = False
		return r

	def __iter__(self):
		return self
