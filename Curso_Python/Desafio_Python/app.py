import os
import arquivo
FINALIZAR = "/sair"
Entrada_usuario = ""
Opcoes_usuario = ["0 - Ler anotação","1 - Escrever anotação", "2 - Lembrar anotações"]

while Entrada_usuario != FINALIZAR:
    print("=======================")
    for a in Opcoes_usuario:
        print(a)
    print("=======================")
    Entrada_usuario = input("O que deseja fazer ?")

    if Entrada_usuario == "0":
       Entrada_usuario = input("Qual é o nome da sua anotação:")
       arquivo.LerArquivos(Entrada_usuario+".txt") 
    
    if Entrada_usuario == "1":
        Entrada_usuario = input("Qual é o nome da sua anotação:")
        arquivo.CriarArquivo(Entrada_usuario+".txt")  
    
    if Entrada_usuario == "2":
        arquivo.ListarAnotacao()

    os.system("cls")