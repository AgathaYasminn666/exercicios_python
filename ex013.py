#programa que leia o salário de um funcionário com 15% de aumento
#esse programa serve para qualquer porcentagem

#exemplo 1
salario = float(input('Qual o salário atual do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que recebia {:.2f},com 15% de aumento, ele passará a receber R${:.2f}'
      .format(salario, novo))

#exemplo 2
preço = float(input('Qual o valor do produto? R$'))
novo = preço - (preço * 8 / 100)
print('O produto de R${:.2f}, com 8% de desconto ficará R${:.2f}'.format(preço, novo))
