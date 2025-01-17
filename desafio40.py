nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"O valor da media é {media:.2f}, está REPROVADO.")
elif media >= 5 and media <= 6.9:
    print(f"O valor da media é {media:.2f}, está de RECUPERAÇÃO.")
else:
    print(f"O valor da media é {media:.2f}, está APROVADO.")
