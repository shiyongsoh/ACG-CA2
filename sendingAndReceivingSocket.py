import socket
# global client_SOCK
# global server_SOCK
global variablePrinted

class Message:
    def __init__(self,ip,port,text=None):
        self.ip=ip
        self.port=port
        self.text=text

    def receive(self):
        server_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        # print("Socket Successfully created.")
        server_SOCK.bind((self.ip,self.port))
        # print("socket binded to %s" %(self.port)) 
        server_SOCK.listen(5)
        # print("socket is listening")
        while True:
            client_SOCK, clientIp= server_SOCK.accept() #address is the ip address.      
            # print('Got connection from', clientIp)
            variable = client_SOCK.recv(10000000)
            variablePrinted=variable.decode()
            return variablePrinted
        client_SOCK.close()

    def send(self):
        client_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_SOCK.connect((self.ip,self.port))
        text=self.text.encode()
        client_SOCK.send(text)
        client_SOCK.close()
        # print("socketClose")