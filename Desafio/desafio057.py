nome = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while nome != 'M' and nome != 'F':
    nome = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper().strip()
if nome == "F":
    nome = 'Femenino'
else:
    nome = 'Masculino'
print(f'Programa finalizado, Sexo {nome} registrado com sucesso!!')