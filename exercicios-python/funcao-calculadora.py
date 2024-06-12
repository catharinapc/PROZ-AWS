'''
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

'''

def funcaoCalculadora(num1,num2,escolha):
    if(escolha==1):
        soma = num1 + num2
        return soma
    elif (escolha==2):
        menos = num1 - num2
        return menos
    elif (escolha==3):
        vezes = num1 * num2
        return vezes
    elif (escolha==4):
        try:
            divisao = num1 / num2
            return divisao
        except:
            print("Não é possível fazer uma divisão por 0")
    else:
        return 0
    
def main():
    while True:
        
        try:
            print("Digite o numero da operação desejada: 1. Soma  2. Subtração  3. Multiplicação  4. Divisão")
            codigoOperacao = input()
            operacaoConvertido = int(codigoOperacao)

            print("Digite o primeiro numero")
            primeiro = input()
            primeiroConvertido = float(primeiro)

            print("Digite o segundo numero")
            segundo = input()
            segundoConvertido = float(segundo)

            print(funcaoCalculadora(primeiroConvertido,segundoConvertido,operacaoConvertido))
            
        except:
            print("Por favor digite um valor numerico")

        terminarFuncao = input("Digite 'sim' para sair e 'não' para continuar: ").strip().lower()
        if terminarFuncao == 'sim':
            break

main()



 
        

    


