import math
from Exceptions.numeroinvalido import NumeroInvalido


#Lista de PrimosSequencial
lista = list()
def LinearPrimos(num):
    for n in range(num+1):
        if  n == 1 or (n!=2 and n % 2 == 0):
            pass
        elif n == 2:
            lista.append(n)
        else:
            if n >= 9:
                cont = 0
                raiz = int(math.sqrt(n))
                for i in range (3, raiz+1, 2):
                    if n % i == 0:
                        cont = 1
                        break
                if cont == 0:
                    lista.append(n)
            else:
                cont = 0
                for i in range(2,n):
                    if n % i == 0:
                        break
                if cont == 0:
                    lista.append(n)
                
    return(lista)


def RecursivaPrimos(termo, div = 1):
    if div != termo-1:
        div  += 1

    if div == termo-1:
        return termo
    elif termo % div == 0:
        return False 
    else:
        return RecursivaPrimos(termo, div)
    
def Lista_primos(num, cont = 2):
    primos = []

    while cont < num:
        if RecursivaPrimos(cont):
            primos.append(cont)
        cont += 1
    return primos

def mensagem():
    try: 
        num = int(input("Digite um n° para sabermos quaisa são os números primos que exixtem até eles: "))
        if num <= 1:    
            raise NumeroInvalido
        else:
            return num
    except NumeroInvalido:
        mensagem()

num = mensagem()
print(f'Linear de Primos: {LinearPrimos(num)}')
print(f'Recursiva de Primos : {Lista_primos(num)}') #essa função chama a função recursiva em questão