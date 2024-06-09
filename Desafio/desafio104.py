def leiaInt(msg):
    valor=(input(msg))
    while True:
        if valor.isnumeric():
            valor=int(valor)
            break
        else:
            print('erro')
            valor=str(input(msg))
    return valor


n=leiaInt('Digite um numero: ')
print(f'O numero digitado foi o {n}')