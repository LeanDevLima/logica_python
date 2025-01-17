primeiro = float(input("Digite o primeiro número: "))
segundo = float(input("Digite o segundo número: "))

if primeiro > segundo:
    print(f" O 1º numero {primeiro} é maior que o 2º {segundo}.")
elif segundo > primeiro:
    print(f"O 2º numero {segundo} é maior que o 1º {primeiro}.")
elif segundo == primeiro:
    print(f"Esses números são iguais {primeiro} e {segundo}")
else:
    print("Digite apenas números.")

