def txt(msg):
    tam = len(msg)+4
    print('*' * tam)
    print(f'  {msg}')
    print('*' * tam)


texto = str(input('Digite um texto:'))
txt(texto)
txt('Mensage, teste')