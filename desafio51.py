primeiro_termo = int(input("Digite o primeiro termo da progressão: "))
razao = int(input("Digite a razão: "))
numero_termos = int(input("Digite o numero de termos: "))
ultimo_termo = primeiro_termo + (razao * numero_termos)  

for c in range(primeiro_termo, ultimo_termo + razao, razao):
     print(c)

print("FIM!")
