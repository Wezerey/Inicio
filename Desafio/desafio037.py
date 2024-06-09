numero=int(input('Digite um numero? '))
print('Escolha uma das opcoes abaixo')
print('[1] para binario')
print('[2] para octal')
print('[3] para hexadecimal')
choise = int(input('Sua opcao: '))
if choise == 1:
    print(f'{numero} convertido para binario: {bin(numero)[2:]}')
elif choise == 2:
    print(f'{numero} convertido para octal: {oct(numero)[2:]}')
elif choise == 3:
    print(f'{numero} convertido para hexadecimal: {hex(numero)[2:]}')
else:
    print('Opcao invalida')