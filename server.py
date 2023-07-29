import socket, threading

host = '127.0.0.1'
port = 7976

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} go away'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print("Connection with {}".format(str(address)))
        client.send('NICKNAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print("Name {}".format(nickname))
        broadcast("{} joins".format(nickname).encode('utf-8'))
        client.send('Connected to the server'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()

