from funcoesQ1 import gerar_lista
from funcoesQ1 import salvar_lista

while True:
    try:
        quantidade = int(input("Digite a quantidade de números da lista: "))
        valor_minimo = int(input("Digite o valor mínimo da lista: "))
        valor_maximo = int(input("Digite o valor máximo da lista: "))
        if type(quantidade) == int and type(valor_minimo) == int and type(valor_maximo) == int:
            break
    except ValueError:
        print("Por favor, digite números inteiro sem pontos ou vírgulas. Insira os valores novamente...")

print(gerar_lista(quantidade, valor_minimo, valor_maximo))

salvar_lista((gerar_lista(quantidade, valor_minimo, valor_maximo))[1], "ListaSalva")