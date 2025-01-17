valor = 0

while valor >= 0:
    valor = int(input("Quer a tabuada de qual valor? "))
    num = 0
    if valor < 0: break

    while num < 10:
        num+= 1
        print(f"{valor} x {num} = {num * valor}")
        


