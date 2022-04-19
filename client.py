import socket
import threading
import json

class Client:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        while 1:
            try:
                host = input('Enter host name --> ')
                port = int(input('Enter port --> '))
                self.s.connect((host,port))
                
                break
            except:
                print("Couldn't connect to server")

        self.username = input('Enter username --> ')
        self.s.send(self.username.encode())
        
        message_handler = threading.Thread(target=self.handle_messages,args=())
        message_handler.start()

        input_handler = threading.Thread(target=self.input_handler,args=())
        input_handler.start()

    def handle_messages(self):
        while 1:
            data = json.loads(self.s.recv(1204).decode())
            
            msg = str(data['msg'])
            destination = str(data['dest'])
            
            if(len(data['path']) == 1):
                print("\n" +str(data['src'])+": "+str(data['msg']))
                print("enter message --> ")
            else:
                h = {
                    'src': str(data['src']),
                    'dest': destination,
                    'msg': msg,
                    'path': data['path'][1:],
                }
                j = json.dumps(h)
                self.s.send(j.encode())
            
                

    def input_handler(self):
        while 1:
            msg = input("enter message --> ")
            dest = input("enter destination address --> ")
            h = {
                'src': self.username,
                'dest': dest,
                'msg': msg,
                'path': [],
            }
            j = json.dumps(h)
            self.s.send(j.encode())

client = Client()
