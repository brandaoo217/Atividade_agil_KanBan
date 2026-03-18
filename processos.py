
def media(nota):

    tam = len(nota)
    
    soma = 0

    for n in nota:
        soma = soma + n

    media = soma/tam

    return (media)

def aprovacao(valor):

    if valor >= 7:
        return True    
    else:
        return False

def validacao(lista):
    if len(lista) == 0:
        return print("Aprovado")
    else:
        return print("Reprovado")
 