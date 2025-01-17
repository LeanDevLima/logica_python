numeros_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
    'dezoito', 'dezenove', 'vinte'
)

num = int(input("Escolha um número inteiro de 0 a 20: "))

while num > 20 or num < 0:
    print(" O intervalo deve ser de 0 a 20")
    num = int(input("Escolha um número inteiro de 0 a 20: "))

print(f" Voce digitou {numeros_extenso[num]}." )
