from datetime import date

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = int(date.today().year)
idade = ano_atual - ano_nasc

if ano_nasc > ano_atual:
    print("O ano de nascimento não pode ser maior que o ano atual.")
elif idade > 18:
    print(f"Já passou o tempo de alistamento, sua idade é {idade}. Voce pasou {idade - 18} anos do prazo")
elif idade < 18:
    print(f"Ainda não é hora de se alistar, sua idade é {idade} ainda faltam {18 - idade} anos.")
elif idade == 18:
    print(f"Pode ir se alistar, sua idade é {idade}.")