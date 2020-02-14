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

def interpreter(stringToProcess):
    #interpretes things that was send over by the server, from string to arrays
    print("stringToProcess",stringToProcess)
    result = []
    allList = []
    titleNsubtitle = stringToProcess.split("\n")
    for x in range(0,len(titleNsubtitle)):
        individual = titleNsubtitle[x].split(",")
        result.append(individual)
    return result
def arrayToString(content):
    #converts array to string
    for x in content:
        processedContent = "".join(str(content))
    return processedContent

#-------------------utility--------------------------------#


def auth():
    print('placeholder auth')
    #messageManagement.communicate("send",'hello')
    #messageManagement.communicate("receive")

#Send message to server then receive.
def request(content):
    print("content", content)
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
    print('server Response',serverResponse)
    publicKey = serverResponse
    publicKey = publicKey.encode()
    time.sleep(2)
    msg.sendMessage('asdf')
    signature = msg.getMessage()
    secure.verifying(publicKey,signature)
    if publicKey != None or '':
            publicKey = serverResponse
            sessionKey = secure.generating("AES", "client")
            encryptedSessionkey=secure.encrypting("RSA",publicKey,sessionKey)
            time.sleep(3)
            msg.sendMessage(encryptedSessionkey,"")
            content = secure.encrypting("AES",sessionKey,content)
            time.sleep(3)
            msg.sendMessage(content,'')
            test = msg.getMessage()
            test = secure.decrypting("AES",sessionKey,test)
            return test, sessionKey
        # except:
        #     print('no send')
        #     return False
#Authentication of the user
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

            # menuItem=msg.sendMessage(cmd_GET_MENU)
            menuItem=request(cmd_GET_MENU)
            with open(f'{filePath}/client/{menu_file}','w') as clientMenu:
                clientMenu.write(menuItem)

            with open(f'{filePath}/client/{menu_file}','r') as clientMenu:
                clientMenuContents=clientMenu.read()
                print(clientMenuContents)

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
#userVerify()
print(secureChannel(cmd_GET_MENU))
okToSendEndDay,key = secureChannel(cmd_END_DAY)
if okToSendEndDay == "ok":
    with open(f"{filePath}/client/{return_file}","r") as f:
        asdf = f.read()
    encryptedQuery = secure.encrypting("AES",key, asdf)
    msg.sendMessage(encryptedQuery,'')
#secure = secure()
#print(secure.generating("AES","client"))