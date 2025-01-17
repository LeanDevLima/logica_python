times = (
    'Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Internacional',
    'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Atlético-MG', 'Grêmio', 'Criciúma',
    'Bragantino', 'Juventude', 'Athletico-PR', 'Fluminense', 'EC Vitória', 
    'Corinthians', 'Cuiabá', 'Atlético-GO'
)

print(f"Os primeiros 5 colocados são {times[:5]}.\n")
print(f"Os últimos 4 colocados são {times[-4:]}.\n")
print(f"Em ordem alfabética fica: {sorted(times)}.\n")
print(f"O Corinthians está na posição {times.index('Corinthians') + 1}.\n")
