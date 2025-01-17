from math import radians, sin, cos, tan

angulo = float (input ('Digite o ângulo que você deseja: '))
seno = sin(radians (angulo))
print('0 ângulo de {} tem o SENO de {:.2f}'. format(angulo, seno))
cosseno = cos (radians (angulo))
print('0 ângulo de {} tem o COSSENQ de {:.2f}' . format(angulo, cosseno))
tangente = tan(radians (angulo) )
print('0 ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))


