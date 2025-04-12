#cálculo da dimensão da parede e a quantidade de tinta que irá utilizar

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area/2
print('Para pintar essa parede, serão neccessários {}l de tinta'.format(tinta))
