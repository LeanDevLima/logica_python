numero = int(input("Digite um número inteiro: "))

print("Vai converter esse número para qual sistema numérico?")

conv = int(input(" 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n Digite a opção: "))

if conv == 1:
    print(f"Em binário é {bin(numero)}")
elif conv == 2:
    print(f"Em octal é {oct(numero)}")
elif conv == 3:
    print(f"Em hexadecimal é {hex(numero)}")
else:
    print("Só podem ser números de 1 a 3, reinicie o programa.")
