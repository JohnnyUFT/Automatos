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
from  PIL  import  Image # desnecessário, talvez?
import sys

#  AQUI INICIA A IMPLEMENTAÇÃO DA PARTE GRÁFICA
Janela = tk.Tk()  # instancia da Janela Principal (mainWindow)
"""
Posteriomente, separar este método em uma classe separada
e trabalhar com implementação OO e GUI.
"""
#  principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="")
frame2 = Frame(Janela, height=100, bg="")
frame3 = Frame(Janela, height=100, bg="")
frame4 = Frame(Janela, height=100, bg="")
frame5 = Frame(Janela, height=100, bg="")
frame6 = Frame(Janela, width=30, bg="green")# serve apenas para definir uma margem
frame7 = Frame(Janela, width=30, bg="green")# serve apenas para definir uma margem

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
            font=('Ubuntu', '12', 'bold'), height=6) # , bg="white"
lb1.pack()

#  elementos contidos no frame2
lb2 = Label(frame2, text="Alfabeto: ", font=fonte1)
ent1 = Entry(frame2, text="", font=fonte1)
bt1 = Button(frame2, text="Ok ", font=fonte1)
lb3 = Label(frame2, text="Qtd estados: ", font=fonte1)
ent2 = Entry(frame2, text="", font=fonte1)
lb4 = Label(frame2, text="Estado Inicial: ", font=fonte1)
ent3 = Entry(frame2, text="", font=fonte1)# substituir por ComboBox
lb5 = Label(frame2, text="Estado Final: ", font=fonte1)
ent4 = Entry(frame2, text="", font=fonte1)# substituir por ComboBox

# elementos contidos no frame3
lb6 = Label(frame3, text="Função de Transição: ", font=fonte1)
lbox1 = Listbox(frame3, height=7)# trocar por treeview
lb8 = Label(frame3, text="Palavra informada:")
ent5 = Entry(frame3, text="", font=fonte1)
btn2 = Button(frame3, text="Inserir e Processar")

# frame4 possui apenas uma imagem (caráter decorativo)
image = Image.open("content.gif")
photo = ImageTk.PhotoImage(image)
lb9 = Label(frame4, image=photo)

# elementos contidos no frame5
# refazer isso aqui
lb10 = Label(frame5, text="Palavra Rejeitada!") # mudar o tipo do widget?

#  disposição dos widgets do frame2
lb2.grid(row=0, column=0, stick=W)
ent1.grid(row=1, column=0, stick=W)
bt1.grid(row=1, column=1, stick=W)
lb3.grid(row=0, column=2, stick=W)
ent2.grid(row=1, column=2, stick=W)
lb4.grid(row=0, column=3, stick=W)
ent3.grid(row=1, column=3, stick=W)
lb5.grid(row=0, column=4, stick=W)
ent4.grid(row=1, column=4, stick=W)

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
Janela.geometry("700x510+300+100")
Janela.mainloop()
