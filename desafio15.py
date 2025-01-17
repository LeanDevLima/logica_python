dias = float(input("Quantos dias alugado? "))
km = float(input("Quantos Kms rodados? "))

kmtotal = km * 0.15
diastotal = dias * 60

total = kmtotal + diastotal

print(f"O total a pagar é R$ {total:.2f}")
