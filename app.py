import tkinter as tk
from tkinter import messagebox
import os

def valida_cnpj(cnpj):
    cnpj = [int(d) for d in cnpj if d.isdigit()]
    if len(cnpj) != 14:
        return False
    pesos1, pesos2 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2], [6] + [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(12, 14):
        soma = sum(cnpj[num] * (pesos1 if i == 12 else pesos2)[num] for num in range(0, i))
        dv = 0 if soma % 11 < 2 else 11 - soma % 11
        if dv != cnpj[i]:
            return False
    return True

def valida_cpf(cpf):
    cpf = [int(d) for d in cpf if d.isdigit()]
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    for i in range(9, 11):
        soma = sum(cpf[num] * ((i + 1) - num) for num in range(0, i))
        dv = (soma * 10) % 11
        if dv == 10:
            dv = 0
        if dv != cpf[i]:
            return False
    return True

def valida_dv(documento, tipo):
    return valida_cnpj(documento) if tipo == "CNPJ" else valida_cpf(documento)

def salvar_em_arquivo(dados):
    with open("etiquetas.txt", "a") as f:
        for registro in dados:
            etiqueta = registro[0]
            documento = registro[1] if registro[1] else ""
            nome = registro[2] if registro[2] else ""
            status_dv = registro[3] if len(registro) > 3 and registro[3] else ""
            linha = f"{etiqueta};{documento};{nome}{(';' + status_dv) if status_dv else ''}\n"
            f.write(linha)

def renomear_arquivo_etiqueta(numero_etiqueta):
    novo_nome = f"RF{numero_etiqueta}.txt"
    if os.path.exists("etiquetas.txt"):
        os.rename("etiquetas.txt", novo_nome)
    else:
        with open(novo_nome, 'w') as f:
            pass

def exibir_mensagem_temporaria(mensagem, cor="green"):
    label_temp = tk.Label(root, text=mensagem, font=("Arial", 22), bg="#f0f0f0", fg=cor)
    label_temp.grid(row=0, column=0, pady=10, padx=10)
    root.after(1000, label_temp.destroy)

def atualizar_lista_temp(registro):
    lista_temp.insert(tk.END, f"Etiqueta: {registro[0]}")
    lista_temp.insert(tk.END, f"Documento: {registro[1] if registro[1] else 'N/A'}")
    lista_temp.insert(tk.END, f"Nome: {registro[2] if registro[2] else 'N/A'}")
    if len(registro) > 3 and registro[3]:
        lista_temp.insert(tk.END, f"Status DV: {registro[3]}")
    lista_temp.insert(tk.END, "-" * 40)

def limpar_lista_temp():
    lista_temp.delete(0, tk.END)

def proximo_registro():
    if botao_concluido["state"] != tk.DISABLED:
        messagebox.showerror("Erro", "Aperte em concluído para prosseguir.")
        return

    etiqueta = entrada_etiqueta.get()
    if not etiqueta.isdigit() or len(etiqueta) != 9:
        messagebox.showerror("Erro", "O número da etiqueta deve ter exatamente 9 dígitos.")
        return

    etiqueta = "RF" + etiqueta
    documento = entrada_documento.get().replace(".", "").replace("/", "").replace("-", "").replace(" ", "")
    nome = entrada_nome.get().strip().upper() or ""
    tipo_documento = "CNPJ" if var_tipo.get() == 1 else "CPF"

    status_dv = ""
    if documento and not valida_dv(documento, tipo_documento):
        resposta = messagebox.askquestion(
            "Aviso", f"O DV do {tipo_documento} está errado. Deseja corrigir?", icon="warning"
        )
        if resposta == "yes":
            entrada_documento.focus()
            return
        else:
            status_dv = "(DV Errado)"

    if not documento and not nome:
        messagebox.showerror("Erro", "Você deve preencher pelo menos o NOME ou o DOCUMENTO!")
        return

    registro = [etiqueta, documento if documento else "", nome, status_dv]
    salvar_em_arquivo([registro])
    exibir_mensagem_temporaria("Registro salvo!", "green")
    atualizar_lista_temp(registro)
    entrada_documento.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_documento.focus()

def reiniciar_etiqueta():
    numero_etiqueta = entrada_etiqueta.get()
    if not numero_etiqueta.isdigit() or len(numero_etiqueta) != 9:
        messagebox.showerror("Erro", "O número da etiqueta deve ter exatamente 9 dígitos.")
        return

    renomear_arquivo_etiqueta(numero_etiqueta)
    entrada_documento.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_etiqueta.config(state=tk.NORMAL)
    entrada_etiqueta.focus()
    botao_concluido.config(state=tk.NORMAL)
    botao_proximo_registro.config(state=tk.DISABLED)
    entrada_etiqueta.delete(0, tk.END)
    limpar_lista_temp()
    messagebox.showinfo("Etiqueta", "Etiqueta criada com sucesso!")

def concluir():
    etiqueta = entrada_etiqueta.get()
    if not etiqueta.isdigit() or len(etiqueta) != 9:
        messagebox.showerror("Erro", "O número da etiqueta deve ter exatamente 9 dígitos.")
        return
    entrada_etiqueta.config(state=tk.DISABLED)
    botao_concluido.config(state=tk.DISABLED)
    botao_proximo_registro.config(state=tk.NORMAL)

def habilitar_edicao_etiqueta():
    entrada_etiqueta.config(state=tk.NORMAL)
    botao_concluido.config(state=tk.NORMAL)
    botao_proximo_registro.config(state=tk.DISABLED)
    entrada_etiqueta.focus()

def validar_entrada(apenas_numeros):
    return apenas_numeros.isdigit() or apenas_numeros == ""

def limitar_caracteres(event, max_length, entry_field):
    if len(entry_field.get()) >= max_length and event.keysym != "BackSpace":
        return "break"

def mover_foco(event, proximo_widget):
    proximo_widget.focus()

def concluir_enter(event=None):
    concluir()

#Atalhos

# Atalhos de teclado
def atalho_f1(event):
    var_tipo.set(1)


def atalho_f2(event):
    var_tipo.set(2)

def atalho_f3(event):
    botao_editar_etiqueta.invoke()
def atalho_f5(event):
    botao_reiniciar.invoke()

def atalho_f11(event):
    # Verifica se a janela está no modo tela cheia
    if root.attributes('-fullscreen'):
        # Se estiver em tela cheia, volta para o modo janela
        root.attributes('-fullscreen', False)
        root.geometry("800x500")  # Define o tamanho normal da janela
    else:
        # Se não estiver em tela cheia, vai para tela cheia
        root.attributes('-fullscreen', True)

root = tk.Tk()
root.title("Registro de Etiquetas")
root.geometry("800x500")
root.configure(bg="#f0f0f0")
root.attributes('-fullscreen', True)
root.bind("<F1>", atalho_f1)
root.bind("<F2>", atalho_f2)
root.bind("<F3>", atalho_f3)
root.bind("<F5>", atalho_f5)
root.bind("<F11>", atalho_f11)

dados = []

validar_somente_numeros = root.register(validar_entrada)

frame = tk.Frame(root, bg="#e0e0e0")
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

tk.Label(frame, text="Número da ETIQUETA(somente numeros):", font=("Arial", 22), bg="#e0e0e0", fg="#D50000").grid(row=0, column=0, sticky="w", pady=5, padx=10)
entrada_etiqueta = tk.Entry(frame, font=("Arial", 22), validate="key", validatecommand=(validar_somente_numeros, "%P"))
entrada_etiqueta.grid(row=1, column=0, padx=(0,500), pady=5, sticky="w")
entrada_etiqueta.bind("<KeyPress>", lambda event: limitar_caracteres(event, max_length=9, entry_field=entrada_etiqueta))
entrada_etiqueta.bind("<Return>", lambda event: (concluir(), mover_foco(event, entrada_documento)))
botao_concluido = tk.Button(frame, text="Concluído", command=concluir, font=("Arial", 12), bg="#FFD700", fg="#000000", width=15)
botao_concluido.grid(row=1, column=0, padx=10, pady=70)

tk.Label(frame, text="CNPJ/CPF:", font=("Arial", 22), bg="#e0e0e0", fg="#D50000").grid(row=2, column=0, sticky="w", pady=5, padx=10)
entrada_documento = tk.Entry(frame, font=("Arial", 22), validate="key", validatecommand=(validar_somente_numeros, "%P"))
entrada_documento.grid(row=3, column=0, padx=(0,500), pady=20, sticky="w")
entrada_documento.bind("<KeyPress>", lambda event: limitar_caracteres(event, max_length=14, entry_field=entrada_documento))
entrada_documento.bind("<Return>", lambda event: entrada_nome.focus())

var_tipo = tk.IntVar(value=1)
tk.Radiobutton(frame, text="CNPJ", variable=var_tipo, value=1, font=("Arial", 12), bg="#e0e0e0", fg="#D50000").grid(row=3, column=0, padx=(220,300))
tk.Radiobutton(frame, text="CPF", variable=var_tipo, value=2, font=("Arial", 12), bg="#e0e0e0", fg="#D50000").grid(row=3, column=0, padx=(200,100))

tk.Label(frame, text="Nome:", font=("Arial", 22), bg="#e0e0e0", fg="#D50000").grid(row=4, column=0, sticky="w", pady=5, padx=10)
entrada_nome = tk.Entry(frame, font=("Arial", 22), width=40)
entrada_nome.grid(row=5, column=0, columnspan=3, padx=5, pady=15, sticky="w")
entrada_nome.bind("<Return>", lambda event: (mover_foco(event, botao_proximo_registro), botao_proximo_registro.invoke()))

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w")

botao_proximo_registro = tk.Button(button_frame, text="Próximo Registro", command=lambda: [proximo_registro(), entrada_documento.focus()], font=("Arial", 12), bg="#FFD700", fg="#000000", width=15)
botao_proximo_registro.grid(row=0, column=0, padx=10)

botao_editar_etiqueta = tk.Button(button_frame, text="Editar Etiqueta", command=habilitar_edicao_etiqueta, font=("Arial", 12), bg="#FFA500", fg="#000000", width=15)
botao_editar_etiqueta.grid(row=0, column=1, padx=10)

botao_reiniciar = tk.Button(button_frame, text="Próxima ETIQUETA", command=reiniciar_etiqueta, font=("Arial", 12), bg="#D50000", fg="#ffffff", width=15)
botao_reiniciar.grid(row=0, column=2, padx=10)

lista_frame = tk.Frame(root, bg="#f0f0f0")
lista_frame.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

tk.Label(lista_frame, text="Registros Salvos", font=("Arial", 16), bg="#f0f0f0", fg="#000").grid(row=0, column=0, pady=5)
lista_temp = tk.Listbox(lista_frame, font=("Arial", 12), width=40, height=15)
lista_temp.grid(row=1, column=0, pady=5, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
lista_frame.grid_rowconfigure(1, weight=1)

root.mainloop()
