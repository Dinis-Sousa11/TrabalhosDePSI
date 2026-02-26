import tkinter as tk                 # Biblioteca principal para GUI
from tkinter import ttk, messagebox  # ttk = widgets modernos | messagebox = popups
import time                          # Usado para gerar IDs únicos


# Lista onde ficam guardados todos os produtos

produtos = []


# CORES - DARK MODE

BG_MAIN = "#1e1e1e"      # Fundo principal da janela
BG_FRAME = "#2b2b2b"     # Fundo dos frames
FG_TEXT = "white"        # Cor padrão do texto
BTN_GREEN = "#28a745"    # Cor botão adicionar
BTN_RED = "#dc3545"      # Cor botão remover
BTN_YELLOW = "#f0ad4e"   # Cor botão editar


# FUNÇÕES PRINCIPAIS

def adicionar():

    try:
        id_prod = int(time.time() % 100000)  # Geração simples de ID

        nome = entry_nome.get()    #vai buscar nos tres
        preco = float(entry_preco.get())
        qtd = int(entry_qtd.get())

        produtos.append((id_prod, nome, preco, qtd))   #adiciona na lista de tuplos

        atualizar_tabela()

    except:
        messagebox.showerror("Erro", "Valores inválidos!")


def remover():

    item = tabela.selection()
    if not item:
        return

    id_sel = tabela.item(item)["values"][0]   #pega no id

    global produtos
    produtos = [p for p in produtos if p[0] != id_sel]   #cria nova lista, percorre, mantem os n selecionados

    atualizar_tabela()


def editar():

    #Edita o produto selecionado com os dados escritos nos campos.

    item = tabela.selection()
    if not item:
        return

    id_sel = tabela.item(item)["values"][0]  #pega no id para ter a certeza que edita o certo

    try:
        for i, p in enumerate(produtos):
            if p[0] == id_sel:
                produtos[i] = (      #sobreescreve o tuplo
                    id_sel,
                    entry_nome.get(),
                    float(entry_preco.get()),
                    int(entry_qtd.get())
                )

        atualizar_tabela()

    except:
        messagebox.showerror("Erro", "Valores inválidos!")


def pesquisar(event=None):  #permite procurar por keyrealese e pesquisar normal

    #Filtra os produtos pelo nome enquanto o utilizador escreve

    termo = entry_pesquisa.get().lower()

    tabela.delete(*tabela.get_children())

    for p in produtos:
        if termo in str(p[1]).lower():
            tabela.insert("", "end", values=p)    #e passar do if escreve no final


def limpar_lista():

    #Apaga todos os produtos após confirmação.

    if messagebox.askyesno("Confirmar", "Deseja limpar toda a lista?"):
        global produtos
        produtos = []
        atualizar_tabela()


def atualizar_tabela():

    tabela.delete(*tabela.get_children())    #devolve uma lista que e apagada
                                             #serve para limpar a tabela antes de mostrar
    total = 0

    for p in produtos:
        tabela.insert("", "end", values=p)
        total += p[2] * p[3]    #calcular o preço final

    lbl_total.config(text=f"Valor Total em Stock: {total:.2f} €")

    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)


def carregar_campos(event):   #ativada pelo rato

    #Quando o utilizador faz duplo clique numa linha,os dados são carregados automaticamente para os campos.

    item = tabela.selection()
    if not item:
        return

    v = tabela.item(item)["values"]   #inserir numa variavel para escrever de seguida

    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, v[1])

    entry_preco.delete(0, tk.END)
    entry_preco.insert(0, v[2])

    entry_qtd.delete(0, tk.END)
    entry_qtd.insert(0, v[3])


# CRIAÇÃO DA JANELA PRINCIPAL


janela = tk.Tk()  # Cria a janela principal
janela.title("Gestor de Produtos - Dark Mode")  # Título
janela.geometry("800x600")  # Tamanho inicial
janela.configure(bg=BG_MAIN)  # Cor de fundo


# ESTILO DA TABELA (TTK)

style = ttk.Style()
style.theme_use("default")

# Estilo das linhas
style.configure("Treeview",
                background=BG_FRAME,
                foreground="white",
                fieldbackground=BG_FRAME,
                rowheight=30)

# Estilo do cabeçalho
style.configure("Treeview.Heading",
                background="#333333",
                foreground="white",
                font=("Arial", 10, "bold"))

