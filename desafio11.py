larg = float(input("Informe a largura da parede: "))
alt = float(input("Informe a altura da parede: "))

area = larg * alt
tinta = area / 2

print(f"Sua parere tem uma dimensão de {larg}x{alt} e a área é de {(area):.2f} m² ")
print(f"Para pintar essa parede vocÊ precisará de {tinta} litros de tinta.")