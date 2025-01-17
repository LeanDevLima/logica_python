from datetime import datetime

dados = {
    "nome": input("Digite o nome: "),
    "ano": int(input("Digite o ano de nascimento: ")),
    "cpts": int(input("Digite a carteira de trabalho: ")),
    "ano_contratacao": int(input("Digite o ano de contratação: ")),
    "salario": int(input("Digite o salario: "))
}

ano_atual = datetime.now().year
anos_trabalhados = ano_atual - dados["ano_contratacao"]

print(dados)
print(f"Ano atual é {ano_atual}")
print(f"Já trabalhou {anos_trabalhados} anos")
print("Já pode aposentar" if anos_trabalhados > 60 else "Não pode aposentar ainda") 
