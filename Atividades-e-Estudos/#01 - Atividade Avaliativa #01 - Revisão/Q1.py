# importar as funcoes
from funcoesQ1 import gerar_lista
from funcoesQ1 import salvar_lista

# loop para usar o try except para tratar excessoes e solicitar os argumentos da funcao
while True:
    try:
        quantidade = int(input("Digite a quantidade de números da lista: ")) 
        valor_minimo = int(input("Digite o valor mínimo da lista: "))
        valor_maximo = int(input("Digite o valor máximo da lista: "))
        if type(quantidade) == int and quantidade >= 0 and type(valor_minimo) == int and type(valor_maximo) == int:
            break
    except ValueError:
        print("Por favor, digite números inteiros sem pontos ou vírgulas. Insira os valores novamente...")

# testando funcao gerar_lista
lista = gerar_lista(quantidade, valor_minimo, valor_maximo)[1][:]
print(lista)

# testando funcao salvar_lista
salvar_lista(lista, "ListaSalva")