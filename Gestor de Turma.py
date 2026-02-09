import tkinter as tk
from tkinter import messagebox, simpledialog

# ---------- Limites ----------
NOTA_MIN = 0
NOTA_MAX = 20
FALTAS_MIN = 0
FALTAS_MAX = 60
FALTAS_CHUMBO = 30  # acima disto reprova

# ---------- Dados ----------
turma = []
filtro_atual = "Todos"

# ---------- Funções ----------
def calcular_situacao(nota, faltas):
    if faltas > FALTAS_CHUMBO:
        return "Reprovado por faltas"
    elif nota < 10:
        return "Reprovado por nota"
    else:
        return "Aprovado"

def validar_nota(nota):
    return NOTA_MIN <= nota <= NOTA_MAX

def validar_faltas(faltas):
    return FALTAS_MIN <= faltas <= FALTAS_MAX

def validar_texto(texto):
    return texto.replace(" ","").isalpha()

def atualizar_lista():
    listbox.delete(0, tk.END)
    for a in turma:
        if filtro_atual == "Aprovados" and a['situacao'] != "Aprovado":
            continue
        if filtro_atual == "Reprovados" and a['situacao'] == "Aprovado":
            continue

        idx = listbox.size()
        listbox.insert(
            tk.END,
            f"{a['nome']} | {a['disciplina']} | Nota: {a['nota']} | "
            f"Faltas: {a['faltas']} | {a['situacao']}"
        )

        listbox.itemconfig(
            idx,
            fg="#7CFC90" if a['situacao'] == "Aprovado" else "#FF7A7A"
        )

def limpar_campos():
    for e in (entry_nome, entry_disciplina, entry_nota, entry_faltas):
        e.delete(0, tk.END)

def adicionar_aluno():
    nome = entry_nome.get()
    disciplina = entry_disciplina.get()
    try:
        nota = float(entry_nota.get())
        faltas = int(entry_faltas.get())
    except:
        messagebox.showerror("Erro", "Nota ou faltas inválidas.")
        return

    if not validar_texto(nome):
        messagebox.showerror("Erro", "Nome não pode conter números ou caracteres especiais!")
        return

    if not validar_texto(disciplina):
        messagebox.showerror("Erro", "Disciplina não pode conter números ou caracteres especiais!")
        return

    if not validar_nota(nota):
        messagebox.showerror("Erro", "A nota deve estar entre 0 e 20.")
        return

    if not validar_faltas(faltas):
        messagebox.showerror("Erro", f"As faltas devem estar entre {FALTAS_MIN} e {FALTAS_MAX}.")
        return

    turma.append({
        "nome": nome,
        "disciplina": disciplina,
        "nota": nota,
        "faltas": faltas,
        "situacao": calcular_situacao(nota, faltas)
    })

    atualizar_lista()
    limpar_campos()

def editar_aluno(event=None):
    if not listbox.curselection():
        return

    i = listbox.curselection()[0]
    aluno = turma[i]

    novo_nome = simpledialog.askstring("Editar", "Nome:", initialvalue=aluno['nome'])
    if novo_nome:
        if not validar_texto(novo_nome):
            messagebox.showerror("Erro", "Nome não pode conter números ou caracteres especiais!")
            return
        aluno['nome'] = novo_nome

    nova_disciplina = simpledialog.askstring("Editar", "Disciplina:", initialvalue=aluno['disciplina'])
    if nova_disciplina:
        if not validar_texto(nova_disciplina):
            messagebox.showerror("Erro", "Disciplina não pode conter números ou caracteres especiais!")
            return
        aluno['disciplina'] = nova_disciplina

    try:
        nova_nota = float(simpledialog.askstring("Editar", "Nota (0–20):", initialvalue=str(aluno['nota'])))
        if not validar_nota(nova_nota):
            messagebox.showerror("Erro", "A nota deve estar entre 0 e 20.")
            return
        aluno['nota'] = nova_nota
    except:
        pass

    try:
        novas_faltas = int(simpledialog.askstring("Editar", f"Faltas ({FALTAS_MIN}-{FALTAS_MAX}):", initialvalue=str(aluno['faltas'])))
        if not validar_faltas(novas_faltas):
            messagebox.showerror("Erro", f"As faltas devem estar entre {FALTAS_MIN} e {FALTAS_MAX}.")
            return
        aluno['faltas'] = novas_faltas
    except:
        pass

    aluno['situacao'] = calcular_situacao(aluno['nota'], aluno['faltas'])
    atualizar_lista()

def remover_aluno():
    if not listbox.curselection():
        return
    turma.pop(listbox.curselection()[0])
    atualizar_lista()

def limpar_turma():
    if messagebox.askyesno("Confirmar", "Apagar TODOS os alunos?"):
        turma.clear()
        atualizar_lista()

