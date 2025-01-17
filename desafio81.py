lista = []

print('Digite números para adicionar na lista. (S para continuar e N para parar)')

while True:
    num_input = input("Digite um número: ")
    
    if num_input.isdigit():
        num = int(num_input)
        lista.append(num)
    else:
        print("Por favor, digite um número válido.")
        continue

    escolha = input("Quer adicionar mais números? (S/N): ").strip().upper()
    
    if escolha == 'N':
        break
    elif escolha != 'S':
        print("Opção inválida! Escolha 'S' para sim ou 'N' para não.")

print(f"A lista é: {lista}")
print(f"Foram digitados {len(lista)} numeros")
lista.sort(reverse=True)
print(f"Em ordem descrescente fica {lista}")

cinco = 0

for num in lista:
    if num == 5:
        cinco += 1

if cinco > 0:
    print(f"O número 5 aparece na lista {cinco} vez(es).")
else:
    print("O número 5 não aparece na lista.")

unicos = list(set(lista))
print(f"E os valores únicos em ordem crescente são: {sorted(unicos)}")