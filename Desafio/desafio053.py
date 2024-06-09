st = str(input('Digite uma frase: ')).strip().upper()
palavras = st.split()
junto = ''.join(palavras)
inverso =""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    print(f'o inverso de {junto} é {inverso}')
    if inverso == junto:
        print('temo um palindromo')
    else:
        print('nao temos um palindromo')