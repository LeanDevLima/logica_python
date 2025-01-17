import math
import random
import emoji

num = float(input("Digite um número: "))
nume = random.randint(1, 60)
raiz = math.sqrt(num)
raizq = math.sqrt(nume)
print(f"A raiz é {raiz}")
print(f"A outra raiz é {raizq}")
print(emoji.emojize("Olá Mundo 😉"))
print("😉")
print(f"A parte inteira dos números são {int(num)} e {int(nume)}")

