m=float(input('Uma distancia em metros: '))
print('A medida de {} corresponde a'.format(m))
print('{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format((m*0.001),(m*0.01),(m*0.1),(m*10),(m*100),(m*1000)))