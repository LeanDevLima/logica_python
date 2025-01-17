lados = []

for i in range(3):
    numero = int(input(f"Informe o lado {i + 1}: "))
    lados.append(numero)

lados_ord = sorted(lados)

if lados_ord[0] + lados_ord[1] <= lados_ord[2]:
    print("Não é possível formar um triângulo.")
else:
    print("É possível formar um triângulo.")
    if lados_ord[0] == lados_ord[1] == lados_ord[2]:
        print("TRIÂNGULO EQUILÁTERO")
    elif lados_ord[0] == lados_ord[1] or lados_ord[1] == lados_ord[2]:
        print("TRIÂNGULO ISÓSCELES")
    else:
        print("TRIÂNGULO ESCALENO")
