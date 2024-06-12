'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2024).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
'''

def calculaIdade(nascimento):
    return 2024 - nascimento

def main():
    nome = input('Digite seu nome completo: ')
    validador = True
    while(validador):
        try:
            ano = int(input('Digite um ano de nascimento entre 1922 e 2023: '))
            if(ano<1922 or ano>2023):
                print("Por favor digite um ano valido")
            else:
                validador = False
        except:
            print("Por favor digite um numero inteiro entre 1922 e 2023")
    idade = calculaIdade(ano)
    print("O nome completo do usuário é " + nome)
    print("A idade do usuário ao final de 2024 será " + str(idade))

main()


    


    