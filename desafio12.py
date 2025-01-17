preco = float(input("Informe o valor do produto: "))
desc = float(input("Informe o percentual (%) de desconto: "))

result = preco - (preco * (desc * 0.01))

print(f"O produto custa {preco} e com desconto de {desc:.0f}% custará R$ {result:.2f} ")
