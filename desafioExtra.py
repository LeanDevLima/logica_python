primeiro = input("Primeiro número: ")
segundo = input("Segundo número: ")
soma = int(primeiro) + int(segundo)

print("A soma entre", primeiro, "e", segundo, "vale", soma, " normal!")
print(f"A soma entre {primeiro} e {segundo} vale {soma}, usei f-string")
print("A soma entre {} e {} vale {}, usei .format".format(primeiro, segundo, soma))



