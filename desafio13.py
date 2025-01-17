salario = float(input("Informe o salário: R$ "))
reaj = float(input("Informe o percentual (%) de reajuste: "))

result = salario + (salario * (reaj * 0.01))

print(f"O salario R$ {salario} e com reajuste de {reaj:.0f}% resultará em R$ {result:.2f} ")
