import random

print("**********************************")
print("**Bem vindo ao gerador de senhas**")
print("**********************************")

#Caracteres 
senha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*()_-+={[}]|\.,:;?1234567890"

#Input
qtd_senhas = int(input("Quantas senha você quer: "))
tam_senha = int(input("Tamanho da senha: "))

#Imprime as senhas
print("Senhas:")

#Gera a sequencia aleatoria
for pwd in range(qtd_senhas):
    ger_senha = ""
    for c in range(tam_senha):
        ger_senha += random.choice(senha)
    print(ger_senha)