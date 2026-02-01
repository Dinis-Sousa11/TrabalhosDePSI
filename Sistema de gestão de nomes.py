# Importamos o Tkinter, que é a biblioteca gráfica do Python
# É como o motor gráfico do Minecraft
import tkinter as tk

# messagebox serve para criar pop-ups (avisos, erros, confirmações)
# Tipo mensagens do servidor SMP
from tkinter import messagebox, ttk


# - Dados -

# Lista onde vamos guardar os nomes
#baú
nomes = []


#- Funçoes -

# Função para adicionar um nome
# É chamada quando clicamos no botão "Adicionar"
def adicionar_nome():

    # Lê o texto que o utilizador escreveu na caixa
    nome = entrada_nome.get().strip()
    # strip() remove espaços no início e no fim (anti-troll)

    # Se o nome não estiver vazio
    if nome:
        # Adiciona o nome à lista (baú)
        nomes.append(nome)

        # Atualiza a lista visual na interface
        atualizar_lista()

        # Limpa a caixa de texto
        entrada_nome.delete(0, tk.END)

        # Mostra uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Nome adicionado!")
    else:
        # Caso o utilizador não tenha escrito nada
        messagebox.showwarning("Aviso", "Digite um nome válido.")


# Função para remover um nome
def remover_nome():
    try:
        # Pega no índice do nome selecionado na lista
        selecionado = lista_nomes.curselection()[0]

        # Remove o nome da lista usando o índice
        nomes.pop(selecionado)

        # Atualiza a interface
        atualizar_lista()
    except:
        # Se não houver nada selecionado
        messagebox.showwarning("Aviso", "Selecione um nome para remover.")


# Função para procurar um nome
def procurar_nome():
    # Lê o nome escrito
    nome = entrada_nome.get().strip()

    # Verifica se o nome existe na lista
    if nome in nomes:
        messagebox.showinfo("Encontrado", f"O nome '{nome}' está na lista.")
    else:
        messagebox.showerror("Erro", f"O nome '{nome}' não foi encontrado.")


# Função para editar um nome existente
def editar_nome():
    try:
        # Índice do nome selecionado
        selecionado = lista_nomes.curselection()[0]

        # Novo nome escrito na caixa
        novo_nome = entrada_nome.get().strip()

        if novo_nome:
            # Substitui o nome antigo pelo novo
            nomes[selecionado] = novo_nome

            # Atualiza a interface
            atualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Digite o novo nome.")
    except:
        messagebox.showwarning("Aviso", "Selecione um nome para editar.")


# Função para ordenar os nomes de A a Z
def ordenar_nomes():
    # sort() organiza a lista alfabeticamente
    nomes.sort()
    atualizar_lista()


# Função para limpar todos os nomes
def limpar_lista():
    # Pergunta ao utilizador se tem a certeza
    if messagebox.askyesno("Confirmação", "Deseja apagar todos os nomes?"):
        # clear() apaga tudo da lista
        nomes.clear()
        atualizar_lista()


# Função que atualiza a lista visual
def atualizar_lista():
    # Limpa a lista gráfica
    lista_nomes.delete(0, tk.END)

    # Volta a inserir todos os nomes
    for nome in nomes:
        lista_nomes.insert(tk.END, nome)


# - main janela -

# Cria a janela principal
# É o "mundo" do Minecraft
janela = tk.Tk()
janela.title("Gestor de Nomes")
janela.geometry("450x520")
janela.configure(bg="#1e1e1e")  # Tema escuro
janela.resizable(False, False)


#- personalizaçao -

# ttk.Style permite personalizar o visual dos componentes
# tipo resource pack
style = ttk.Style(janela)
style.theme_use("clam")

# Estilo dos botões
style.configure(
    "Dark.TButton",
    font=("Segoe UI", 11),
    padding=10,
    background="#2d2d2d",
    foreground="white",
    borderwidth=0
)

# Efeito quando o rato passa por cima
style.map(
    "Dark.TButton",
    background=[("active", "#3a3a3a")]
)

# Estilo da caixa de texto
style.configure(
    "Dark.TEntry",
    fieldbackground="#2b2b2b",
    background="#2b2b2b",
    foreground="white",
    padding=8
)


#interface

#titulo da aplicaçao
titulo = tk.Label(
    janela,
    text=" Gestor de Nomes",
    bg="#1e1e1e",
    fg="white",
    font=("Segoe UI", 20, "bold")
)
titulo.pack(pady=15)

#caixa de texto para escrever nomes
entrada_nome = ttk.Entry(
    janela,
    style="Dark.TEntry",
    font=("Segoe UI", 12),
    width=30
)
entrada_nome.pack(pady=10)

# Frame para organizar os botões
frame_botoes = tk.Frame(janela, bg="#1e1e1e")
frame_botoes.pack(pady=10)

# Lista de botões com texto e função associada
botoes = [
    ("Adicionar", adicionar_nome),
    ("Remover", remover_nome),
    ("Procurar", procurar_nome),
    ("Editar", editar_nome),
    ("Ordenar A-Z", ordenar_nomes),
    ("Limpar Tudo", limpar_lista)
]

# Criação dos botões em grelha
for i, (texto, comando) in enumerate(botoes):
    ttk.Button(
        frame_botoes,
        text=texto,
        command=comando,
        style="Dark.TButton",
        width=18
    ).grid(row=i//2, column=i%2, padx=8, pady=8)

# Lista visual onde aparecem os nomes
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

# Mantém o programa a correr
# Sem isto, a janela fecha logo
janela.mainloop()