import tkinter as tk
from tkinter import ttk, messagebox
import time

# Lista onde os produtos ficam guardados durante a execução
produtos = []


# CORES DARK MODE

BG_MAIN = "#1e1e1e"
BG_FRAME = "#2b2b2b"
FG_TEXT = "white"
BTN_GREEN = "#28a745"
BTN_RED = "#dc3545"


# FUNÇÃO ADICIONAR

def adicionar():
    """
    Esta função cria um novo produto
    e adiciona-o à lista 'produtos'.
    Depois atualiza a tabela.
    """
    try:
        # Criar um ID baseado no tempo atual
        id_prod = int(time.time() % 100000)

        # Obter valores introduzidos pelo utilizador
        nome = entry_nome.get()
        preco = float(entry_preco.get())
        qtd = int(entry_qtd.get())

        # Guardar produto como tuplo
        produtos.append((id_prod, nome, preco, qtd))

        # Atualizar interface
        atualizar_tabela()

    except:
        messagebox.showerror("Erro", "Valores inválidos!")


# FUNÇÃO REMOVER

def remover():

    #Remove o produto selecionado na tabela.

    item = tabela.selection()
    if not item:
        return

    # Obter ID do item selecionado
    id_sel = tabela.item(item)["values"][0]

    # Criar nova lista sem o produto removido
    global produtos
    produtos = [p for p in produtos if p[0] != id_sel]

    atualizar_tabela()


# FUNÇÃO ATUALIZAR TABELA

def atualizar_tabela():

    #Limpa a tabela e insere novamente todos os produtos da lista.Também calcula o valor total do stock.

    tabela.delete(*tabela.get_children())

    total = 0

    for p in produtos:
        tabela.insert("", "end", values=p)
        total += p[2] * p[3]  # preço × quantidade

    # Atualizar texto do total
    lbl_total.config(text=f"Valor Total em Stock: {total:.2f} €")

    # Limpar campos de entrada
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)


# CRIAÇÃO DA JANELA

janela = tk.Tk()
janela.title("Gestor de Produtos - Dark Mode")
janela.geometry("750x550")
janela.configure(bg=BG_MAIN)


# ESTILO DA TABELA

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background=BG_FRAME,
                foreground="white",
                fieldbackground=BG_FRAME,
                rowheight=30)

style.configure("Treeview.Heading",
                background="#333333",
                foreground="white",
                font=("Arial", 10, "bold"))

style.map("Treeview",
          background=[("selected", "#444444")])


# TÍTULO

titulo = tk.Label(
    janela,
    text="GESTOR DE PRODUTOS",
    font=("Arial", 18, "bold"),
    bg=BG_MAIN,
    fg=FG_TEXT
)
titulo.pack(pady=15)


# FRAME DO FORMULÁRIO

frame_form = tk.Frame(janela, bg=BG_FRAME, padx=20, pady=20)
frame_form.pack(padx=20, pady=10, fill="x")

tk.Label(frame_form, text="Nome do Produto", bg=BG_FRAME, fg=FG_TEXT).grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(frame_form, width=25, bg="#3a3a3a", fg="white", insertbackground="white")
entry_nome.grid(row=1, column=0, padx=10)

tk.Label(frame_form, text="Preço (€)", bg=BG_FRAME, fg=FG_TEXT).grid(row=0, column=1, padx=10, pady=5)
entry_preco = tk.Entry(frame_form, width=15, bg="#3a3a3a", fg="white", insertbackground="white")
entry_preco.grid(row=1, column=1, padx=10)

tk.Label(frame_form, text="Quantidade", bg=BG_FRAME, fg=FG_TEXT).grid(row=0, column=2, padx=10, pady=5)
entry_qtd = tk.Entry(frame_form, width=15, bg="#3a3a3a", fg="white", insertbackground="white")
entry_qtd.grid(row=1, column=2, padx=10)

# Botões
btn_add = tk.Button(frame_form, text="Adicionar", bg=BTN_GREEN, fg="white", command=adicionar)
btn_add.grid(row=1, column=3, padx=15)

btn_rem = tk.Button(frame_form, text="Remover", bg=BTN_RED, fg="white", command=remover)
btn_rem.grid(row=1, column=4, padx=5)

# -------------------
# FRAME DA TABELA
# -------------------
frame_tabela = tk.Frame(janela, bg=BG_MAIN)
frame_tabela.pack(padx=20, pady=10, fill="both", expand=True)

tabela = ttk.Treeview(
    frame_tabela,
    columns=("ID", "Nome", "Preço", "Qtd"),
    show="headings"
)

tabela.heading("ID", text="ID")
tabela.heading("Nome", text="Produto")
tabela.heading("Preço", text="Preço (€)")
tabela.heading("Qtd", text="Stock")

tabela.column("ID", width=80, anchor="center")
tabela.column("Nome", width=250)
tabela.column("Preço", width=100, anchor="center")
tabela.column("Qtd", width=80, anchor="center")

tabela.pack(fill="both", expand=True)


lbl_total = tk.Label(
    janela,
    text="Valor Total em Stock: 0.00 €",
    font=("Arial", 12, "bold"),
    bg=BG_MAIN,
    fg=FG_TEXT
)
lbl_total.pack(pady=10)

# Iniciar aplicação
janela.mainloop()