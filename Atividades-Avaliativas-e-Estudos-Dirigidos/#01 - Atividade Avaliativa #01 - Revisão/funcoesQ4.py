import csv

# funcao para ler o arquivo do ano escolhido pelo user
def ler_arquivo(ano):
    try:
        with open("cartola_fc_{}.csv".format(ano), "r", ) as f:
            arquivo = csv.reader(f)
            dados = [linha for linha in arquivo]
        return dados
    except FileNotFoundError:
        print("O arquivo para esse ano não foi encontrado. Por favor digite um ano válido.")
        return