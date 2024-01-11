import socket, threading

PORT = 7777

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', PORT))
    except:
        return print("\nA conexão com o servidor não foi possível.\n")
    
    username = input('Usuário: ')
    print('\nConectado.')

    thread_1 = threading.Thread(target=receberMensagem, args = [client])
    thread_2 = threading.Thread(target=enviarMensagem, args = [client, username])

    thread_1.start()
    thread_2.start()


def receberMensagem(client):
    while True:
        try:
            message = client.recv(2048).decode()
            print('{}'.format(message)+'\n')
        except:
            print('\nA conexão com o servidor não foi possível.\n')
            print('Pressione enter para continuar...')
            client.close()
            break


def enviarMensagem(client, username):
    while True:
        try:
            message = input('\n')
            client.send('<{}> {}'.format(username, message).encode())
        except:
            return
        

if __name__ == '__main__':
    main()