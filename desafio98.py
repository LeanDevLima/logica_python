def contador(inicio, fim, passo):
    if passo == 0 or passo < 0:
        print("O passo não pode ser 0 ou negativo.")
        return

    if (inicio > fim and passo > 0) or (inicio < fim and passo < 0):
        passo = -passo

    while (inicio > fim and passo < 0) or (inicio < fim and passo > 0):
        print(inicio)
        inicio += passo

inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))

contador(inicio, fim, passo)