# Cor quando uma linha está selecionada
style.map("Treeview", background=[("selected", "#444444")])


# TÍTULO DA APLICAÇÃO

titulo = tk.Label(janela,
                  text="GESTOR DE PRODUTOS",
                  font=("Arial", 18, "bold"),
                  bg=BG_MAIN,
                  fg=FG_TEXT)

titulo.pack(pady=10)


# FRAME DO FORMULÁRIO

# Frame para agrupar os campos de entrada
frame_form = tk.Frame(janela,
                      bg=BG_FRAME,
                      padx=15,
                      pady=15)

frame_form.pack(padx=20, pady=10, fill="x")


#CAMPOS DE ENTRADA

tk.Label(frame_form, text="Nome do Produto",
         bg=BG_FRAME, fg=FG_TEXT).grid(row=0, column=0, padx=5)

entry_nome = tk.Entry(frame_form,
                      width=25,
                      bg="#3a3a3a",
                      fg="white",
                      insertbackground="white")

entry_nome.grid(row=1, column=0, padx=5)


tk.Label(frame_form, text="Preço (€)",
         bg=BG_FRAME, fg=FG_TEXT).grid(row=0, column=1, padx=5)

entry_preco = tk.Entry(frame_form,
                       width=15,
                       bg="#3a3a3a",
                       fg="white",
                       insertbackground="white")

entry_preco.grid(row=1, column=1, padx=5)


tk.Label(frame_form, text="Quantidade",
         bg=BG_FRAME, fg=FG_TEXT).grid(row=0, column=2, padx=5)

entry_qtd = tk.Entry(frame_form,
                     width=15,
                     bg="#3a3a3a",
                     fg="white",
                     insertbackground="white")

entry_qtd.grid(row=1, column=2, padx=5)


#  BOTÕES

btn_add = tk.Button(frame_form,
                    text="Adicionar",
                    bg=BTN_GREEN,
                    fg="white",
                    command=adicionar)

btn_add.grid(row=1, column=3, padx=10)


btn_edit = tk.Button(frame_form,
                     text="Editar",
                     bg=BTN_YELLOW,
                     fg="white",
                     command=editar)

btn_edit.grid(row=1, column=4, padx=5)


btn_rem = tk.Button(frame_form,
                    text="Remover",
                    bg=BTN_RED,
                    fg="white",
                    command=remover)

btn_rem.grid(row=1, column=5, padx=5)


btn_limpar = tk.Button(frame_form,
                       text="Limpar Lista",
                       bg="#555555",
                       fg="white",
                       command=limpar_lista)

btn_limpar.grid(row=1, column=6, padx=5)


# PESQUISA

tk.Label(janela,
         text="Pesquisar Produto:",
         bg=BG_MAIN,
         fg=FG_TEXT).pack(pady=(0, 2))

entry_pesquisa = tk.Entry(janela,
                          width=30,
                          bg="#3a3a3a",
                          fg="white",
                          insertbackground="white")

entry_pesquisa.pack()

# Sempre que o utilizador escreve, executa a função pesquisar
entry_pesquisa.bind("<KeyRelease>", pesquisar)


# TABELA DE PRODUTOS

frame_tabela = tk.Frame(janela, bg=BG_MAIN)
frame_tabela.pack(padx=20, pady=10, fill="both", expand=True)

tabela = ttk.Treeview(frame_tabela,
                      columns=("ID", "Nome", "Preço", "Qtd"),
                      show="headings")

# Cabeçalhos
tabela.heading("ID", text="ID")
tabela.heading("Nome", text="Produto")
tabela.heading("Preço", text="Preço (€)")
tabela.heading("Qtd", text="Stock")

# Largura e alinhamento das colunas
tabela.column("ID", width=80, anchor="center")
tabela.column("Nome", width=250)
tabela.column("Preço", width=100, anchor="center")
tabela.column("Qtd", width=80, anchor="center")

tabela.pack(fill="both", expand=True)

# Duplo clique carrega os dados para edição
tabela.bind("<Double-1>", carregar_campos)


# LABEL DO TOTAL

lbl_total = tk.Label(janela,
                     text="Valor Total em Stock: 0.00 €",
                     font=("Arial", 12, "bold"),
                     bg=BG_MAIN,
                     fg=FG_TEXT)

lbl_total.pack(pady=5)


# Mantém a aplicação aberta
janela.mainloop()
