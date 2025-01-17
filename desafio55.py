pesos = []

for c in range(0, 5):
    peso = float(input("Digite o pesso: "))
    pesos.append(peso)

print(f"O maior peso é o {max(pesos):.2f} kg e o menor é o {min(pesos):.2f} kg.")