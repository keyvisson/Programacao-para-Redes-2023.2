import os, socket
from urllib.parse import urlparse

url = input("Insira a URL da imagem: ")

#separando as partes da URL
hostImage = urlparse(url).hostname
nameImage = os.path.basename(url)
localImage = urlparse(url).path

#iniciando conexão socket
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect((hostImage, 80))

#requisição hhtp
requisição = 'GET {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(localImage, hostImage)
mySock.sendall(requisição.encode())

#variavel para salvar os dados recebidos da requisição
resposta = b''

#loop para salvar os dados recebidos da conexão até não ter mais
while True:
    dados = mySock.recv(1024)
    if not dados:
        break
    resposta += dados

#encerrar conexão socket
mySock.close()

# Salvar a imagem no mesmo diretório do programa
saveImage = open(nameImage, 'wb')
saveImage.write(resposta)
saveImage.close()

# print(nameImage)
# print(hostImage)
# print(localImage)