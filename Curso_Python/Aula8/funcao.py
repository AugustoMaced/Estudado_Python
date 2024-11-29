# criar uma função que repita X vezes Usuario decide 
# O usuario pode escolher o valor inicial 
# escolher o valor que vai ser incrementado
# ter opção se o valor vai ser incrementado ou o inverso (sub)

def RepetirECalcular (VezesRepeticao, ValorInicial, ValorIncrementado, Opcao = "+"):
    for i in range (VezesRepeticao):
        if Opcao == "+":
            ValorInicial= ValorInicial + ValorIncrementado
        else:
            ValorInicial= ValorInicial - ValorIncrementado

    return ValorInicial

print(RepetirECalcular(7,8,2))            