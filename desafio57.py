sexo = str(input("Digite seu sexo: ")).upper()[0].strip()

while sexo not in 'MmFf':
    print("Só é aceito [M] ou [F]")
    sexo = str(input("Digite seu sexo: ")).upper()[0].strip()

print(f"Você digitou {sexo} !")
