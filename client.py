import socket, threading

nickname = input('Enter your nickname - ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 7976))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error')
            client.close()
            break

def write():
    while True:
        message = '{}:{}'.format(nickname, input(""))
        client.send(message.encode('utf-8'))


recive_thread = threading.Thread(target=receive)
recive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
