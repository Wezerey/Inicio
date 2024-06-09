def leiaDinheiro(msg):
    valor = str(input(msg))
    while True:
        if valor.isnumeric():
            break
        else:
            print('Erro')
            valor = str(input(msg))
    return float(valor)