numeros = []

for i in range(3):
    numero = int(input(f"Informe o número {i + 1}: "))
    numeros.append(numero)

numeros_ordenados = sorted(numeros)

print(f"Os números informados foram: {numeros}")
print(f"Os números organizados do menor para o maior: {numeros_ordenados}")
print(f"O maior é o {numeros_ordenados[2]}")
print(f"O menor é o {numeros_ordenados[0]}")