# ---------- Organização ----------
def organizar():
    win = tk.Toplevel(janela)
    win.title("Organizar")
    win.geometry("420x260")
    win.configure(bg=bg)

    def ordenar(chave):
        if chave == "nome":
            turma.sort(key=lambda a: a['nome'].lower())
        elif chave == "nota":
            turma.sort(key=lambda a: a['nota'], reverse=True)
        elif chave == "faltas":
            turma.sort(key=lambda a: a['faltas'])
        atualizar_lista()
        win.destroy()

    tk.Label(win, text="Organizar por",
             font=("Arial",18,"bold"), bg=bg, fg=fg).pack(pady=20)

    for t,c in [("🔤 Nome","nome"),("📊 Nota","nota"),("🚫 Faltas","faltas")]:
        tk.Button(win,text=t,command=lambda x=c:ordenar(x),
                  bg=btn_bg,fg="white",font=("Arial",14),
                  width=22,relief="flat",pady=6).pack(pady=6)

# ---------- Estatísticas ----------
def estatisticas():
    total = len(turma)
    aprovados = sum(1 for a in turma if a['situacao']=="Aprovado")

    win = tk.Toplevel(janela)
    win.title("Estatísticas")
    win.geometry("420x320")
    win.configure(bg=bg)

    tk.Label(win,text="📊 Estatísticas",
             font=("Arial",20,"bold"),bg=bg,fg=fg).pack(pady=20)

    for txt in [
        f"👥 Total: {total}",
        f"✅ Aprovados: {aprovados}",
        f"❌ Reprovados: {total-aprovados}"
    ]:
        tk.Label(win,text=txt,font=("Arial",14),
                 bg=bg,fg=fg).pack(pady=6)

# ---------- Filtro ----------
def set_filtro(v):
    global filtro_atual
    filtro_atual = v
    atualizar_lista()

# ---------- Interface ----------
janela = tk.Tk()
janela.title("Gestor de Turma")
janela.geometry("950x720")

bg="#1e1e1e"
fg="white"
entry_bg="#2d2d2d"
btn_bg="#3a3a3a"
border="#555555"

janela.configure(bg=bg)

tk.Label(janela,text="Gestor de Turma",
         font=("Arial",26,"bold"),bg=bg,fg=fg).pack(pady=15)

# ---------- Form ----------
frame_form = tk.LabelFrame(janela,text=" Dados do Aluno ",
                           bg=bg,fg=fg,font=("Arial",14))
frame_form.pack(pady=10)

def criar_label(t,r):
    tk.Label(frame_form,text=t,font=("Arial",14),
             bg=bg,fg=fg).grid(row=r,column=0,padx=10,pady=8,sticky="e")

def criar_entry(r):
    e=tk.Entry(frame_form,width=40,font=("Arial",14),
               bg=entry_bg,fg=fg,insertbackground=fg,
               relief="solid",bd=1,
               highlightthickness=1,highlightbackground=border)
    e.grid(row=r,column=1,padx=10,pady=8)
    return e

criar_label("Nome:",0); entry_nome=criar_entry(0)
criar_label("Disciplina:",1); entry_disciplina=criar_entry(1)
criar_label("Nota (0–20):",2); entry_nota=criar_entry(2)
criar_label(f"Faltas ({FALTAS_MIN}-{FALTAS_MAX}):",3); entry_faltas=criar_entry(3)

# ---------- Botões ----------
frame_btn=tk.Frame(janela,bg=bg)
frame_btn.pack(pady=20)

def botao(t,c,col,row):
    tk.Button(frame_btn,text=t,command=c,bg=btn_bg,fg="white",
              font=("Arial",13),width=18,
              relief="flat",pady=6
    ).grid(row=row,column=col,padx=6,pady=6)

botao("Adicionar",adicionar_aluno,0,0)
botao("Editar",editar_aluno,1,0)
botao("Remover",remover_aluno,2,0)

botao("Organizar",organizar,0,1)
botao("Estatísticas",estatisticas,1,1)
botao("Limpar Turma",limpar_turma,2,1)

# ---------- Filtro ----------
frame_filtro=tk.Frame(janela,bg=bg)
frame_filtro.pack()

for t in ["Todos","Aprovados","Reprovados"]:
    tk.Button(frame_filtro,text=t,
              command=lambda x=t:set_filtro(x),
              bg=btn_bg,fg="white",
              font=("Arial",12),
              relief="flat",width=14
    ).pack(side="left",padx=5)

# ---------- Lista ----------
listbox=tk.Listbox(
    janela,width=90,height=8,font=("Arial",12),
    bg=entry_bg,fg=fg,
    relief="solid",bd=1,
    highlightthickness=1,highlightbackground=border,
    selectbackground="#555555"
)
listbox.pack(pady=15)
listbox.bind("<Double-Button-1>", editar_aluno)

janela.mainloop()
