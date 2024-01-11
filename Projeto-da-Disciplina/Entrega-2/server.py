import socket, threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 7777
ADDR = (IP, PORT)
DISCONNECT = '!s'
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

    while True:
        try:
            message = client.recv(2048)
            broadcast(message, client)
            print('[{}] {}'.format(addr, message))

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
    print('[ACTIVE CONNECTIONS] {}'.format(threading.active_count() - 2))

if __name__ == '__main__':
    main()