c = []

while len(c) < 5:
    num = int(input("Digite o valor: "))
    c.append(num)

print(f"A lista é {c}")
print(f"O valor máximo é {max(c)}")
print(f"O valor mínimo é {min(c)}")
x = 0

for i in (c):
    print(f"Na posição {x} temos {c[x]}")
    x += 1
