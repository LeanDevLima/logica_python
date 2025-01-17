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
unicos = list(set(lista))
print(f"E os valores únicos em ordem crescente são: {sorted(unicos)}")