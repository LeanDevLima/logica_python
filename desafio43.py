alt = float(input("Informe a sua altura (em metros): "))
pes = float(input("Informe o seu peso (em kg): "))

imc = pes / (alt ** 2)

imc_ideal_min = 18.5
imc_ideal_max = 25

peso_ideal_min = imc_ideal_min * (alt ** 2)
peso_ideal_max = imc_ideal_max * (alt ** 2)

if imc < 18.5:
    print(f"Está ABAIXO do peso ideal, IMC {imc:.2f}.")
    peso_necessario = peso_ideal_min - pes
    print(f"Você deve aumentar aproximadamente {peso_necessario:.2f} kg para atingir o peso ideal.")
elif 18.5 <= imc <= 25:
    print(f"Está no PESO IDEAL, IMC {imc:.2f}.")
elif 25 < imc <= 30:
    print(f"Você está no SOBREPESO, IMC {imc:.2f}.")
    peso_necessario = pes - peso_ideal_max
    print(f"Você deve diminuir aproximadamente {peso_necessario:.2f} kg para atingir o peso ideal.")
elif 30 < imc <= 40:
    print(f"Você está na OBESIDADE, IMC {imc:.2f}.")
    peso_necessario = pes - peso_ideal_max
    print(f"Você deve diminuir aproximadamente {peso_necessario:.2f} kg para atingir o peso ideal.")
else:
    print(f"OBESIDADE MORBIDA, IMC {imc:.2f}.")
    peso_necessario = pes - peso_ideal_max
    print(f"Você deve diminuir aproximadamente {peso_necessario:.2f} kg para atingir o peso ideal.")
