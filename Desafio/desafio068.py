from random import randint
contador = 0
while True:
    numero_computador = randint(1,10)
    numero = int(input('Digite um numero: '))
    resposta = str(input('Escolhe impar ou par [I/P]: ')).strip().upper()
    soma = numero_computador + numero
    print("=" * 40)
    if resposta == 'P':
        Par_impar = True
    else:
        Par_impar = False
    if soma % 2 == 0:
        Verificacao = True
    else:
        Verificacao = False
    if Verificacao == True:
        print(f'Pc Jogou {numero_computador} == Voce Jogou {numero} == {soma} DEU PAR')
    else:
        print(f'Pc Jogou {numero_computador} == Voce Jogou {numero} == {soma} DEU IMPAR')
    print("=" * 40)
    if Verificacao == True and Par_impar == True or Verificacao == False and Par_impar == False:
        contador += 1
    else:
        print('Perdeu')
        break
print(f'Voce ganhou {contador}x')
