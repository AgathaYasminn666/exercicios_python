#programa que pergunte a quantidaded e km rodados por um carro alugado e quantidade de dias pelo qual ele foi alugado

input('Valor da diária: R$60,00')
input('Valor de KM rodado por dia R$0,15')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago é de R${:.2f}'.format(pago))
