lados = []

for i in range(3):
    numero = int(input(f"Informe o lado {i + 1}: "))
    lados.append(numero)

lados_ordenados = sorted(lados)

if lados_ordenados[0] + lados_ordenados[1] <= lados_ordenados[2]:
    print("Não é possível formar um triângulo.")
else:
    print("É possível formar um triêngulo.")
