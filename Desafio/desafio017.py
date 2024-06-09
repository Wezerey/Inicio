import math
co=float(input('Coloque o valor do cateto o: '))
ca=float(input('Coloque o valor do cateto a: '))
hip=math.hypot(ca,co)
print('A hipotenusa vai medir {:.2f}'.format(hip))