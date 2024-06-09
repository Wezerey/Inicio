n1=int(input('Digite um numero'))
n2=int(input('Digite um numero'))
n3=int(input('Digite um numero'))
if n1 > n2:
    m=n1
else:
    m=n2
if m > n3:
    print('o maior numero é {}'.format(m))
else:
    m = n3
    print('o maior numero é {}'.format(m))
if n1 < n2:
    n=n1
else:
    n=n2
if n < n3:
    print('o menor numero é {}'.format(n))
else:
    n = n3
    print('o menor numero é {}'.format(n))
