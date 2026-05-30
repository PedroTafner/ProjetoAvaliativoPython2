import random as r

def gerar_id(opcao):
    id = ""
    if opcao == 1:
        alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        letra = r.randint(0,25)
        letra = alfabeto.pop(letra)
        id += str(letra)
        for _ in range(4):
            id += str(r.randint(0, 9))
        return id
    else:
        for _ in range(4):
            id += str(r.randint(0, 9))
        return id