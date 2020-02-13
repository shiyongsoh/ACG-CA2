import socket
port = 8888
destination = '127.0.0.1'
from FileManager import FileManager
class MessageManagement:
    def __init__(self, Encode=None,connection=True):
        self.connection = connection
        self.Encode = Encode

    def getMessage(self,timeout=None):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#kill ports
        s.bind((destination, port))
        s.listen()
        print('listening',port)
        #print("timeout",asdf)
        conn, addr = s.accept()
        with conn:
            print('Connected by ',addr)
            data = conn.recv(99999)
            print('data',data)
            try:
                print('dataDecode try is running')
                dataDecode = data.decode()
            except:
                print('dataDecode except is running')
                dataDecode = data
            conn.sendall(data)
            s.close()
        #FM = FileManager()
        #FM.writing(data)
        print(data)
        print(dataDecode)
        return dataDecode
    def sendMessage(self,message):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((destination, port))
            if message == None or "":
                message = "Null"
            #print("encode", self.Encode)
            if self.Encode == None or self.Encode:
                s.sendall(message.encode())
                print('message sent',message)
            else:
                s.sendall(message)
            #print(self.message)
            data = s.recv(99999)#this is to see what was send
            #print(repr(data))
        except:
            data = "connection Refused"
        # with FileManager("transmissionLogs.csv",data) as FileManager:
        #     FileManager.log()
        return data
    def check(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.destination, self.port))
            print("Port might be occupied, try later")
            return False
        except:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#kill ports
            s.bind((self.destination, self.port))
            print("port is available and initiated")
            s.close()
            print("Port close, check complete")        
            return True