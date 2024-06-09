def soma(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f'Somando os {valores} eu tenho o resultado {s}')

soma(1,9,5)
soma(8,5,1,5)
