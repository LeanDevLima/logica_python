num = int(input("Digite um número: "))

if num > 1:
    for c in range(2, num):
        if num % c == 0:
            print("Não é primo.")
            break       
    else:
        print("É primo!")
else:
    print("Não é primo.")
