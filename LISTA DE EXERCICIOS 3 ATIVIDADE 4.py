#Faça um programa que leia 5 números e informe a soma e a média dos números.

if __name__ == '__main__':

    contador = 1
    soma = 0

    while (contador<=5):
        numero = int(input("Digite os numeros: "))
        soma = soma + numero
        contador = contador+1

    print(soma)
    media = soma / 5
    print(media)
