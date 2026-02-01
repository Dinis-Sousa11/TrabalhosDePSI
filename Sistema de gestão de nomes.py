# Importa a biblioteca Tkinter para criar interfaces gráficas
import tkinter as tk

# Importa caixas de mensagem e widgets estilizados (ttk)
from tkinter import messagebox, ttk


# lista para onde vão os nomes
nomes = []


# funçoes

# Adiciona um nome à lista
def adicionar_nome():
    nome = entrada_nome.get().strip()  # Lê o texto da caixa e remove espaços extras

    if nome:
        nomes.append(nome)             # Adiciona à lista
        atualizar_lista()              # Atualiza a lista visual
        entrada_nome.delete(0, tk.END) # Limpa a caixa de texto
        messagebox.showinfo("Sucesso", "Nome adicionado!")
    else:
        messagebox.showwarning("Aviso", "Digite um nome válido.")


# Função responsável por remover um nome da lista
def remover_nome():

    # Obtém os índices dos itens selecionados na Listbox
    # O resultado é uma tupla, por exemplo: (0,) ou (2,)
    selecionado = lista_nomes.curselection()

    # se houver algo
    if selecionado:

        # Guarda o índice do primeiro item selecionado
        indice = selecionado[0]

        # Remove da lista 'nomes' o elemento que está nessa posição
        nomes.pop(indice)

        # Atualiza a lista visual para refletir a remoção
        atualizar_lista()

    else:
        # Executado quando nenhum nome foi selecionado
        messagebox.showwarning(
            "Aviso",
            "Selecione um nome para remover."
        )

# Procura um nome na lista
def procurar_nome():
    nome = entrada_nome.get().strip()

    if nome in nomes:
        messagebox.showinfo("Encontrado", f"O nome '{nome}' está na lista.")
    else:
        messagebox.showerror("Erro", f"O nome '{nome}' não foi encontrado.")


# Função responsável por editar o nome selecionado na lista
def editar_nome():

    # obtém os índices dos itens selecionados na Listbox
    # o resultado é uma tupla
    selecionado = lista_nomes.curselection()

    # Verifica se existe algum item selecionado
    if selecionado:

        # Guarda o índice do item selecionado
        indice = selecionado[0]

        # Lê o novo nome escrito na caixa de texto
        # strip() remove espaços no início e no fim
        novo_nome = entrada_nome.get().strip()

        # Verifica se o novo nome não está vazio
        if novo_nome:

            # Substitui o nome antigo pelo novo nome
            nomes[indice] = novo_nome

            # Atualiza a lista visual para mostrar a alteração
            atualizar_lista()

        else:
            # Caso a caixa de texto esteja vazia
            messagebox.showwarning(
                "Aviso",
                "Digite o novo nome."
            )
    else:
        # Executado quando nenhum nome está selecionado
        messagebox.showwarning(
            "Aviso",
            "Selecione um nome para editar."
        )


# Ordena os nomes alfabeticamente
def ordenar_nomes():
    nomes.sort()
    atualizar_lista()


# Limpa todos os nomes da lista
def limpar_lista():
    if messagebox.askyesno("Confirmação", "Deseja apagar todos os nomes?"):
        nomes.clear()
        atualizar_lista()


# Atualiza a lista visual
def atualizar_lista():
    lista_nomes.delete(0, tk.END)
    for nome in nomes:
        lista_nomes.insert(tk.END, nome)


# main janela

# Cria a janela principal
janela = tk.Tk()
janela.title("Gestor de Nomes")
janela.geometry("450x520")
janela.configure(bg="#1e1e1e")
janela.resizable(False, False)


# coisas para ficar bonito 

style = ttk.Style(janela)
style.theme_use("clam")

style.configure(
    "Dark.TButton",
    font=("Segoe UI", 11),
    padding=10,
    background="#2d2d2d",
    foreground="white",
    borderwidth=0
)

style.map(
    "Dark.TButton",
    background=[("active", "#3a3a3a")]
)

style.configure(
    "Dark.TEntry",
    fieldbackground="#2b2b2b",
    background="#2b2b2b",
    foreground="white",
    padding=8
)


# ---------------- INTERFACE ----------------

# Título da aplicação
titulo = tk.Label(
    janela,
    text="Gestor de Nomes",
    bg="#1e1e1e",
    fg="white",
    font=("Segoe UI", 20, "bold")
)
titulo.pack(pady=15)

# Caixa de texto para inserir nomes
entrada_nome = ttk.Entry(
    janela,
    style="Dark.TEntry",
    font=("Segoe UI", 12),
    width=30
)
entrada_nome.pack(pady=10)

# Frame para os botões
frame_botoes = tk.Frame(janela, bg="#1e1e1e")
frame_botoes.pack(pady=10)

# Lista de botões
botoes = [
    ("Adicionar", adicionar_nome),
    ("Remover", remover_nome),
    ("Procurar", procurar_nome),
    ("Editar", editar_nome),
    ("Ordenar A-Z", ordenar_nomes),
    ("Limpar Tudo", limpar_lista)
]

# Cria os botões em formato de grelha
for i, (texto, comando) in enumerate(botoes):
    ttk.Button(
        frame_botoes,
        text=texto,
        command=comando,
        style="Dark.TButton",
        width=18
    ).grid(row=i//2, column=i%2, padx=8, pady=8)

# Lista onde os nomes aparecem
lista_nomes = tk.Listbox(
    janela,
    font=("Segoe UI", 12),
    bg="#2b2b2b",
    fg="white",
    selectbackground="#444",
    relief="flat",
    height=10
)
lista_nomes.pack(padx=20, pady=20, fill=tk.BOTH)

# Rodapé
rodape = tk.Label(
    janela,
    text="Mini Projeto • Dark UI • Python",
    bg="#1e1e1e",
    fg="#888",
    font=("Segoe UI", 9)
)
rodape.pack(pady=5)

# Mantém a aplicação em execução
janela.mainloop()
rodape.pack(pady=5)

# Mantém o programa a correr
# Sem isto, a janela fecha logo

janela.mainloop()
