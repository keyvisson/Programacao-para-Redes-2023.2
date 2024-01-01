from random import randint
import os

def gerar_lista(quantidade, valor_minimo, valor_maximo):
    lista = []
    lista_gerada_corr = False
    for i in range(quantidade):
        lista.append(randint(valor_minimo, valor_maximo))
    if len(lista) == quantidade:
        lista_gerada_corr = True
        return (lista_gerada_corr, lista)
    else:
        lista_gerada_corr = False
        lista = None
        return (lista_gerada_corr, lista)
    
def salvar_lista(nome_lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for i in nome_lista:
            arquivo.write(str(i) + '\n')
    
