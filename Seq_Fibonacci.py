from Exceptions.numeroinvalido import NumeroInvalido


# FUNÇÃO RECURSIVA FIBONNACI
def FibonnaciRecursiva(termo):
    if termo == 0:
        return 0
    elif termo == 1:
        return 1
    else:
        return FibonnaciRecursiva(termo-1) + FibonnaciRecursiva(termo-2)

# FUNÇÃO LINEAR FIBONNACI
def FibonnaciLinear(termo):
    a = 0
    b = 1
    if termo == 0:
        return 0
    elif termo == 1:
        return 1
    else:
        for i in range(1, termo):
            resultado = a + b
            a = b
            b = resultado
    return resultado

def mensagem():
    try: 
        num =  int(input("Digite um número para saber seu correspondente na sequencia de Fibonnaci: "))
        if num < 0:    
            raise NumeroInvalido
        else:
            return num
    except NumeroInvalido:
        mensagem()

num = mensagem()
print(f'Recursiva de Fibonnaci: {FibonnaciRecursiva(num)}')
print(f'Linear de Fibonnaci: {FibonnaciLinear(num)}')