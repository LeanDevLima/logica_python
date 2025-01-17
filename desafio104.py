def leiaint(n):
    if n == '0123456789':
        print("Digite apenas números: ")
    else: 
        print(f"Você digitou {n}")

n = int(input("Digite um número: "))
leiaint(n)