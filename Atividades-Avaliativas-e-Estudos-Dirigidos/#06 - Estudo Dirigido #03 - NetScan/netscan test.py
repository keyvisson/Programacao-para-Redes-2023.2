import os, socket

#pegar a url do host e transformar em IP
host = input('Qual o host que deseja verificar? ')
ip_host = socket.gethostbyname(host)

#funcao para criar uma lista com os dados do arquivo
def criar_lista(nome_arquivo):
    local = os.path.dirname(os.path.abspath(nome_arquivo))
    arquivo = open(local + '/tabela-protocolos.csv', 'r', encoding='utf-8')
    arquivo = arquivo.read()
    lista_arquivo = arquivo.split('\n')
    lista_arquivo.remove('')
    return lista_arquivo

lista_arquivo = criar_lista('tabela-protocolos.csv')

print(lista_arquivo)

#loop para separar os itens da lista removendo o ; para separar os itens e cada linha será uma lista
for s in lista_arquivo:
    item = s.split(';')
    porta = item[0].strip('\ufeff')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  
    estado_porta = sock.connect_ex(('{}'.format(ip_host),int(porta)))
    if estado_porta == 0:
        print ("Porta: {} Estado: Aberta".format(porta))
    else:
        print ("Porta: {} Estado: Fechada".format(porta))
    sock.close()

    