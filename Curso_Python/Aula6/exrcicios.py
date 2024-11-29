def calcular () :
    valorA = int(input("escolha o primeiro numero que você deseja multiplicar\n"))
    ValorB = int(input("escolha o segundo numero que você deseja multiplicar\n"))
    Resultado = valorA * ValorB
    
    print(Resultado)

    return Resultado
# calcular()
    
Valor_Mult = calcular()

def ValorMaior (Valor_Mult):
    if Valor_Mult >= 500 :
        print("É MAIOR")

    else :
        print("É MENOR")

ValorMaior(Valor_Mult)