#ex. de como pular espaços
nome = input ('qual o seu nome? ')
print ('Prazer em te conhecer {:^20}!'.format(nome))

#calculadora de operadores aritméticos
n1 = int(input('um valor '))
n2 = int(input('outro valor '))
s = n1+n2
su = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print ('a soma vale {},  a subtração  vale {}, o produto é {}, a divisão é {} '
       .format(s, su,m, d))
print('a divisão inteira é {}, e potência é {} '
      .format(di, e))
