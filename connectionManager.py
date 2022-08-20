#sockets
import socket
import threading
import time
#connection manager for p2p network
class ConnectionManager:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.connections = []
        self.threads = []
        self.threads.append(threading.Thread(target=self.listen))
        self.threads.append(threading.Thread(target=self.broadcast))
        for thread in self.threads:
            thread.start()
        self.threads.append(threading.Thread(target=self.check_connections))
        for thread in self.threads:
            thread.start()
    def listen(self):
        while True:
            conn, addr = self.sock.accept()
            self.connections.append(conn)
            print("New connection from: " + str(addr))
    def broadcast(self):
        while True:
            for conn in self.connections:
                conn.send(bytes("Hello", "utf-8"))
                time.sleep(1)
    def check_connections(self):
        while True:
            for conn in self.connections:
                try:
                    data = conn.recv(1024)
                    print(data)
                except:
                    self.connections.remove(conn)
                    conn.close()
                    print("Connection closed")
                    break
    cm = ConnectionManager("localhost", 9999)
    cm.sock.close()
    print("Server closed")
#sockets


