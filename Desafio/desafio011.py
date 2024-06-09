la=float(input('Largura da parede: '))
al=float(input('Altura da parede: '))
print('Sua parede tem a dimensao de {}x{} e sua area é de {:.3f}m²\nPara pintar essa parede , voce precisará de {:.4f}l de tinta'.format(la,al,(la*al),(la*al)/2))