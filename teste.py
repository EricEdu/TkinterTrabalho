import tkinter
from tkinter import OptionMenu, StringVar, messagebox as mb
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


# Cria conexão
connection = sqlite3.connect("teste.db")

# Cria o cursor e cria a tabela
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT)")

def VerificarCPF(CPF):
    # CPF deve ser na forma "123.456.789-10"
    if len(CPF) != 14:
        return False
    partes = CPF.split(".")
    if len(partes) != 3:
        return False
    for parte in partes[:2]:
        if len(parte) != 3 or not parte.isdigit():
            return False
    parte3 = partes[2].split("-")
    if len(parte3) != 2 or len(parte3[0]) != 3 or not parte3[0].isdigit() or len(parte3[1]) != 2 or not parte3[1].isdigit():
        return False
    return True

def inserevalores(nome, cpf, estado):
    # Insere linha na tabela
    cursor.execute("INSERT INTO Tabela1 (nome, cpf, estado) VALUES (?, ?, ?)", (nome, cpf, estado))
    connection.commit()  # Salva as alterações no banco de dados

def pegavalores():
    # Pega valores da tabela
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def carregar_estados():
    # Lê os estados do arquivo config.txt
    with open('config.txt', 'r') as file:
        conteudo = file.read()
        estados = [estado.strip() for estado in conteudo.split(';')]
    return estados

def salvar_dados():
    nome = e1.get()
    cpf = e2.get()
    estado = estado_var.get()
    if VerificarCPF(cpf) and estado in estados:
        inserevalores(nome, cpf, estado)
        print("Dados salvos com sucesso")
    else:
        if not VerificarCPF(cpf):
            print("CPF inválido")
        if estado not in estados:
            print("Estado inválido")

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

    global estados  # Definindo estados como global para ser acessível na função salvar_dados
    estados = carregar_estados()
    global estado_var  # Definindo estado_var como global para ser acessível na função salvar_dados
    estado_var = StringVar(root)
    estado_var.set(estados[0])  # Define um estado padrão

    option_menu = OptionMenu(root, estado_var, *estados)
    option_menu.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = salvar_dados  # Associando a função salvar_dados ao botão
    test2.pack()

    root.iconify() # Minimiza a tela
    root.update()
    root.deiconify() # Maximiza a tela
    root.mainloop()  # Loop principal, impede o código de seguir e permite capturar inputs

Main()