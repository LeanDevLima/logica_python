n = str(input('Digite seu nome comoleto: ')).strip()
nome = n.split()

print ('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {(nome[0])}')
print(f'Seu ultimo nome é {(nome[len(nome)-1])}')
 