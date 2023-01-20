import socket
import threading

from pickle import dump as pickle_dump, load as pickle_load


# UDP SOCKET
class Server:
    def __init__(self):
        self.port = 2304
        self.host_ip_address = socket.gethostbyname(socket.gethostname())
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.max_data_size = 2048

        self.players = []

        try: socket.bind((host_ip_address, port))
        except: print(str(socket.error))

        socket.listen(2)


s = Server()