import socket
import threading


HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT="utf8"

LOGIN="login"

def recieveList(conn):
    list=[]
    item=conn.recv(1024).decode(FORMAT)
    while(item!="end"):
        
        list.append(item)
        conn.sendall(item.encode(FORMAT))
        item=conn.recv(1024).decode(FORMAT)

    return list

def handleClient(conn: socket,addr):

    print("conn:",conn.getsockname())


    msg=None
    while(msg!='quit'):
        msg=conn.recv(1024).decode(FORMAT)
        print("clien ",addr,"says", msg)
        # msg=input("Serve response: ")
        conn.sendall(msg.encode(FORMAT))
        if(msg==LOGIN):
            list=recieveList(conn)
            if(is_account_valid(accounts,list)):
                print("Tai khoan hop le")
                msg="y"
                conn.sendall(msg.encode(FORMAT))
            else:
                print("Tai khoan khong hop le")
                conn.sendall(msg.encode(FORMAT))


            
    print("client",addr,"finised")
    print(conn.getsockname(),"close")
    conn.close()

def read_accounts(filename):
    accounts = {}
    
    # Mở file trong chế độ đọc
    with open(filename, 'r') as file:
        # Đọc từng dòng trong file
        for line in file:
            # Loại bỏ ký tự xuống dòng và chia dòng thành hai phần
            parts = line.strip().split()
            
            # Kiểm tra nếu có đủ hai phần (tài khoản và mật khẩu)
            if len(parts) == 2:
                tai_khoan, mat_khau = parts
                # Lưu tài khoản và mật khẩu vào dictionary
                accounts[tai_khoan] = mat_khau
                
    return accounts

def is_account_valid(accounts, account):
    # Kiểm tra tài khoản và mật khẩu
    return accounts.get(account[0]) == account[1]

filename = 'account.txt'
accounts = read_accounts(filename)







s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print("server:",HOST,SERVER_PORT)
print("Waiting for Client")

nClient=0
while(nClient<3):
    try:
        conn, addr=s.accept()

        thr=threading.Thread(target=handleClient,args=(conn,addr))
        thr.daemon=False
        thr.start()
        

    except:
        print("Error")
    nClient+=1
print("End")



conn.close()

