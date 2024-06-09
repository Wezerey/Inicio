from math import pow,sqrt
num=int(input('Digite um numero (Ca): '))
num2=int(input('Digite um numero (Co): '))
ca=int(pow(num,2))
co=int(pow(num2,2))
hip=int(sqrt(ca+co))
print('A conta de hipotenusa8 é: hipo²=Ca² + Co²\nentao considerando Ca {}²={} e Co {}²={}, faremos a soma de ca e co = {}\nhipo²={}, ² pasara a ser raiz quadrada\nhipo=√{}, o resultado da conta é Hipo = {}'.format(num,ca,num2,co,(ca+co),(ca+co),(ca+co),hip))