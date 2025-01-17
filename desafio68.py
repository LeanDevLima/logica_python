import random

vitoria = True  
cont = 0

while vitoria:
    valor = int(input("Digite um valor: "))
    escolha = str(input("Par ou Impar? DIGITE [P] OU [I]: ").upper())
    
    numero = random.randint(1, 2)
    soma = numero + valor
    cont += 1
    
    if soma % 2 == 0 and escolha == 'P':
        print(f"Você escolheu {valor} e o computador escolheu {numero}. A soma é {soma}!")
        print("Parabéns, você ganhou! Vamos jogar novamente.")
    elif soma % 2 != 0 and escolha == 'I':
        print(f"Você escolheu {valor} e o computador escolheu {numero}. A soma é {soma}!")
        print("Parabéns, você ganhou! Vamos jogar novamente.")
    else:
        print(f"Você escolheu {valor} e o computador escolheu {numero}. A soma é {soma}!")
        print("Não foi dessa vez - GAME OVER!")
        cont += -1
        print(f"Você venceu {cont} vezes")
        vitoria = False
