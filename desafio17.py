from math import pow, sqrt

cat_op = pow(float(input("Informe o cateto oposto: ")), 2)
cat_adj = pow(float(input("Informe o cateto adjacente: ")), 2)

hip = cat_op + cat_adj

print(f"A hipotenusa é {sqrt(hip):.2f}")