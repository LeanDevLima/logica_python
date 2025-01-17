dados = {
    'nomes': [],
    'idades': [],
    'sexos': []
        }

for c in range(0, 4):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ")

    dados['nomes'].append(nome)
    dados['idades'].append(idade)
    dados['sexos'].append(sexo)

idades = dados['idades']
media_idade = sum(idades) / len(idades)

print(f"A média de idades é {media_idade:.2f}.")

sexos = dados['sexos']

idades_homens = []
for i in range(len(sexos)):
    if sexos[i] == 'M':
        idades_homens.append(idades[i])

if idades_homens:  
    idade_homem_mais_velho = max(idades_homens)
    print(f"A idade do homem mais velho é: {idade_homem_mais_velho}")
else:
    None

idades_mulheres = []

for i in range(len(sexos)):
    if sexos[i] == 'M':
        idades_mulheres.append(idades[i])

if idades_mulheres: 
    idade_mulher_maisq21 =  len([idade for idade in idades_mulheres if idade < 21])
    if idade_mulher_maisq21 > 1:
        print(f"Existem {idade_mulher_maisq21} mulheres menor que 21 anos ")
    else:
        print(f"Existe {idade_mulher_maisq21} mulher menor que 21 anos. ")
else:
    None



