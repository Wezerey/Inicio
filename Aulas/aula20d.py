def vezes(list):
    pos = 0
    while pos < len(list):
        list[pos]*=2
        pos += 1
    print(list)


valor = [3,5,6,1,9]
vezes(valor)

