preco = float(input("Qual o preco do produto? "))

opc = int(input("Qual vai ser a forma de pagamento? \n 1 - A vista: Dinheiro/ Cheque \n 2 - A vista com cartão \n 3 - Até 2x no cartão \n 4 - 3x ou mais no cartão \n Digite uma opção: "))

if opc == 1:
    print(f"Você terá 10% de desconto, preço normal R$ {preco:.2f}, preco final R$ {(preco - (preco * 0.1)):.2f}.")
elif opc == 2:
    print(f"VocÊ terá 5% de decontro, preço normal R$ {preco:.2f}, preço final R$ {(preco - (preco * 0.05)):.2f}.")
elif opc == 3:
    print(f"Você paragará o preço nomal R$ {preco:.2f}. Ficará duas parcelas de R$ {(preco / 2):.2f}.")
elif opc == 4:
    print(f"Você pagará o valor com juros, preco normal {preco:.2f} preco final R$ {(preco + (preco * 0.05))}.")
else:
    print(f"Você só pode digitar valores de 1 a 4")