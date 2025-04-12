#conversor de  real em dolar

real = float(input('Quanto dinheiro você tem na carteira: '))
dolar = real / 5.87
euro = real / 6.67
print('Com R${:.2f} você pode comprar US${:.2f}\ne EUR$ {:.2f} '
       .format(real, dolar, euro))
