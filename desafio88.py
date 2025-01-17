from random import sample

numeros = 0
vezes = 0
mega = []
resposta = ''

while True:
    numeros = sample(range(1, 61), 6)
    print(f"Esses são os números: {numeros}")
    mega.append(numeros)
    vezes += 1
    resposta = str(input("Quer continuar? Digite [S] ou [N]: "))
    if resposta in 'Nn': break

print(f"{vezes} vezes")
print(f"Esses são os números: {mega}")
print(f"Esses são os números: {mega}")
