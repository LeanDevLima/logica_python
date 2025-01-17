from datetime import datetime

ano_atual = datetime.now().year

def voto(ano):
    idade = ano_atual - ano
    if idade >= 65: print(f"VOTO OPCIONAL: sua idade é {idade}.")
    else: print(f"VOTO OBRIGATORIO: sua idade é {idade}.")

ano = int(input("Informe seu ano de nascimento: "))
voto(ano)