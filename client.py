#!/usr/bin/env python3
import socket
import hashlib
import os

def userVerify():
    # default 
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 8888        # The port used by the server
    cmd_GET_MENU = b"GET_MENU"
    cmd_END_DAY = b"CLOSING"
    cmd_getUser = b"getUsers"
    menu_file = "menu.csv"
    return_file = "day_end.csv"
    length = 9999

    #receive
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
        my_socket.connect((HOST, PORT))
        my_socket.sendall(cmd_getUser)
        data = my_socket.recv(4096)
        userClient = open(f"{filePath}/client/usersClient.txt","wb")
        userClient.write(data)
        userClient.close()
        my_socket.close()
    print('Received', repr(data))  # for debugging use
    my_socket.close()
    length += 999

    with open(f"{filePath}/client/usersClient.txt","r") as userRead:
        userClientRead=userRead.read()

    userSplitByComma=userClientRead.split(",")
    for x in range(0,len(userSplitByComma)):
        userTxtFileUserNamePasswordSeparate = userSplitByComma[x].split(":")
        userList.append(userTxtFileUserNamePasswordSeparate)

    user=input("What is your username: ")
    password=input("What is your password: ")
    encodedPassword=password.encode()
    cipher = hashlib.sha256()
    cipher.update(encodedPassword)
    userHash=cipher.hexdigest()
    print(userHash)
    print(userList)

    for x in range(0, len(userList)):
        if user in userList[x][0] and userHash in userList[x][1]:
            print("OKAY")

            #receive
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
                my_socket.connect((HOST, PORT))
                my_socket.sendall(cmd_GET_MENU )
                data = my_socket.recv(4096)
                menu_file = open(f"{filePath}/client/{menu_file}","wb")
                menu_file.write(data)
                menu_file.close()
                my_socket.close()
            print('Received', repr(data))  # for debugging use
            my_socket.close()
            length += 999

            #send
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
                print('second part of client code running')
                my_socket.connect((HOST, PORT))
                my_socket.sendall(cmd_END_DAY)
                out_file = open(f"{filePath}/client/{return_file}","rb")
                file_bytes = out_file.read(1024) 
                print('file_bytes',file_bytes)
                while file_bytes != b'':
                    my_socket.send(file_bytes)
                    file_bytes = out_file.read(1024) # read next block from file
                    print(f'sending {file_bytes}')
                out_file.close()
                my_socket.close()
            print('Sent', file_bytes)  # for debugging use
            print('Sent', repr(file_bytes))  # for debugging use
            my_socket.close()
        break


#while True:
filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
print(filePath)
userList=[]
userVerify()