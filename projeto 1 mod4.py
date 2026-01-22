import random

while True:
    print("\n=== Gerador De Passwords ===")
    print("1 - Iniciais das palavras + números")
    print("2 - Iniciais + números + símbolo")
    print("3 - Palavra inteira + números")
    print("0 - Sair")


    opcao = input("Escolha uma opção: ")

    # Opção para sair do programa
    if opcao == "0":
        print("Adeus!!👋")
        break


    frase = input("Digite uma frase: ")

    #divide a frase em palavras (lista)
    palavras = frase.split()

    #onde a senha vai ser feita
    senha = ""

    #1 iniciais das palavras+numeros
    if opcao == "1":
        for palavra in palavras:
            senha += palavra[0].upper()  #primeira letra de cada palavra em maiuscula
        senha += str(random.randint(0, 999))  #adiciona um número aleatorio

    #2 iniciais+numeros+simbolo
    elif opcao == "2":
        for palavra in palavras:
            senha += palavra[0].upper()
        senha += str(random.randint(0, 999))
        senha += random.choice("!@#$%&§*")  # adiciona um simbolo aleatorio

    #3 palavra inteira aleatoria+numeros
    elif opcao == "3":
        senha = random.choice(palavras).capitalize()  #escolhe uma palavra aleatoria
        senha += str(random.randint(100, 9999))


    else:
        print("Opção inválida!")
        continue  #volta ao inicio do menu

    #embaralha os caracteres da senha
    lista_senha = list(senha)     # Converte a senha numa lista
    random.shuffle(lista_senha)   # Embaralha a lista
    senha = "".join(lista_senha)  # Converte novamente para string

    #senha final
    print("Senha gerada:", senha)
