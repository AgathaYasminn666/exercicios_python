#conversor de temperaturas

c = float (input('Informe a temperatura em °C: '))
f = ((9*c)/5)+32 #não há necessidade de colocar os ()
print('A temperatura de {}°C corresponde a {}°F'
      .format(c,f))
