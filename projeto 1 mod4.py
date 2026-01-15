import random

print("=== Gerador De Passwords ===")
print("1 - Iniciais das palavras + números")
print("2 - Iniciais + números + símbolo")
print("3 - Palavra inteira + números")

opcao = input("Escolha uma opção: ")

frase = input("Digite uma frase: ")
palavras = frase.split()
senha = ""

#iniciais+numeros
if opcao == "1":
    for palavra in palavras:
        senha += palavra[0].upper()
    senha += str(random.randint(0, 999))

#palavra+numeros+simbolos
elif opcao == "2":
    for palavra in palavras:
        senha += palavra[0].upper()
    senha += str(random.randint(0, 999))
    senha += random.choice("!@#$%&§*")

#palavra+numeros
elif opcao == "3":
    senha = random.choice(palavras).capitalize()
    senha += str(random.randint(100, 9999))

else:
    print("Opção inválida!")
    exit()

# Embaralhar a senha
lista_senha = list(senha)
random.shuffle(lista_senha)
senha = "".join(lista_senha)

print("Senha gerada:", senha)
