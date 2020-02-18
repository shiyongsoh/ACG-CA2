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
secure = secure()
import time

#Send message to server then receive.
def request(content):
    # print("content", content)
    msg.sendMessage(content)
    result = msg.getMessage()
    return result

#Get message from the server and server sends to client.
def respond(content,thingsToSend):
    msg.getMessage(content)
    msg.sendMessage(thingsToSend)

def secureChannel(content):
    #establishing secure
    serverResponse = request(content)
    # serverResponse = interpreter(serverResponse)
    publicKey = serverResponse
    try:
        publicKey = publicKey.encode()
    except:
        pass
    time.sleep(2)  #Waits for the server to get ready
    msg.sendMessage('asdf')
    signature = msg.getMessage()
    secure.verifying(publicKey,signature)   #will quit the program if this is not verified
    if publicKey != None or '':     #if public key is not none
            publicKey = serverResponse
            sessionKey = secure.generating("AES", "client") #generates the AES key
            encryptedSessionkey=secure.encrypting("RSA",publicKey,sessionKey)
            time.sleep(3)   #Waits for the server to get ready
            msg.sendMessage(encryptedSessionkey,"") #sends the encrpyted key without encoding it again to prevent error
            content = secure.encrypting("AES",sessionKey,content)
            time.sleep(3)   #Waits for the server to get ready
            msg.sendMessage(content,'')
            test = msg.getMessage()
            # print(type(test))
            test = secure.decrypting("AES",sessionKey,test)#decrypts the response
            # print(type(test))
            return test, sessionKey
        # except:
        #     print('no send')
        #     return False

#Authentication of the user
def userVerify():
    userClientRead,key = secureChannel(cmd_getUser)
    #gets the reposne and check the authorised list of people
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
    print('userHash',userHash)
    for x in range(0, len(userList)):
        if user in userList[x][0] and userHash in userList[x][1]:
            print(userList[1][0], userList[1][1])
            #user autheticated
            print(f"\n{'-'*30}\nOKAY, sending menu over now.\n{'-'*30}\n")

            #talks to server

            menu,sessionKey = secureChannel(cmd_GET_MENU)
            print('sessionKey',sessionKey)
            print(f"\n{'='*20}\nMenu for today:\n{menu}\n{'='*20}")
            #send
            okToSendEndDay,key = secureChannel(cmd_END_DAY)
            if okToSendEndDay == "ok":
                with open(f"{filePath}/client/{return_file}","r") as f:
                    asdf = f.read()
                # print("sent", asdf)
                encryptedQuery = secure.encrypting("AES",key, asdf)
                msg.sendMessage(encryptedQuery,'')
            break


#while True:
filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
# print(filePath)
userList=[]
#auth()
userVerify()
