valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = float(input("Vai pagar em quantos anos? "))
prestacao = valor_casa / (anos * 12) 
validacao = (salario / 100) * 30 


if prestacao < validacao:
    print(f"Empréstimo aprovado! A prestação será de R$ {prestacao:.2f} e 30% do salário é R$ {validacao:.2f}")
else:
    print(f"Empréstimo negado! Prestação R$ {prestacao:.2f} e 30% do salario é R$ {validacao:.2f}")


 
