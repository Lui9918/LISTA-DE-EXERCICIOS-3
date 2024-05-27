#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

if __name__ == '__main__':

    print("Bem vindo a sua conta!")
    usuario = input("Para começarmos digite seu nome de usuario:")
    senha = input("Agora digite sua senha:")

while usuario == senha:
    print("Sua senha não pode ser igual ao seu nome de usuário. Por favor, escolha uma senha diferente.")
    senha = input("Agora digite sua senha:")

print ("Senha valida, login concluido!")


