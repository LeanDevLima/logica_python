resp = ""
cont = 0
soma = 0
lista_numeros = []

while resp != "n":
    try:
        num = int(input("Digite um número: "))
        lista_numeros.append(num)
        soma += num
        cont += 1
    except ValueError:
        print("Digite um número válido!")
        continue

    resp = input("Quer continuar? [s/n]: ").lower()
    while resp not in ['s', 'n']:
        print("Só é permitido [s] ou [n].")
        resp = input("Quer continuar? [s/n]: ").lower()

print(f"Você digitou {cont} números.")
print(f"O maior valor é o número {max(lista_numeros)}.")
print(f"O menor valor é o número {min(lista_numeros)}.")
print(f"A média dos valores é {(soma / cont):.2f}.")
