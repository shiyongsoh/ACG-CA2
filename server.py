import datetime
import os
from secure import secure
from MessageManagement import MessageManagement

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
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\asdf',decryptedSessionKey)
    print(type(decryptedSessionKey))
    if decryptedSessionKey != None or '':
        query = request("ok")
        #print(query.decode())
        decryptedQuery = secure.decrypting("AES",decryptedSessionKey,query)
        print("query",decryptedQuery)
        print("query",type(decryptedQuery))
        encryptedGiveBack = start_server(decryptedQuery)
        giveBack = secure.encrypting(encryptedGiveBack)
        msg.sendMessage(giveBack)
    else:
        print('cannot')
def start_server(choice =None):
    
    while True:
        if choice == None:
            receivedMsg=msg.getMessage()
            print('receivemsg',receivedMsg)
        #receivedMsg=msg.communicate('receive')
        else:
            receivedMsg = choice
        if receivedMsg == "hi":
            with open(f'{filePath}/menu_today.txt',"r") as menu_today_server:
                menuFile=menu_today_server.read()
            secureChannel(menuFile)

        if receivedMsg=="getUsers":
            with open(f'{filePath}/users.txt',"r") as f:
                userFile=f.read()
                return userFile
            #userFile.communicate("send",userFile)
            #sended = msg.sendMessage(userFile)
            #print("sended", sended)
        elif receivedMsg=="GET_MENU":
            with open(f'{filePath}/menu_today.txt',"r") as menu_today_server:
                menuFile=menu_today_server.read()
            #menuFile.communicate("send",menuFile)
            #sended = msg.sendMessage(menuFile)
            #print("sended", sended)
            return menuFile
        elif receivedMsg=="CLOSING":
            #receivedMsg=msg.communicate("receive")
            receivedMsg=msg.getMessage()
            with open(f"{filePath}/dayEndServer.csv","w") as dayEndServerFile:
                dayEndServerFile.write(receivedMsg)
filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
#print(filePath)
start_server()