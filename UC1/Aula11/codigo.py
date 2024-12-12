# Categorias Registradas

Categorias = ["Eletronicos", "Veiculo", "Eventos", "Roupa"]



#Variaveis de compras

CumpomDesconto = False

ValorCompra = 0.0

Carrinho = []

#Produtos cadastrados

    # Dicionario "marca","Preço","Categoria"

Produtos = {"Computador":["Acer AMD",2.050,"Eletronicos"], 
            "Carro":["Fox",30.000,"Veiculo"],
            "Shows":["RIR",700,"Eventos"],
            "Camisa":["Thug Nine",200,"Roupa"]
            }




def CalculoDeImpostos(Categoria):

    """

        Calculadora de impostos para cada categoria:

            Categoria: Parametro para saber como será calculado o imposto

    """

    if Categoria == "Eletronicos":

        print("Impostos Aplicados!")

        return 450*2


    if Categoria == "Veiculos":

        print("Impostos Aplicados!")

        return 1000*2


    if Categoria == "Eventos":

        print("Impostos Aplicados!")

        return 120*2


    if Categoria == "Roupas":

        print("Impostos Aplicados!")

        return 47*2

    else :
        print("A categoria solicitada não existe no nosso Banco de Dados")


def DescontosProdutos(Categoria,Quantidade):

    """

        Caculo de cada Desconto por categoria e por quantidade

            Categoria: Qual Categoria vai ser analisada

            Quantidade: Quantos itens o cliente esta comprando

    """

    if Categoria == "Eletronicos" and Quantidade >=2:

        return 200.20

   

def AdicionarCarrinho(Item,Quantidade):

    """

        Função que armazena a compra do usuario:

            Item: qual Item deseja aplicar ao carrinho

            Quantidade: Quantidade Comprada daquele item

    """

    return Carrinho.append(f"{Item} {str(Quantidade)}")

   




def SistemaCalculoFinanceiro():

    # Crie o seu codigo Aqui!!

    print("SISTEMA DE COMPRAS PARA E-Comerce!")

    Escolher_Produto = input("Qual produto deseja ?")
    Quantidade_escolhida = int(input ("qual é a quantidade desejada"))
    Produtos [Escolher_Produto]
    print(Produtos [Escolher_Produto][0])


    ValorCompra = Produtos[Escolher_Produto][1]* Quantidade_escolhida
    ValorCompra = ValorCompra - DescontosProdutos(Produtos[Escolher_Produto][2], Quantidade_escolhida)
    ValorCompra = ValorCompra + CalculoDeImpostos(Produtos[Escolher_Produto][2])

    print(f"A compra resultou em R$ {ValorCompra} deseja continuar ?")
    
    if input("Digite s para continuar") == "s":
         AdicionarCarrinho(Produtos[Escolher_Produto][0],Quantidade_escolhida)
    else:
        print("Compra Cancelada")

    return ValorCompra




while True:

    if SistemaCalculoFinanceiro() == 0.0:

        print("O usuario não comprou nenum item 😢")

    else:

        print(f"Carrinho do usuario 🛒")

        for i in Carrinho:

            print(i)