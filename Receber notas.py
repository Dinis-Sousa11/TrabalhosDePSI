notas = []

while True:
    nota = input("Insere uma nota ou escreva 'sair' para terminar: ")

    if nota.lower() == "sair":
        break

 notas.append(float(nota))

if len(notas) > 0:
    print("Notas inseridas:", notas)
    print("Nota mais baixa:", min(notas))
    print("Nota mais alta:", max(notas))
    print("Media das notas:", sum(notas) / len(notas))
else:
    print("Nenhuma nota foi inserida.")