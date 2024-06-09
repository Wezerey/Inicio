def txt(msg):
    print('*' * (len(msg)+4))
    print(f'  {msg}')
    print('*' * (len(msg)+4))


texto = str(input('Digite um texto:'))
txt(texto)