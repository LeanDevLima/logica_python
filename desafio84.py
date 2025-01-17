imc = []

maior_peso = 0
nome_maior_peso = ""
menor_peso = float('inf')
nome_menor_peso = ""

while True:
    nome = input("Digite o nome: ")
    peso = int(input("Digite o peso: "))

    imc.append([nome, peso])

    if peso > maior_peso:
        maior_peso = peso
        nome_maior_peso = nome

    if peso < menor_peso:
        menor_peso = peso
        nome_menor_peso = nome

    resposta = input("Quer continuar? [S/N]: ").strip().upper()
    if resposta == 'N':
        break

print("\nAs pessoas cadastradas são:")
for pessoa in imc:
    print(f"{pessoa[0]} - {pessoa[1]} kg")

print(f"\nO menor peso é de {nome_menor_peso}: {menor_peso} kg")
print(f"O maior peso é de {nome_maior_peso}: {maior_peso} kg")
