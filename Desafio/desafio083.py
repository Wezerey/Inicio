r = str(input('Digite o comando: exemplo (a+b) :'))
l=o=0
for y,x in enumerate(r):
    print(y)
    print(x)
    if x == '(':
        l+=1
    if x == ')':
        o += 1
if l == o:
    print('Seu comando esta certo')
else:
    print('Seu comando esta errado')