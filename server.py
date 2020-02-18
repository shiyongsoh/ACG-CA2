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
# print(cert)
msg = MessageManagement
msg = MessageManagement()

def request(content):
    #sends and expects something in return. Returns a value
    # print("content", content)
    msg.sendMessage(content)
    result = msg.getMessage()
    return result

#Get message from the server and server sends to client.
def respond(content,thingsToSend):
    #receive something and sends something back. Does not return a value
    msg.getMessage(content)
    msg.sendMessage(thingsToSend)


#-------------------utility--------------------------------#
def secureChannel(content):
    #establish an encrpyted signal, returns the symmetric key.
    #query comes in plaintext, reponse goes back in encrypted text
    # print("public",type(public))
    publicKey=msg.sendMessage(public,'')
    #this can be any message, as it is just another way for telling the server that they can continue sending
    #it is like acknowledgement from client
    asdf = msg.getMessage()
    # print('asdf',asdf)
    certToSend=msg.sendMessage(cert,'') #sends cert to client to ensure that the coming response is coming from the server.
    encryptedSessionKey = msg.getMessage()#gets session key in return
    decryptedSessionKey = secure.decrypting("RSA",private,encryptedSessionKey)#decrypts session key
    
    if decryptedSessionKey != None or '':
        #decrypts content with decrypted session key and sends back a encrpyted response
        query = request("ok")
        decryptedQuery = secure.decrypting("AES",decryptedSessionKey,query)
        # print("query",decryptedQuery)
        decryptedQuery = decryptedQuery.encode()
        # print("query",type(decryptedQuery))
        # print("content",content)
        giveBack = secure.encrypting("AES",decryptedSessionKey,content)
        # print("giveBack",giveBack)
        time.sleep(3)
        # print("slept")
        msg.sendMessage(giveBack,'')
        return content,decryptedSessionKey
    else:
        print('cannot')

def start_server(choice =None):
    #starts to listen and respond to any query send by the client
    # print('choice',choice)
    # print(type(choice))
    while True:
        # print('choice',choice)
        if choice == None:
            # print("choice is None")
            receivedMsg=msg.getMessage()
            # print('receivemsg',receivedMsg)
        else:
            #receive the query and deocode it
            receivedMsg = choice.decode().upper()
            # print('receivedMsg',receivedMsg)
            break
        #---------------------------------------------------------------reponse to query-----------------------------------------------------#
        if receivedMsg=="getUsers":
            with open(f'{filePath}/users.txt',"r") as f:
                userFile=f.read()
            secureChannel(userFile)
        elif receivedMsg == "GET_MENU":
            # print("get menu is running")
            with open(f'{filePath}/menu_today.txt',"r") as menu_today_server:
                menuFile=menu_today_server.read()
            # print("sended", menuFile)
            secureChannel(menuFile)
        elif receivedMsg=="CLOSING":
            closing()
def closing():
    contentToWrite,key = secureChannel('ok')
    if contentToWrite == "ok":
        information = msg.getMessage()
        contentToWrite = secure.decrypting("AES",key,information)
        with open(f"{filePath}/dayEndServer.csv","w+") as dayEndServerFile:
            serverFile = dayEndServerFile.write(contentToWrite)
            print(f"\n{'='*20}\n{contentToWrite}\n{'='*20}")
            print(f"serverFile is {serverFile} bytes",)
filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
#print(filePath)
start_server()