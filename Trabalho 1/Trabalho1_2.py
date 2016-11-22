#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
author: Johnny Pereira
email: johnnyuft@gmail.com
last modified: August 2016

"""
import os

from Tkinter import *
from PIL import Image, ImageTk


class Janela:
    def __init__(self, instancia_Tk):

        # criando titulo da aplicacao
        self.frame = Frame(instancia_Tk)
        self.frame.pack()

        im = PhotoImage(file='content2.gif') # encapsulando a imagem
        self.imagem = Label(self.frame, image=im) # colocando-a no label
        self.imagem.pack()

        self.titulo = Label(self.frame, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
                            font=('Verdana', '13', 'bold'))
        self.titulo.pack()

        # conteiners para receber e distribuir informacoes na tela
        self.container1 = Frame(instancia_Tk, pady=10)
        self.container2 = Frame(instancia_Tk)
        self.container3 = Frame(instancia_Tk)
        self.container4 = Frame(instancia_Tk)
        # self.container5 = Frame(instancia_Tk)
        # self.container6 = Frame(instancia_Tk)

        # estes conteiners sao empacotados/encapsulados com o gerenciador de geometria '.pack(side=TOP)'
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()
        self.container4.pack()
        # self.container5.pack()
        # self.container6.pack()

        # configuração de fonte, permanente para labels e outros
        fonte1 = ('Verdana', '10')

        # label pedindo entrada de simbolos do alfabeto:
        Label(self.container1, text='Entrada (Alfabeto): ').grid(row=1, column=1,
                                            sticky=W)

        # textbox aguardando entrada de dados:
        self.nome = Entry(self.container1, width=16,
                          font=fonte1).grid(row=2, column=1, sticky=W)

        # button para Inserir
        # ... ou simplesmente pressione Enter: "<Return>"
        Button(self.container1, text='Inserir').grid(row=2, column=2,
                                                     stick=W, padx=20)

        # label para listagem de alfabetos:
        Label(self.container2, text='Lista de Alfabetos: ').grid(row=1, column=1,
                                                                 sticky=W)

        # textbox listando alfabetos:
        # alterar widget (não é este que foi usado)
        Label(self.container2, width=26,
                          font=fonte1, bg='white').grid(rowspan=5, column=1, sticky=N+E+S+W)

        # button para Unir Alfabetos
        # ... ou simplesmente pressione Enter: "<Return>"
        Button(self.container3, text='Unir Alfabetos').grid(row=12, column=2, pady=8)

        # label pedindo uma palavra:
        Label(self.container4, text='Palavra: ').grid(row=13, column=1,
                                                                 sticky=W, pady=3)

        # textbox aguardando palavra:
        self.nome = Entry(self.container4, width=22,
                          font=fonte1).grid(row=14, column=1, sticky=W, pady=3)

        # button pedindo para Verificar
        # ... ou simplesmente pressione Enter: "<Return>"
        Button(self.container4, text='Verificar ').grid(row=14, column=2, stick=E, pady=8)

        # button para pedir Prefixos
        # ... ou simplesmente pressione Enter: "<Return>"
        Button(self.container4, text='Prefixos ').grid(row=16, column=1, stick=W, pady=8)

        # button para pedir Sufixos
        # ... ou simplesmente pressione Enter: "<Return>"
        Button(self.container4, text='Sufixos ').grid(row=16, column=2, pady=8)

        # button para pedir Subpalavras
        # ... ou simplesmente pressione Enter: "<Return>"
        Button(self.container4, text=' Subpalavras ').grid(row=16, column=3, stick=E, pady=8)


        # Funções a parte
        # def showImg(self):
        #     load = Image.open("content2.gif")
        #     render = ImageTk.PhotoImage(load)
        #
        #     # labels can be text or images
        #     img = Label(self, image=render)
        #     img.image = render
        #     img.place(x=0, y=0)

raiz=Tk()
raiz.geometry("860x510+200+200")
Janela(raiz)
raiz.mainloop()