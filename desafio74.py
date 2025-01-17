import random

lista: list[int] = []
num = 0

while len(lista) < 5:
    num = random.randint(0, 5)
    lista.append(num)

print(f"Os numeros foram {lista}")
print(f"O maior número é {max(lista)}")
print(f"O menor número é {min(lista)}")