def bicesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
        return True
    else:
        return False
def menu():
    ano = int(input("qual o ano? "))
    if bicesto(ano):
        print(f"O ano {ano} é bicesto")
    else:
        print(f"O ano {ano} é nao bicesto")

menu()