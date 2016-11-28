#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: November 2016
"""


# pacotes importados
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import string
import sys

"""
    Este trabalho tem por objetivo SIMULAR a implementação

    de um AFND que possui as seguintes características:
    reconhecer w sobre o alfabeto 'a','b' | w tenha 'a' como
    antepenúltimo símbolo.
"""


def getEntrada():
    """
    Aqui temos o método que captura a entrada (palavra),

    utilizando os componentes de interface gráfica com
    o usuário. Este método é chamado pelo método removeSpace().
    E chama o método Automato() passando a palavra lida como parâmetro.
    :return:
    """
    palavra = ed1.get()
    print("Palavra informada "+palavra)
    Automato(palavra)


def Automato(palavra):
    """
    Aqui temos o método que se encarrega de capturada a entrada do usuário,

    enviá-la para processamento e posteriormente analisar o estado de retorno
    como sendo 'de aceitação' ou 'de NÃO aceitação'
    :param palavra:
    :return:
    """
    # chamada para Função de Transição Estendida
    lEstados = ['q0'] # declaração e inicialização, tipo lista
    estadosFinais = fEstendida(lEstados, palavra)

    # teste dispensável
    print("Estados Finais: %s"%estadosFinais)

    # teste final:
    if 'q3' in estadosFinais:
        messagebox.showinfo("Info", "palavra aceita! ")
    else:
        messagebox.showerror("Erro", "palavra rejeitada! ")


def fTransicao(estado, simbolo):
    """
    Aqui temos o método que implementa a Função de Transição

    para o AFND em questão: "Autômato que reconhece palavras sobre
    alfabeto 'a' 'b' que possuam 'a' como ANTEPENÚLTIMO símbolo"
    :param estado:
    :param simbolo:
    :return:
    """
    if(estado=='q0'):
        if(simbolo=='a'):
            return ['q0','q1']
        elif(simbolo=='b'):
            return ['q0']
        else:
            return ['qErr0']
    elif(estado=='q1'):
        if(simbolo=='a' or simbolo=='b'):
            return ['q2']
        else:
            return ['qErr0']
    elif (estado == 'q2'):
        if (simbolo == 'a' or simbolo == 'b'):
            return ['q3']
        else:
            return ['qErr0']
    # tratamento para estado de erro
    else:
        return ['qErro']


def fEstendida(lEstados, palavra):
    """
    Aqui temos o método que 'simula' a implementação

    da Função de Transição Estendida para os AFNDs
    :param lEstados:
    :param palavra:
    :return:
    """
    # teste dispensável
    print("Estado Atual: %s - Palavra atual: %s "%(lEstados, palavra))
    # Base
    if(palavra == ""):
        return lEstados
    # Indução
    else:
        print("Lista atual: %s"%lEstados)
        for elementos in lEstados:
            print("Elementos na lista: %s"%elementos)
            # separando a palavra em x e a
            x = palavra[1:]  # toda a palavra, exceto o primeiro símbolo
            a = palavra[:1]  # primeiro símbolo da palavra
            lista1 = []
            for elementos in lEstados:
                lista1.extend(fTransicao(elementos, a))
            return fEstendida(lista1, x)



Janela = tk.Tk()  # instancia da Janela Principal (mainWindow)
"""
Aqui jaz, a implementação dos componentes visuais bem como a organização

dos mesmos. Tecnologia utilizada: Tkinter GUI (Python).
"""

#  principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="")
frame1.pack()

#  configuração de fonte, permanente para labels e outros
fonte1 = ('Ubuntu', '10')
lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
            font=('Ubuntu', '12', 'bold'), height=6)


lb2 = Label(frame1, text="Entrada (palavra): ", font=fonte1)
ed1 = Entry(frame1, text=" ", font=fonte1)
bt1 = Button(frame1, text="Inserir e Analisar", font=fonte1, command=getEntrada)

# empacotamento:
lb1.pack()
lb2.pack()
ed1.pack()
bt1.pack()

Janela.title("Linguagens Formais & Autômatos - Trabalho #4")
#  Largura x Altura + Esquerda + Topo
Janela.geometry("560x310+300+100")
Janela.mainloop()
