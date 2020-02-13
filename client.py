#!/usr/bin/env python3
import socket
import hashlib
import os
from secure import secure
from MessageManagement import MessageManagement
cmd_GET_MENU = "GET_MENU"
cmd_END_DAY = "CLOSING"
cmd_getUser = "getUsers"
menu_file = "menu.csv"
return_file = "day_end.csv"
msg = MessageManagement()


def auth():
    print('placeholder auth')
    #messageManagement.communicate("send",'hello')
    #messageManagement.communicate("receive")
def request(content):
    print("content", content)
    msg.sendMessage(content)
    result = msg.getMessage()
    return result
def respond(content,thingsToSend):
    msg.getMessage(content)
    msg.sendMessage(thingsToSend)
def userVerify():
    userClientRead = request(cmd_getUser)
    print(userClientRead)
    # with open(f"{filePath}/client/usersClient.txt","r") as userRead:
    #     userClientRead=userRead.read()

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

            #send
            msg.sendMessage(cmd_END_DAY)
            with open(f"{filePath}/client/{return_file}","r") as f:
                asdf = f.read()
            msg.sendMessage(asdf)
            #messageManagement.communicate('send',cmd_END_DAY,return_file)
            
        break


#while True:
filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
print(filePath)
userList=[]
#auth()
userVerify()
#secure = secure()
#print(secure.generating("AES","client"))