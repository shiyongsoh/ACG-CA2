import datetime
import os
from secure import secure
from MessageManagement import MessageManagement
import time
cmd_GET_MENU = "GET_MENU"
cmd_END_DAY = "CLOSING"
default_menu = "menu_today.txt"
helloServer="hello"
default_save_base = "result-"
cmd_getUsers="getUsers"
secure=secure()
public, private = secure.generating("RSA","SERVER")
cert = secure.createCert(private,public)
print(cert)
msg = MessageManagement
msg = MessageManagement()
def request(content):
    print("content", content)
    msg.sendMessage(content)
    result = msg.getMessage()
    return result

#Get message from the server and server sends to client.
def respond(content,thingsToSend):
    msg.getMessage(content)
    msg.sendMessage(thingsToSend)

def interpreter(stringToProcess):
    #interpretes things that was send over by the server, from string to arrays
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
def secureChannel(content):
    print("this is running")
    print("public",type(public))
    publicKey=msg.sendMessage(public,'')
    asdf = msg.getMessage()
    print('asdf',asdf)
    certToSend=msg.sendMessage(cert,'')
    print("cert",type(cert))
    #msg.sendMessage(thingsToSend)
    encryptedSessionKey = msg.getMessage()
    print("encryptedSessionKey",encryptedSessionKey)
    print("encryptedSessionKey",type(encryptedSessionKey))
    print("encryptedSessionKey",encryptedSessionKey)
    decryptedSessionKey = secure.decrypting("RSA",private,encryptedSessionKey)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nasdf',decryptedSessionKey)
    print(type(decryptedSessionKey))
    
    if decryptedSessionKey != None or '':
        query = request("ok")
        #print(query.decode())
        decryptedQuery = secure.decrypting("AES",decryptedSessionKey,query)
        print("query",decryptedQuery)
        decryptedQuery = decryptedQuery.encode()
        print("query",type(decryptedQuery))
        #encryptedGiveBack = start_server(decryptedQuery)
        print("content",content)
        giveBack = secure.encrypting("AES",decryptedSessionKey,content)
        print("giveBack",giveBack)
        time.sleep(3)
        print("slept")
        print(msg.sendMessage(giveBack,''))
        #start_server()
        return content,decryptedSessionKey
    else:
        print('cannot')

def start_server(choice =None):
    print('choice',choice)
    print(type(choice))
    while True:
        print('choice',choice)
        if choice == None:
            print("choice is None")
            receivedMsg=msg.getMessage()
            print('receivemsg',receivedMsg)
        #receivedMsg=msg.communicate('receive')
        else:
            
            receivedMsg = choice.decode().upper()
            print('receivedMsg',receivedMsg)
            break
        
        if receivedMsg=="getUsers":
            with open(f'{filePath}/users.txt',"r") as f:
                userFile=f.read()
                return userFile
            #userFile.communicate("send",userFile)
            #sended = msg.sendMessage(userFile)
            #print("sended", sended)
        elif receivedMsg == "GET_MENU":
            print("get menu is running")
            with open(f'{filePath}/menu_today.txt',"r") as menu_today_server:
                menuFile=menu_today_server.read()
            #menuFile.communicate("send",menuFile)
            #sended = msg.sendMessage(menuFile)
            print("sended", menuFile)
            # return menuFile
            secureChannel(menuFile)
        elif receivedMsg=="CLOSING":
            #receivedMsg=msg.communicate("receive")
            #receivedMsg=msg.getMessage()
            closing()
            # contentToWrite = secureChannel('ok')
            # print("contentToWrite",contentToWrite)
            # contentToWrite = contentToWrite.decode()
            # with open(f"{filePath}/dayEndServer.csv","w") as dayEndServerFile:
            #     serverFile = dayEndServerFile.write(contentToWrite)
            #     print("serverFile",serverFile)
            #     serverFile = serverFile.encode()
        # elif receivedMsg == "hi":
        #     with open(f'{filePath}/menu_today.txt',"r") as menu_today_server:
        #         menuFile=menu_today_server.read()
        #     secureChannel(menuFile)
def closing():
    contentToWrite,key = secureChannel('ok')
    print('key',type(key))
    print('key',key)
    print("contentToWrite",contentToWrite)
    print("contentToWrite",type(contentToWrite))
    if contentToWrite == "ok":
        information = msg.getMessage()
        print('msg.getMessage()',information)
        contentToWrite = secure.decrypting("AES",key,information)
        print(contentToWrite)
        exit()
        with open(f"{filePath}/dayEndServer.csv","w") as dayEndServerFile:
            serverFile = dayEndServerFile.write(contentToWrite)
            print("serverFile",serverFile)
            serverFile = serverFile.encode()
filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
#print(filePath)
start_server()