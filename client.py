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
            print(self.s.recv(1204).decode())

    def input_handler(self):
        while 1:
            print('send the message global for private: input g or c')
            c_g = input()
            if c_g == 'g':
                msg = input('message: ')
                h = {
                    'method': 'global',
                    'message': msg
                }
            else:
                receiver = input('Enter receiver username: ')
                msg = input('message: ')
                h = {
                'method': 'private',
                'user': self.username,
                'reciever': receiver,
                'message': msg
                }

            j = json.dumps(h)
            self.s.send((j).encode())

client = Client()
