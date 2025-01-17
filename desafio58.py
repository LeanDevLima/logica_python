import random

num = random.randint(0, 10)
numero = int(input("Digite um número de 0 a 10: "))
tentativa = 1

while num != numero:
        tentativa += 1
        if num > numero:
            print("É um numero maior, tente denovo: ")
            numero = int(input("Digite um número de 0 a 10: "))
        elif num < numero:
            print("É um numero menor, tente denovo: ")
            numero = int(input("Digite um número de 0 a 10: "))

print(f"Você acertou, Parabéns e usou {tentativa} tentativa(s)")
