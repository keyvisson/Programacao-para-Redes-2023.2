# importar lib para gerar numeros aleatorios
from random import randint

# definindo a funcao gerar_lista
def gerar_lista(quantidade, valor_minimo, valor_maximo):
    lista = []
    for i in range(quantidade):
        lista.append(randint(valor_minimo, valor_maximo))
    if len(lista) == quantidade:
        lista_gerada_corr = True
        return True, lista
    else:
        lista_gerada_corr = False
        lista = None
        return False, lista

# definindo funcao salvar_lista
def salvar_lista(nome_lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for i in nome_lista:
            arquivo.write(str(i) + '\n')
    
