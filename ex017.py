#programa que leia um número real pelo teclado e mostre na tela sua porção inteira

#jeito 1 importando uma biblioteca
from math import trunc
num = float(input('Digte um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'
      .format(num, trunc(num)))

#jeito 2 sem biblioteca
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é de {}'
      .format(num, int(num)))
