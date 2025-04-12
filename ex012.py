#programa que calcule o preço com 5% de desconto
#esse cálculo serve para qualquer conta com porcentagem

preço = float(input('Qua é o preço do produto? R$'))
novo = preço - (preço * 5/100) #preço = -5%
print ('O produto ques custava {:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'
       .format (preço, novo))
