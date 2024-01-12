import socket, threading, time, platform

PORT = 7777
IP = socket.gethostbyname(socket.gethostname())
DISCONNECT = '/sair'
systemInfo = '<SERVER> /hardware'

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        try:
            print('Conectando ao servidor...')
            client.connect((IP, PORT))
        except (ConnectionRefusedError):
            print("\nA conexão com o servidor não foi possível.\n")
            time.sleep(7)
            continue 
        except (OSError):
            break
    
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
            # if message == systemInfo:
            #     client.send('{}'.format(print(getHardwareInfo())).encode())
            #     break
            # if message == systemInfo:
            #     return client.send(getHardwareInfo()) 
        except:
            print('\nA conexão com o servidor não foi possível.\n')
            print('Pressione enter para continuar...')
            client.close()
            break

def enviarMensagem(client, username):
    connected = True
    while connected:
        try:
            message = input('\n> ')
            client.send('<{}> {}'.format(username, message).encode())
            if message == DISCONNECT:
                connected = False
        except:
            return
    client.close()


# def getHardwareInfo():
    # uname = platform.uname()
    # Info = 'Sistema Operacional: {} {}\n'.format(uname.system, uname.release)
    # Info += 'Nome da máquina: {}\n'.format(uname.node)
    # Info += 'Processador: {uname.processor}'.format(uname.processor)
    # return Info

if __name__ == '__main__':
    main()

# print(getHardwareInfo())