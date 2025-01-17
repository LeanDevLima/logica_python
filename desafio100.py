from random import randint

numeros = []

def sorteio():
    """
    é só pra ver se funciona
    pra ver esse comentário é só inserir help(sorteio) no fim desse código
    """
    for i in range(5):
        sorteio_lista = randint(1, 5)  
        numeros.append(sorteio_lista)

def somaPar():
    soma = 0  
    for i in numeros:
        if i % 2 == 0: 
            soma += i
    return soma

sorteio()
print(numeros)
print(f"A soma dos números pares é {somaPar()}.")