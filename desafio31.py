dist = float(input("Informe a distancia da viagem: "))

if dist <= 200:
    print(f"O valor da passagem é R$ {(dist * 0.5):.2f}")
else:
    print(f"O valor da passagem é R$ {(dist * 0.45):.2f}")