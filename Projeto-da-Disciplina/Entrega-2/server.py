import socket, threading

IP = socket.gethostbyname('localhost')
PORT = 7777
ADDR = (IP, PORT)
DISCONNECT = '/s'
clients = []


def main():
    print('[STARTING] Inicializando servidor...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((IP, PORT))
        server.listen()
        print('[LISTENING] Servidor está escutando em {}:{}'.format(IP, PORT))
    except:
        return print('Inicializar o servidor não foi possível.')
    
    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args= (client, addr))
        thread.start()  
        print('[ACTIVE CONNECTIONS] {}'.format(threading.active_count() - 1))

def messagesTreatment(client, addr):
    print('[NEW CONNECTION] {} connected.'.format(addr))

    connected = True
    while connected:
        try:
            message = client.recv(2048)
            if message == DISCONNECT:
                connected = False   
            broadcast(message, client)

        except:
            deleteClient(client)
            break


def broadcast(message, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(message)
            except:
                deleteClient


def deleteClient(client):
    clients.remove(client)                



if __name__ == '__main__':
    main()