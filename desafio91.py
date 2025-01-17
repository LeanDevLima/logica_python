import random

dados_resultados = {}

for i in range(1, 5):
    jogadora = "Jogadora " + str(i)
    resultado = random.randint(1, 6)
    dados_resultados[jogadora] = resultado

ordenados = sorted(dados_resultados.items(), key=lambda x: x[1], reverse=True)

print("Resultados:")
for jogadora, resultado in ordenados:
    print(jogadora, "tirou", resultado)

vencedora = ordenados[0]
print("\nA vencedora foi", vencedora[0], "com resultado", vencedora[1])
