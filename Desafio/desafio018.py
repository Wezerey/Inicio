import math
ang=int(input('Digite o angulo: '))
seno=math.sin(math.radians(ang))
coseno=math.cos(math.radians(ang))
tang=math.tan(math.radians(ang))
print('O angulo de {} tem: seno de {:.2f} coseno de {:.2f} tangente de {:.2f}'.format(ang,seno,coseno,tang))