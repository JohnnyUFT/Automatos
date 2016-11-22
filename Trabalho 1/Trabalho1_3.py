#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: November 2016

"""
from lib2to3.pgen2.tokenize import Whitespace

from Tkinter import *
import Tkinter as tk
import tkMessageBox
import string


#  Definições de funções e métodos a serem usados ao longo do programa
#  Transferir esta coleção de métodos para outro arquivo, desta forma fica mais organizado
#  Dividir tudo em funções pequenas, que executam passos simples de cada vez

#  MÉTODOS A SEREM IMPLEMENTADOS NUMA CLASSE BEM DEFINIDA (Object Oriented)

#  método que recebe os alfabetos inseridos no "Entry"

#  método que abstrai/simula o autômato

def automato():
    alfabeto1 = removeSpace() # remove os espaços em branco
    repetidos = verRepeticao(alfabeto1) # verifica repetição de símbolos
    if(not repetidos):
        q0(alfabeto1)  # começa pelo q0() que é o estado inicial
    else:
        qErro()

def obterAlfabeto():
    print(ed1.get())  # teste dispensável
    alfabeto = ed1.get()  # guarda conteúdo lido numa string
    return alfabeto


#  esboço da função de transição
def q0(alfabeto):
    i = 0  # marca índice da string lida (cadeia de simbolos da fita)
    print("i em q0: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if ((alfabeto[i] == '{') and len(alfabeto) > 1):
        q1(alfabeto, i + 1)
    else:
        qErro()


def q1(alfabeto, i):
    print("i em q1: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if i <= len(alfabeto)-2:
        if verAlphaNumeric(alfabeto, i):
            q2(alfabeto, i+1)
        else:
            qErro()
    else:
        qErro()


def q2(alfabeto, i):
    print("i em q2: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if i <= len(alfabeto)-1:
        if alfabeto[i] == ',' and i < len(alfabeto)-1:
            q1(alfabeto, i + 1)
        elif alfabeto[i] == '}' and i == len(alfabeto)-1: # não há mais simbolos na 'fita'
            q3(alfabeto, i) # chegamos ao último símbolo e este é uma vírgula
        else:
            qErro()
    else:
        qErro()


def q3(alfabeto, i):
    print("i em q3: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if i == len(alfabeto)-1:  # teste redundante, .: desnecessário
        tkMessageBox.showinfo("Informação", "Alfabeto aceito!")
        # empilhando alfabeto dentro do listbox:
        lbox1.insert(END, alfabeto)
        #text1.insert(END, alfabeto)
    else:
        qErro()


def qErro():
    tkMessageBox.showerror("Erro", "Faltam ou sobram parâmetros")


#  método que remove os espaços
def removeSpace():
    alfabeto = obterAlfabeto().replace(" ", "")
    return alfabeto


#  método que verifica se há repetição de símbolos no alfabeto
def verRepeticao(alfabeto):
    tam = len(alfabeto)-1
    for i in range(tam):
        for j in range(i+1,tam,1):
            if(alfabeto[i] == alfabeto[j] and alfabeto[i] != ','):
                # tratar símbolos repetidos
                print("Símbolos repetidos: %s"%alfabeto[i])
                return True # encontrou símbolos repetidos
    return False # não encontrou repetição


#  método que testa se o símbolo está entre A,...,Z ou a,...,z ou 0,...,9
def verAlphaNumeric(alfabeto, i):
    if (ord(alfabeto[i]) >= 65 and ord(alfabeto[i]) <= 90) \
            or (ord(alfabeto[i]) >= 97 and ord(alfabeto[i]) <= 122) \
            or (ord(alfabeto[i]) >= 48 and ord(alfabeto[i]) <= 57):
        return True
    return False


# método que trabalha a união dos alfabetos
# removendo os símbolos repetidos
def unirAlfabetos():
    pass



#  AQUI INICIA A IMPLEMENTAÇÃO DA PARTE GRÁFICA
#  seperar da parte de negócios (este deve ser uma classe bem definida)
Janela = tk.Tk()  # instancia da Janela Principal (mainWindow)

#  principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="")
frame2 = Frame(Janela, width=100, bg="")  # bg="" é desnecessário aqui
frame3 = Frame(Janela, height=100, bg="")  # height é desnecessário aqui
frame4 = Frame(Janela, width=100, bg="")

frame1.pack(side=TOP, fill=X)
frame2.pack(side=LEFT, fill=Y)
frame4.pack(side=RIGHT, fill=Y)
frame3.pack(fill=BOTH)

#  configuração de fonte, permanente para labels e outros
fonte1 = ('Ubuntu', '10')

lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
            font=('Ubuntu', '12', 'bold'), height=6) # , bg="white"
lb1.pack()

#  elementos contidos no frame 3 (o do meio)
lb3 = Label(frame3, text="Entrada (alfabeto): ", font=fonte1)
ed1 = Entry(frame3, text="", font=fonte1)  # trabalhar a função obterAlfabeto - em outro arquivo, de preferência
bt1 = Button(frame3, text="Inserir", font=fonte1, command=automato)
lb4 = Label(frame3, text="Lista de alfabetos: ", font=fonte1)
lbox1 = Listbox(frame3, height=7)
#text1 = Text(frame3, height=7)
bt2 = Button(frame3, text="Unir alfabetos ", font=fonte1, command=unirAlfabetos)
lb5 = Label(frame3, text="Palavra: ", font=fonte1)
ed2 = Entry(frame3, text="", font=fonte1)
bt3 = Button(frame3, text="Verificar", font=fonte1)
bt4 = Button(frame3, text="Prefixos", font=fonte1)
bt5 = Button(frame3, text="Sufixos", font=fonte1)
bt6 = Button(frame3, text="Subpalavras", font=fonte1)

#  disposição de todos os widgets do frame (conteiner) nº 3 (odo meio)
lb3.grid(row=0, column=0, stick=W)
ed1.grid(row=1, column=0)
bt1.grid(row=1, column=1)
lb4.grid(row=2, column=0, stick=W)
lbox1.grid(row=3, column=0)
#text1.grid(row=3, column=0)
bt2.grid(row=4, column=0)  # ATENÇÃO!!! e as linhas do listbox? resp: não interferem nesta "contagem"
lb5.grid(row=5, column=0, stick=W)
ed2.grid(row=6, column=0)
bt3.grid(row=6, column=1)
bt4.grid(row=7, column=0, stick=W)  # cuidar com as disposições destes botões
bt5.grid(row=7, column=1)
bt6.grid(row=7, column=2, stick=E)

Janela.title("Linguagens Formais & Autômatos ")
#  Largura x Altura + Esquerda + Topo
Janela.geometry("560x510+300+100")
Janela.mainloop()
