numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = numero 

print(f"Calculando o fatorial de {numero}:")

while numero > 0:
    print(f"{fatorial} * {numero}") 
    fatorial *= numero
    numero -= 1

print(f"O fatorial é: {fatorial}")
