nome = ''
notas = [[], []]

while True:
    nome = str(input("Qual o nome do aluno? "))
    notas[0] = int(input("Informe a primeira nota: "))
    notas[1] = int(input("Informe a segunda nota: "))
    break

media = notas[0] + notas[1]
print(f"O nome é {nome} ")
print(f"A média é {media}")
print(f"E as notas são {notas}")
