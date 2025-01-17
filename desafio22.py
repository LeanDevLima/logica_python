

nome = str(input("Qual seu nome?")).strip()
separa = nome.split()

print(f"Analisando seu nome...")
print(f"Seu nome é {nome}")
print(f"Em letras maiúsculas ele fica {nome.upper()}")
print(f"Em letras minúsculas ele fica {nome.lower()}")
print(f"Possui {len(nome) - nome.count(' ')} letras.")

print(f"Seu primeiro nome é {separa[0]} e possui {len(separa[0])} letras.")