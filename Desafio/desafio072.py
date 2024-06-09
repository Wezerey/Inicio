numero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
n=int(input('Digite um numero:'))
while True:
    if n <= 10:
        print(numero[n])
        break
    else:
        n = int(input('Tente novamente:'))
