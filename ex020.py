#programa que sorteia um nome
#teste da biblioteca random função random.choice

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3,n4] #no python, uma lista fica entre []
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
