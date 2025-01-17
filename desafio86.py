vezes = 0

lista = [[], [], [],
         [], [], [],
         [], [], []]

while vezes < 9:
    num = int(input(f"Digite o {vezes + 1}º valos da matriz: "))
    lista[vezes].append(num)
    vezes += 1

print(f"[ {lista[0]} ], [ {lista[1]} ], [ {lista[2]} ]")
print(f"[ {lista[3]} ], [ {lista[4]} ], [ {lista[5]} ]")
print(f"[ {lista[6]} ], [ {lista[7]} ], [ {lista[8]} ]")