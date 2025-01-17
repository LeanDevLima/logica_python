vezes = 0

lista = [[], []]

while vezes < 7:
    num = int(input(f"Digite o {vezes + 1}º número: "))
    if num % 2 == 0: lista[0].append(num)
    else: lista[1].append(num)
    vezes += 1

lista[0].sort()
lista[1].sort()

print(f"A lista dos pares é {lista[0]}.")
print(f"A lista dos ímpares é {lista[1]}.")
print(lista)