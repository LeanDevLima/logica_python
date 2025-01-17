from random import choice, randint

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
nome4 = input("Digite o quarto nome: ")

nomes_hash = {
    'nome1': nome1,
    'nome2': nome2,
    'nome3': nome3,
    'nome4': nome4
}
n = randint(1, 4)

print(nomes_hash[f'nome{n}'])

lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print(escolhido)
