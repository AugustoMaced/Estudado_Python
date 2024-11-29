
def Soma () :
    a = 2 
    b = 3 
    print (a + b)

def Repetir (repeticao:int, nome:str, MostrarMesagem:bool=True):
    VezesFoiRepetida = 0 
    for x in range (repeticao):
        VezesFoiRepetida+=1
    if MostrarMesagem == True :    
        return f"{nome} executou {VezesFoiRepetida} vezes"
    else:
        return repeticao

UsuarioRepete = int(input(" Quantas vezes você quer que executar ?"))
Repetir(UsuarioRepete, "Augusto", True)
Resultado = Repetir(UsuarioRepete, "Augusto", )
print(Resultado)


#Ou

# def Repetir ( nome, repeticao= input("Digite um valor"), MostrarMesagem=True):
#     VezesFoiRepetida = 0 
#     for x in range (repeticao):
#         VezesFoiRepetida+=1
#     if MostrarMesagem == True :    
#         print(f"{nome} executou {VezesFoiRepetida} vezes")


# Repetir("Augusto")


#ou
# Repetir(int(input(" Quantas vezes você quer que executar ?")))

# for i in range (10):
#     Soma()