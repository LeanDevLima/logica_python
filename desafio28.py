import random

num = random.randint(1, 5)
numero = int(input("Digite um número: "))

if numero == num:
    print("Você acertou, Parabéns")
else:
    print(f"Era {num} tente denovo. ")