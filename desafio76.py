produtos = []

qtd_produtos = int(input("Quantos produtos você deseja cadastrar? "))

for i in range(qtd_produtos):
    nome_produto = input(f"Digite o nome do {i + 1}º produto: ")
    preco_produto = float(input(f"Digite o preço do {i + 1}º produto: R$ "))
    produtos.append((nome_produto, preco_produto))

print(f"\n{'Produto':<20}{'Preço (R$)':>10}")
print('-' * 30)

for produto, preco in produtos:
    print(f"{produto:<20}{preco:>10.2f}")

print('-' * 30)