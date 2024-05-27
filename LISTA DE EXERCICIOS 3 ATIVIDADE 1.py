#Faça um programa que peça um número, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

if __name__ == '__main__':

    numero = int(input("Insira um numero:"))


    #Enquanto o numero for invalido
    while (numero < 0) or (numero > 10):
        print("Numero invalido!")
        numero = int(input("Insira um numero: "))

    print("Numero valido!")

