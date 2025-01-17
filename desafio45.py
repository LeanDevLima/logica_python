import random

print("PEDRA PAPEL E TESOURA")
print("+++++++++++++++++++++")

esc = int(input("\n 1 - PEDRA \n 2 - PAPEL \n 3 - TESOURA \n OPÇÃO: "))

pc = random.randint(1, 3)

print(f"Sua escolha foi {esc}")
print(f"O computador estolheu {pc}")

if pc == 1 and esc == 1:
    print("Empatou, os dois escolheram PEDRA.")
elif pc == 1 and esc == 2:
    print("Parabéns, você ganhou, PAPEL ganha da PEDRA.")
elif pc == 1 and esc == 3:
    print("Você perdeu, PEDRA ganha da TESOURA.")
elif pc == 2 and esc == 1:
    print("Você perdeu, PAPEL ganha da PEDRA.")
elif pc == 2 and esc == 2:
    print("Empatou, ambos escolheram PAPEL.")
elif pc == 2 and esc == 3:
    print("Parabéns, você ganhou, TESOURA ganha do PAPEL.")
elif pc == 3 and esc == 1:
    print("Parabéns, você ganhou, PEDRA ganha da TESOURA.")
elif pc == 3 and esc == 2:
    print("VocÊ perdeu, TESOURA ganha do PAPEL.") 
elif pc == 3 and esc == 3:
    print("Empatou, ambos escolheram TESOURA")
else:
    print(" Escolha opções de 1 a 3 !!! ")