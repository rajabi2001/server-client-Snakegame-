import socket, json


class Network:

    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def start(self):
        self.s.connect((self.host , self.port))
        
        f = open("config.json" , "w")
        f.write(json.dumps(self.s.recv(1024).decode('ascii')))
        f.close()   

        

    def send_data(self, keys):
        pass

    def get_data(self):
        pass
