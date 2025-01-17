dados = {}
resposta = 's'
contador = 1

while resposta != 'n':
    produto = str(input("Digite o produto: "))
    preco = float(input("Digite o preço R$: "))


    dados[f'produto_{contador}'] = {'nome': produto, 'preco': preco}
    contador += 1

    resposta = str(input("Quer continuar? [s] [n] ").lower())


soma_total = 0
produto_mais_caro = ''
preco_mais_caro = 0

for valor in dados.values():
    soma_total += valor['preco']
    if valor['preco'] > preco_mais_caro:
        preco_mais_caro = valor['preco']
        produto_mais_caro = valor['nome']

print("\nDados armazenados:")
for chave, valor in dados.items():
    print(f"{chave}: Nome: {valor['nome']}, Preço: R$ {valor['preco']}")

print(f"\nSoma total dos produtos: R$ {soma_total:.2f}")
print(f"Produto mais caro: {produto_mais_caro} (R$ {preco_mais_caro:.2f})")
