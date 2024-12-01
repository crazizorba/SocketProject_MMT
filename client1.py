import socket
HOST="127.0.0.1"
SERVER_PORT=65432
FORMAT="utf8"

def sendList(client,list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        client.recv(1024)

    msg="end"
    client.send(msg.encode(FORMAT))

def clientLogin(client):
    account=[]
    username=input('username:')
    password=input('password:')
    account.append(username)
    account.append(password)
    sendList(client,account)

LOGIN="login"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("CLIENT SIDE")

try:
    client.connect((HOST,SERVER_PORT))
    print("client address:", client.getsockname())
    
    list = ["DinhThi","20","Male"]
    msg=None
    while(msg!='quit'):
        msg=input("talk: ")
        client.sendall(msg.encode(FORMAT))
        if(msg==LOGIN):
            client.recv(1024)
            clientLogin(client)
        # msg=client.recv(1024).decode(FORMAT)
        # print("Server respunse: ",msg)
except:
    print("Error")


client.close()