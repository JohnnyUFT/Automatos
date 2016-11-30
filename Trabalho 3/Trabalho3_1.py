#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: November 2016

"""
from lib2to3.pgen2.tokenize import Whitespace

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import string
import PIL
from PIL import ImageTk, Image
from tkinter import PhotoImage
import sys # desnecessário, talvez?
from tkinter import messagebox
from tkinter import ttk

def obterAlfbabeto():
    alfabeto =   ent1.get()
    q0(alfabeto)# começa a verificar o formalismo para o conjunto dado
    qtdEstados = int(ent2.get())
    # de acordo com qtsEstados, criar a lista para escolha do(s) estado(s) final(s):
    preencheListaEstados(qtdEstados)
    estInicial = ent3.get()
    estFinal =   cbb1.get()# corrigir
    print(alfabeto,qtdEstados,estInicial,estFinal)

def obterPalavra():
    palavra = ent5.get()
    print(palavra)
    analisaPalavra(palavra)

def q0(alfabeto):
    """
    Implementa toda lógica necessária ao controle do estado inicial 'q0'.

    O primeiro símbolo do alfabeto deve ser, necessariamente
    um 'abre-chaves', do contrário, a entrada já é considerada errada.
    :param alfabeto: str
    :return: void
    """
    i = 0  # marca índice da string (cadeia de simbolos da fita)
    print("i em q0: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if ((alfabeto[i] == '{') and len(alfabeto) > 1):
        q1(alfabeto, i + 1)
    else:
        qErro()


def q1(alfabeto, i):
    """
    Implementação do estado 'q1'.

    Se o alfabeto informado estiver correto,
    o símbolo informado aqui, deverá ser exclusivamente alfanumérico.
    :param alfabeto: str
    :param i: int
    :return: void
    """
    print("i em q1: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if i <= len(alfabeto)-2:
        if verAlfaNumerico(alfabeto, i):
            q2(alfabeto, i+1)
        else:
            qErro()
    else:
        qErro()


def q2(alfabeto, i):
    """
    Implementação das regras definidas para estado 'q2'.

    Se o alfabeto informado estiver correto, o símbolo processado aqui
    deverá ser uma vírgula.
    :param alfabeto: str
    :param i: int
    :return: void
    """
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
    """
    Implementação das regras definidas para estado 'q3'.

    Este é o estado de aceitação. É nele que está contido o teste
    para confirmar se o alfabeto informado é aceito ou rejeitado.
    :param alfabeto: str
    :param i: int
    :return: void
    """
    print("i em q3: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if i == len(alfabeto)-1:
        messagebox.showinfo("Informação", "Alfabeto aceito!")
        # chamar o que agora?
        # tem que chamar algo aqui
        # para continuar o programa
    else:
        qErro()


def qErro():
    """
    Estado de erro.

    Não faz nada a não ser, mostrar esta mensagem na tela e interromper
    o processo de transições entre os estados.
    :return: void
    """
    messagebox.showerror("Erro", "Alfabeto rejeitado.")

def verAlfaNumerico(alfabeto, i):
    """
    Verifica se o símbolo recebido é alfanumérico.

    Este método testa se o símbolo está entre A,...,Z
                                           ou a,...,z
                                           ou 0,...,9
    :param alfabeto: str
    :param i: int
    :return: boolean
    """
    #print("Em verAlphaNumeric: %s, %d "%(alfabeto, i))
    if (ord(alfabeto[i]) >= 65 and ord(alfabeto[i]) <= 90) \
            or (ord(alfabeto[i]) >= 97 and ord(alfabeto[i]) <= 122) \
            or (ord(alfabeto[i]) >= 48 and ord(alfabeto[i]) <= 57):
        return True
    return False

def analisaPalavra(palavra):
    """
    Realiza última verificação para atestar se a palavra foi aceita, ou não.
    :param palavra:
    :return: void
    """
    messagebox.showinfo("Parabéns", "Palavra foi aceita!")

def preencheListaEstados(qtdEstados):
    for i in range(qtdEstados):
        estado = 'q'+str(i)
        print(estado, type(estado))
        cbb1['values'] = estado


#  AQUI INICIA A IMPLEMENTAÇÃO DA PARTE GRÁFICA
Janela = tk.Tk()  # instancia da Janela Principal (mainWindow)
"""
Posteriomente, separar este método em uma classe separada
e trabalhar com implementação OO e GUI.
"""

values = StringVar()

#  principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="white")
frame2 = Frame(Janela, height=100, bg="")
frame3 = Frame(Janela, height=100, bg="")
frame4 = Frame(Janela, height=100, bg="white")
frame5 = Frame(Janela, height=100, bg="")
frame6 = Frame(Janela, width=30, bg="")# serve apenas para definir uma margem
frame7 = Frame(Janela, width=30, bg="")# serve apenas para definir uma margem

# empacotamento e disposição em que aparecem na tela
frame1.pack(side=TOP, fill=X)
frame6.pack(side=LEFT, fill=Y)# margem esquerda
frame7.pack(side=RIGHT, fill=Y)# margem direita
frame2.pack(side=TOP, fill=X)
frame3.pack(side=TOP, fill=X)
frame4.pack(side=TOP, fill=X)

#  configuração de fonte, permanente para labels e outros
fonte1 = ('Ubuntu', '10')
# elementos contidos no frame1
lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
            font=('Ubuntu', '12', 'bold'), height=6, bg="white")
logo = Image.open("uft4.jpg")
photo1 = ImageTk.PhotoImage(logo)
lb11 = Label(frame1, image=photo1)
lb1.grid(row=0, column=1, stick=W)
lb11.grid(row=0, column=0, stick=W)

#  elementos contidos no frame2
lb2 = Label(frame2, text="Alfabeto: ", font=fonte1)
ent1 = Entry(frame2, text="", font=fonte1)
lb3 = Label(frame2, text="Qtd estados: ", font=fonte1)
ent2 = Entry(frame2, text="", font=fonte1)
bt1 = Button(frame2, text="Ok", font=fonte1)
lb4 = Label(frame2, text="Estado Inicial: ", font=fonte1)
ent3 = Entry(frame2, text="0", font=fonte1)
ent3.insert(0, 'q0')
lb5 = Label(frame2, text="Estado Final: ", font=fonte1)
cbb1 = ttk.Combobox(frame2, textvariable=values, state='readonly')# adicionar propriedades?
values = ['']# é preciso preencher isso aqui

bt2 = Button(frame2, text="Ok ", font=fonte1, command=obterAlfbabeto)

# elementos contidos no frame3
lb6 = Label(frame3, text="Função de Transição: ", font=fonte1)
lbox1 = Listbox(frame3, height=7)# trocar por treeview
lb8 = Label(frame3, text="Palavra informada:")
ent5 = Entry(frame3, text="", font=fonte1)
btn2 = Button(frame3, text="Inserir e Processar", command=obterPalavra)

# frame4 possui apenas uma imagem (caráter decorativo)
image = Image.open("cinema.png")
photo = ImageTk.PhotoImage(image)
lb9 = Label(frame4, image=photo, bg="white")

# elementos contidos no frame5
# refazer isso aqui
lb10 = Label(frame5, text="Palavra Rejeitada!") # setar o texto conforme resultado da análise

#  disposição dos widgets do frame2
lb2.grid(row=0, column=0, stick=W)
ent1.grid(row=1, column=0, stick=W)
lb3.grid(row=0, column=1, stick=W)
ent2.grid(row=1, column=1, stick=W)
bt1.grid(row=1, column=2, stick=W)
lb4.grid(row=0, column=3, stick=W)
ent3.grid(row=1, column=3, stick=W)
lb5.grid(row=0, column=4, stick=W)
cbb1.grid(row=1, column=4, stick=W)
bt1.grid(row=1, column=5, stick=W)

# disposição dos widgets do frame3
lb6.grid(row=0, column=0, stick=W)
lbox1.grid(row=1, column=0, stick=W)
lb8.grid(row=2, column=0, stick=W)
ent5.grid(row=3, column=0, stick=W)
btn2.grid(row=3, column=1, stick=W)

# disposição dos widgets do frame4
#lb9.grid(row=0, column=0, stick=E+W)# imagem que será mostrada no frame
lb9.pack()

# disposição dos widgets do frame5
lb10.grid(row=0, column=0, stick=E+W)# apenas para teste, remover depois

Janela.title("Linguagens Formais & Autômatos - Trabalho #3")
#  Largura x Altura + Esquerda + Topo
Janela.geometry("750x550+300+100")
Janela.mainloop()
