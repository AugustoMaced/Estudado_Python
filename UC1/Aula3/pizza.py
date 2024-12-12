

Pizza = ["Massa", "Molho de Tomate", "Queijo Mussarela", "Orégano"]
print ( "Sua Pizza Terá os Seguintes Igredientes:" + str (Pizza))
Continuar = True
while Continuar:
    NovoIgrediente = input ("Adicione seu igrediente da sua Pizza personalizada: ")



    Pizza.append(NovoIgrediente)

    print ("Sua Pizza Personalizada Terá os Seguintes Igredientes: " + str (Pizza))
        


    Resposta001 = input ("Deseja adicionar mais alguma coisa? Digite Sim ou Não: ")

    if Resposta001 == "Sim":
        print("")

        
    if Resposta001 == "Não":

        Resposta002 = input ("Deseja remover alguma coisa? Digite Sim ou Não: ")

        if Resposta002 == "Sim":
            Pizza.remove ( input ("Deseja Remover Qual Igrediente da Sua Pizza Personalizada: ") )
        
        
        if Resposta002 == "Não":

          Continuar = False
        
          PizzaValor = ((len(Pizza)-4)*5)+30

          print ("Sua Pizza terá o valor de "+ str (PizzaValor)+" Reais. ")
          print ("Obrigado pela Preferência Epero que goste do Nosso Produto, Volte Sempre ^^")
