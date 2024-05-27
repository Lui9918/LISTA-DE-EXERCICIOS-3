#Faça um programa que calcule o mostre a média aritmética de N notas.

if __name__ == '__main__':

    quantidade_notas = int(input("Quantas notas voce deseja calcular?"))

    contador = 1
    soma = 0

    while (contador <= quantidade_notas):
        numero = int(input("Digite as notas: "))
        soma = soma + numero
        contador = contador+1

    print(soma)
    media = soma / quantidade_notas
    print(media)


