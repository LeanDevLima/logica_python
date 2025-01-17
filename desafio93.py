jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: ' ) )
tot = int(input(f'Quantas partidas {jogador["nome"]} joqou? '))

for c in range(0, tot):
    partidas.append(int(input(f' Quantes gels na partida {c + 1}? ' ) ) )

jogador ['gols' ] = partidas [:]
jogador['total'] = sum(partidas)
print(' -= ' * 27)
print(jogador)
print(' -= ' * 27)

for k, v in jogador.items():
    print(f'0 campo {k} tem o valor {v}')
print(' -= ' * 27)
print(f'0 jogador {jogador ["nome"]} jogou {len (jogador ["gols"]) } partidas. ')

for i, v in enumerate(jogador ['gols']):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador ["total"]} gols.')
 
