c = []

while len(c) < 5:
    num = int(input("Digite o valor: "))
    c.append(num)

d = list(set(c))

for i in range(1, len(d)):
    chave = d[i]
    j = i - 1

    while j >= 0 and d[j] > chave:
        d[j + 1] = d[j]
        j -= 1
    d[j + 1] = chave

print(f"A lista é: {c}")
print(f"A lista crescente sem short() é: {d}")