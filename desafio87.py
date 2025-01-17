vezes = 0
soma = 0
ter_col = 0

lista = [[], [], [],
         [], [], [],
         [], [], []]

while vezes < 9:
    num = int(input(f"Digite o {vezes + 1}º valos da matriz: "))
    lista[vezes].append(num)
    vezes += 1
    if num % 2 == 0: soma += num
    if vezes == 9: ter_col = lista[2][0] + lista[5][0] + lista[8][0]

print(f"[ {lista[0]} ], [ {lista[1]} ], [ {lista[2]} ]")
print(f"[ {lista[3]} ], [ {lista[4]} ], [ {lista[5]} ]")
print(f"[ {lista[6]} ], [ {lista[7]} ], [ {lista[8]} ]")

seg_lin = max(lista[3], lista[4], lista[5])

print(f"A soma dos numeros pares digitados é {soma}.")
print(f"A soma dos valores da terceira coluna é {ter_col}.")
print(f"A o maior valor da segunda linha é {seg_lin}.")