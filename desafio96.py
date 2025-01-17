def area(l, c):
    ar = l * c
    print("-------------------")
    print(f'A área do terreno {l}m X {c}m é de {ar}m²')
    print("-------------------")

l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))

area(l, c)