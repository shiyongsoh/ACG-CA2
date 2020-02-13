import socket
import os
class messageManagement:
    def __init__(self):
        print('')
    def communicate(self,operateIn, thingsToSend=None,fileName=None):
        # default 
        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 8888        # The port used by the server
        mode = operateIn.upper()
        print(mode)
        length = 9999
        if mode == 'RECEIVE':
        #receive
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
                my_socket.connect((HOST, PORT))
                my_socket.sendall(b'thingsToSend')
                data = my_socket.recv(4096)
                if fileName == None:
                    try:    
                        userClient = open(f"{filePath}/client/{fileName}","wb")
                        userClient.write(data)
                        userClient.close()
                    except:
                        pass                    
                my_socket.close()
            print('Received', repr(data))  # for debugging use
            my_socket.close()
            length += 999
            return data
        #send
        elif mode == 'SEND':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
                print('second part of client code running')
                my_socket.connect((HOST, PORT))
                my_socket.sendall(b'thingsToSend')
                try:
                    out_file = open(f"{filePath}/client/{fileName}","rb")
                    file_bytes = out_file.read(1024)
                    while file_bytes != b'':
                        my_socket.send(file_bytes)
                        file_bytes = out_file.read(1024) # read next block from file
                        print(f'sending {file_bytes}')
                    out_file.close()
                except:
                    file_bytes = thingsToSend.encode()
                print('file_bytes',file_bytes)
                
                my_socket.close()
            print('Sent', file_bytes)  # for debugging use
            print('Sent', repr(file_bytes))  # for debugging use
            my_socket.close()
        else:
            print('not supported')

filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
print(filePath)
