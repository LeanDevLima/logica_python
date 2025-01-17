from random import randint

numeros_sorteados = {}

for i in range(6):
    sorteio = [randint(1, 6) for _ in range(6)]  
    numeros_sorteados[i] = sorteio

print("Números sorteados:")
for chave, sorteio in numeros_sorteados.items():
    maior = max(sorteio) 
    print(f"Sorteio {chave + 1}: {sorteio} e o maior número é {maior}")

