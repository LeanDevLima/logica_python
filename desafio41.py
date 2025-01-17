import datetime

ano_nasc = int(input("informe seu ano de nascimento: "))
ano_atual = int(datetime.datetime.today().year)
idade = ano_atual - ano_nasc

print("Sua categoria é: ")

if idade <= 9:
    print(f"MIRIM, idade {idade} anos.")
elif idade > 9 and idade <= 14:
    print(f"INFANTIL, idade {idade} anos.")
elif idade > 14 and idade <= 19: 
    print(f"JUNIOR, idade {idade} anos.")
elif idade == 20:
    print(f"SENIOR, idade {idade} anos.")
else:
    print(f"MASTER, idade {idade} anos.")




  


