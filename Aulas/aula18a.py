teste = list ()
teste.append('Weslley')
teste.append('24')
galera = list ()
galera.append((teste[:]))
teste[0]='Kay'
teste[1]='21'
print(galera)
galera.append(teste[:])
print(galera)