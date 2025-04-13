#teste de da biblioteca math

from math import sqrt, floor
num = int(input('Digita um número: '))
raiz = sqrt(num)
print('A raiz de {} vai ser igual a {:.2f}'.format(num, floor(raiz)))

#teste da biblioteca random

#random.randint
import random
print(random.randint(1, 20)) #dado d20

#random.random
import random
num = random.random()
print(num)
