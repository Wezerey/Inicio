n = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0 and c % 2 == 1:
        n += c
        cont += 1
print(n," ",cont)
