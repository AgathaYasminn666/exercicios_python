#programa que lê um número e mostra o antecessor e sucessor dele

#jeito 1
n1 = int(input('digite um número: '))
a = n1 - 1
s = n1 +1
print('o antecessor dele é {} e o sucessor é {}'.format(a, s))


#jeito 2
n = int(input('Digite um  número: '))
print('Analisando o número {}, o antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
