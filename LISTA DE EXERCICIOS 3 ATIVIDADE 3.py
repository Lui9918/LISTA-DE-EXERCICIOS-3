#Faça um programa que leia 5 números e informe o maior número.

if __name__ == '__main__':

    n = int(input("Digite os numeros: "))
    maior = n
    contador = 1

while (contador < 5):
    n= int(input())
    if (n > maior):
        maior = n
        contador = contador + 1
print(maior)
