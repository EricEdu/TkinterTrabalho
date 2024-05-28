import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3

#começar com tela com um botão e um entry (nome)- v1
#adicionar mais duas entrys (cpf e estado) e suas labels - v2
#mudar o fundo para uma imagem mais bonita, adicionar readme.txt explicando como usar - v3
#adicionar clicar no botão salva os 3 dados em um sqlite - v4
#Criar uma branch em que le um config.txt com uma lista de 5 estados possiveis separados por pular linha - x1
#Mudar o separador para ; e adicionar mais 5 estados - x2
#Voltar para main, criar outra branch e criar um dropdown com 3 opções (clt, mei, socio) - y1
#Voltar para main, Corrigir o bug da função de cpf - v5
#Merge de x com v - v6
#Adicionar verificação de CPF e de estado, com base na função cpf e na lista de estados .txt antes de adicionar no sqlite v7


import sqlite3
import tkinter
from tkinter import StringVar, OptionMenu

# Cria conexão
connection = sqlite3.connect("teste.db")

# Cria o cursor e cria a tabela
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT, tipo TEXT)")

def VerificarCPF(CPF):
    # CPF deve ser na forma "123.456.789-10"
    for trecho in CPF.split("."):
        if len(trecho) != 3:
            return False
    return True

def inserevalores(nome, cpf, estado, tipo):
    # Insere linha na tabela
    cursor.execute("INSERT INTO Tabela1 (nome, cpf, estado, tipo) VALUES (?, ?, ?, ?)", (nome, cpf, estado, tipo))
    connection.commit()  # Salva as alterações no banco de dados

def pegavalores():
    # Pega valores da tabela
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def salvar_dados():
    nome = e1.get()
    cpf = e2.get()
    estado = e3.get()
    tipo = tipo_var.get()
    if VerificarCPF(cpf):
        inserevalores(nome, cpf, estado, tipo)
        print("Dados salvos com sucesso")
    else:
        print("CPF inválido")

def Main():
    root = tkinter.Tk()
    root.configure(background='red')
    root.title("Trabalho RAD")
    root.resizable(True, True)
    
    label = tkinter.Label(root, text="Nome")
    label.pack()

    global e1  # Definindo e1 como global para ser acessível na função salvar_dados
    e1 = tkinter.Entry(root)
    e1.pack()

    label = tkinter.Label(root, text="CPF")
    label.pack()

    global e2  # Definindo e2 como global para ser acessível na função salvar_dados
    e2 = tkinter.Entry(root)
    e2.pack()

    label = tkinter.Label(root, text="Estado")
    label.pack()

    global e3  # Definindo e3 como global para ser acessível na função salvar_dados
    e3 = tkinter.Entry(root)
    e3.pack()

    label = tkinter.Label(root, text="Tipo")
    label.pack()

    global tipo_var  # Definindo tipo_var como global para ser acessível na função salvar_dados
    tipo_var = StringVar(root)
    tipo_var.set("CLT")  # Define uma opção padrão

    tipo_options = ["CLT", "MEI", "Sócio"]
    tipo_menu = OptionMenu(root, tipo_var, *tipo_options)
    tipo_menu.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = salvar_dados  # Associando a função salvar_dados ao botão
    test2.pack()

    root.iconify() # Minimiza a tela
    root.update()
    root.deiconify() # Maximiza a tela
    root.mainloop()  # Loop principal, impede o código de seguir e permite capturar inputs

Main()
