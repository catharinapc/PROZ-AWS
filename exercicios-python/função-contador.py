#precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#ORDEM NORMAL

def contadorHotel():
    for i in range(21):
        if (i==13):
            continue
        else:
            print(i)

#ORDEM DECRESCENTE

def contadorHotelDec():
    for i in range(20,-1,-1):
        if (i==13):
            continue
        else:
            print(i)

#USANDO WHILE


def contadorWhile():
    contador = 0
    while(contador <= 20):
        if(contador != 13):
            print(contador)
    
        contador = contador + 1

contadorWhile()