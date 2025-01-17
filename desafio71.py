print("-- CAIXA ELETRÔNICO --")

saque = int(input("Quanto você quer sacar? "))

notas50 = saque // 50
resto = saque % 50

notas20 = resto // 20
resto = resto % 20

notas10 = resto // 10
resto = resto % 10

notas1 = resto

print(f"O valor que você quer sacar é R$ {saque},00")
print(f"Serão {notas50} notas de R$ 50,00")
print(f"Serão {notas20} notas de R$ 20,00")
print(f"Serão {notas10} notas de R$ 10,00")
print(f"Serão {notas1} notas de R$ 1,00")
