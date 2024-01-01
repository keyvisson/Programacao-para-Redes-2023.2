# definir a funcao ler_arquivo
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as l:
            lista = []
            for i in l:
                lista.append(int(i.strip()))
        if not lista:
            print("A lista não é válida.")
            return False, None
        return True, lista
    except FileNotFoundError:
        print("O arquivo não foi encontrado. \
Por favor, verifique se o nome está correto ou verifique o diretório do arquivo.")
    except UnboundLocalError:
        print("O arquivo não foi encontrado. \
Por favor, verifique se o nome está correto ou verifique o diretório do arquivo.")        

#definindo funcao para para selecionar a ordenação desejada
def ordena_lista(nome_lista, metodo_ordena):
    if metodo_ordena == 'BUBBLE':
        lista = ordena_bubble(nome_lista)[1]
        return True, lista
    if metodo_ordena == 'INSERTION':
        lista = ordena_insertion(nome_lista)[1]
        return True, lista
    if metodo_ordena == 'SELECTION':
        lista = ordena_selection(nome_lista)[1]
        return True, lista
    if metodo_ordena == 'QUICK':
        lista = ordena_quick(nome_lista)
        return True, lista

# definir funcao para ordenacao bolha
def ordena_bubble(lista):
    for i in range(len(lista) - 1):
        for x in range(0, len(lista) - i - 1):
            if lista[x] > lista[x + 1]:
                lista[x], lista[x + 1] = lista[x + 1], lista[x]
    return True, lista

# definir funcao para ordenacao por insercao
def ordena_insertion(lista):
    for i in range(1, len(lista)): 
        elem = lista[i] 
        x = i-1
        while x >= 0 and elem <= lista[x]: 
            lista[x+1] = lista[x] 
            x -= 1
        lista[x+1] = elem 
    return True, lista

# definir funcao para ordenacao selecao
def ordena_selection(lista):
    for i in range(len(lista)):
        min = i
        for x in range(i + 1, len(lista)):
            if lista[x] < lista[min]:
                min = x
        (lista[i], lista[min]) = (lista[min], lista[i])
    return True, lista

# definir funcao para ordenacao quick
def ordena_quick(lista):
    if len(lista) <= 1:
        return lista
    else:
        return ordena_quick([x for x in lista[1:] if x < lista[0]]) + [lista[0]] + ordena_quick([x for x in lista[1:] if x >= lista[0]])