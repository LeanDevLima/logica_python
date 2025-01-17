def linha():
    print("~" * (c + 2))

def mensagem(txt):
    linha()
    print(f" {txt} ")
    linha()

txt = str(input("Digite a mensagem: "))
c = len(txt)

mensagem(txt)