vel = float(input("Qual foi a velocidade?"))

if vel > 80:
    print(f"VocÊ foi multado. O valor da multa é R$ {((vel - 80)*7):.2f}")
else:
    print("Não foi dessa vez.")