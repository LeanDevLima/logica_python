ano = int(input("Em que ano estamos? "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é um ano bissexto sim.")
else:
    print(f"O ano {ano} não é bissexto.")