def leiaInt():
    while True:

        while True:
            try:
                inteiro=int(input('Digite um valor inteiro:'))
                break
            except (ValueError, TypeError):
                print('Erro, digite um numero inteiro valido')
        while True:
            try:
                reali=float(input('Digite um valor real:'))
                break
            except (ValueError, TypeError):
                print('Erro, digite um numero inteiro valido')
            except (KeyboardInterrupt):
                print('Erro, o usuario preferiu nao digitar o numero.')
                reali = 0
                break
        print(f'O valor inteiro {inteiro}, e o valor real {reali}')






leiaInt()
