#progama que leia um ângulo qualquer e mostre na tela o valor do seno, cossenoe tangente desse ângulo

from math import radians, sin, cos, tan
ang =float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o seno {:.2f}'.format(ang, seno))
co = cos(radians(ang))
print('O ângulo de {} tem o cosseno {:.2f}'.format(ang, co))
tan = tan(radians(ang))
print('O ângulo de {} tem o tangente de {:.2f}'.format(ang, tan))
