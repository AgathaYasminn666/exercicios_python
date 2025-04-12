#programa que mostre o dobro, o triplo e a raiz quadrada

#jeito 1
n1 = int(input("Digite um número: "))
d = n1*2
t = n1*3
r = n1**(1/2)
print('O dobro de {} vale {}, o triplo vale {} e a raiz quadrada vale {}'
      .format(n1, (n1*2), (n1*3), (n1**(1/2))))

#jeito 2
n = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format (n, n*2))
print('O triplo de {} vale {} \nA raiz quadrada vale {}'
      .format (n, (n*3), (n**(1/2))))
