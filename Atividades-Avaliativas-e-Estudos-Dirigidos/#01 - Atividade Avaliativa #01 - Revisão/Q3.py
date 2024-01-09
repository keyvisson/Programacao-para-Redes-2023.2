import os

for arquivo in os.listdir('serie_historica_anp'):
    if os.path.isfile(arquivo):
        with open(arquivo, 'r') as f:
            lines = [line.rstrip() for line in f] 

        resultados = []
        for line in lines:
            items = line.split(',')
            tupla = (items)
            resultados.append(tupla)
        print(resultados)