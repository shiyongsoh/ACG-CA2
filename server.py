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

msg = MessageManagement()


def start_server():
    
    while True:
        receivedMsg=msg.getMessage()
        print('receivemsg',receivedMsg)
        #receivedMsg=msg.communicate('receive')
        
        # if receivedMsg == "hello":
        #     #sends public key

        if receivedMsg=="getUsers":
            with open(f'{filePath}/users.txt',"r") as f:
                userFile=f.read()
            #userFile.communicate("send",userFile)
            sended = msg.sendMessage(userFile)
            print("sended", sended)
        elif receivedMsg=="GET_MENU":
            with open(f'{filePath}/menu_today.txt',"r") as menu_today_server:
                menuFile=menu_today_server.read()
            #menuFile.communicate("send",menuFile)
            sended = msg.sendMessage(menuFile)
            print("sended", sended)
        elif receivedMsg=="CLOSING":
            #receivedMsg=msg.communicate("receive")
            receivedMsg=msg.getMessage()
            with open(f"{filePath}/dayEndServer.csv","w") as dayEndServerFile:
                dayEndServerFile.write(receivedMsg)

secure=secure()
#public, private = secure.generating("RSA","SERVER")
#cert = secure.createCert(private,public)
#print(cert)        
filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
print(filePath)
start_server()