pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade':22}
del pessoas ['nome']
print('===== comando del nome =====')
for k in pessoas.keys():
    print(k)
print('-'*20)
pessoas ['nome'] = 'Erik'
print('===== acrescentado nome erik =====')
for k,v in pessoas.items():
    print(k,'-',v)