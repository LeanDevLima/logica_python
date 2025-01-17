from datetime import date

contagem = 0

for c in range(0, 6):
    idade = int(input("Digite a idade da pessoa: "))
    if (date.today().year - idade) < 21:
        contagem += 1
    else:
        None

print(f"{contagem} pessoas não tem maioridade.")