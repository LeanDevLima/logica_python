stop = int(input("Digite [999] para parar: "))
cont = 0
soma = 0

while stop != 999:
    cont += 1
    soma += stop
    stop = int(input("Digite [999] para parar: "))

print(f" A foram digitados {cont} numeros e a soma é {soma}.")

