primeiro_termo = int(input("Digite o primeiro termo da progressão: "))
razao = int(input("Digite a razão: "))
numero_termos = 9
ultimo_termo = primeiro_termo + (razao * numero_termos)  
mais_termos = 0

# for c in range(primeiro_termo, ultimo_termo + razao, razao):
#      print(c)

while primeiro_termo <= ultimo_termo:
    print(primeiro_termo)
    primeiro_termo += razao
    
    
mais_termos = int(input("Quantos mais termos vocÊ vai querer? "))

while mais_termos != 0:
    novo_ultimo_termo = primeiro_termo + (razao * mais_termos)
    while primeiro_termo < novo_ultimo_termo:
        print(primeiro_termo)
        primeiro_termo += razao
    
    
    mais_termos = int(input("Quantos mais termos você vai querer? "))




print("FIM!")
