num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
opc = 0

while opc != 5:
    opc = int(input("O que quer fazer com esses números? \n [ 1 ] - SOMAR \n [ 2 ] - MULTIPLICAR \n [ 3 ] - MAIOR \n [ 4 ] - NOVOS NUMEROS \n [ 5 ] - SAIR \n DIGITE A OPÇÃO:  "))

    if opc == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opc == 2:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif opc == 3:
        if num1 > num2:
            print(f"{num1} é MAIOR QUE (>) {num2}")
        else:
            print(f"{num2} é MAIOR QUE (>) {num1}")
    elif opc == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    elif opc == 5:
        print("Obrigado por usar o programa!")
    else:
        print("Opção inválida, tente novamente.")
    