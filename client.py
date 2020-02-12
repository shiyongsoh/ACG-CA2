#!/usr/bin/env python3

import socket

# default 
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888        # The port used by the server
cmd_GET_MENU = b"GET_MENU"
cmd_END_DAY = b"CLOSING"
menu_file = "menu.csv"
return_file = "day_end.csv"
length = 9999
#while True:

#receive
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    my_socket.connect((HOST, PORT))
    my_socket.sendall(cmd_GET_MENU )
    data = my_socket.recv(4096)
    menu_file = open(menu_file,"wb")
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
    out_file = open(return_file,"rb")
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
