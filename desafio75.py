lista: list[int] = []
num = 0

while len(lista) < 4:
    num = int(input("Digite 4 valores inteiros: "))
    lista.append(num)

print(lista)

if 3 in lista:
    print(f"O primeiro numero tres está na posição {lista.index(3)}")
else:
    print("O número tres não aparece na lista.")

if lista.count(9) > 1:
    print(f"O numero nove apareceu na lista {lista.count(9)} vezes.")
elif lista.count(9) == 1:
    print(f"O numero nove apareceu na lista {lista.count(9)} vez.")
else:
    print("O número nove não aparece na lista. ")

if (sum(1 for x in lista if x % 2 == 0)) > 1:
    print(f"Nessa lista contém {sum(1 for x in lista if x % 2 == 0)} valores pares.")
elif (sum(1 for x in lista if x % 2 == 0)) == 1:
    print("Essa lista contém 1 valor par.")
else:
    print("Não há valores pares nessa lista.")
