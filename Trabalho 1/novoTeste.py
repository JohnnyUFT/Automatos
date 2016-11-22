#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
author: Johnny Pereira
email: johnnyuft@gmail.com
last modified: September 2016

"""

from Tkinter import *
import Tkinter as tk

Janela = tk.Tk() # instancia da Janela Principal (mainWindow)

# principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="yellow")
frame2 = Frame(Janela, width=100,  bg="") # bg="" é desnecessário aqui
frame3 = Frame(Janela, height=100, bg="pink") # height é desnecessário aqui
frame4 = Frame(Janela, width=100,  bg="")

frame1.pack(side=TOP, fill=X)
frame2.pack(side=LEFT, fill=Y)
frame4.pack(side=RIGHT, fill=Y)
frame3.pack(fill=BOTH)

# configuração de fonte, permanente para labels e outros
fonte1 = ('Verdana', '10')

lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
            font=('Ubuntu', '12', 'bold'), height=6, bg="white")
lb1.pack()

# elementos contidos no frame 3 (o do meio)
lb3 = Label(frame3, text="Entrada (alfabeto): ", font=fonte1)
ed1 = Entry(frame3, text="", font=fonte1)
bt1 = Button(frame3, text="Inserir", font=fonte1)
lb4 = Label(frame3, text="Lista de alfabetos: ", font=fonte1)
lbox1 = Listbox(frame3, height=7)
bt2 = Button(frame3, text="Unir alfabetos ", font=fonte1)
lb5 = Label(frame3, text="Palavra: ", font=fonte1)
ed2 = Entry(frame3, text="", font=fonte1)
bt3 = Button(frame3, text="Verificar", font=fonte1)
bt4 = Button(frame3, text="Prefixos", font=fonte1)
bt5 = Button(frame3, text="Sufixos", font=fonte1)
bt6 = Button(frame3, text="Subpalavras", font=fonte1)

# disposição de todos os widgets do frame (conteiner) nº 3 (odo meio)
lb3.grid(row=0, column=0, stick=W)
ed1.grid(row=1, column=0)
bt1.grid(row=1, column=1)
lb4.grid(row=2, column=0, stick=W)
lbox1.grid(row=3, column=0)
bt2.grid(row=4, column=0) # ATENÇÃO!!! e as linhas do listbox? resp: não interferem nesta "contagem"
lb5.grid(row=5, column=0, stick=W)
ed2.grid(row=6, column=0)
bt3.grid(row=6, column=1)
bt4.grid(row=7, column=0, stick=W) # cuidar com as disposições desttes botões
bt5.grid(row=7, column=1)
bt6.grid(row=7, column=2, stick=E)


Janela.title("Linguagens Formais & Autômatos ")
# Largura x Altura + Esquerda + Topo
Janela.geometry("560x510+300+100")
Janela.mainloop()