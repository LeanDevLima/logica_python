salario = float(input("Informe o salário: "))

if salario >= 1250:
    print(f"Seu salario é de {salario} e com o aumento fica {salario + (salario * 0.1)}")
else:
    print(f"Seu salaio é de {salario} e com o aumento fica {salario + (salario * 0.15)}")