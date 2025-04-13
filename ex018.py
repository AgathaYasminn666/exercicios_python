#programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, cálcule e mostre o comprimento da hipotenusa

#jeito com biblioteca
from math import hypot
co = float(input('Digite o valor do cateto opoto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))



#jeito sem biblioteca
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'. format(hi))
