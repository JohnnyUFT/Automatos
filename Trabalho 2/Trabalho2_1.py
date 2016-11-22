#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
author: Eufrázio Alexandre & Johnny Pereira
email: johnnyuft@gmail.com
last modified: October 2016

"""

from Tkinter import *
import Tkinter as tk
import tkMessageBox
import string
import sys

# --------------
# PALAVRA SOBRE E={a,b} QUE POSSUAM 'a' COMO ANTEPENÚLTIMO SÍMBOLO
# --------------

# -------------
# Implementar a função de transição e
# ------------- função de transição estendida
# -------------

#método que...
def Automato(palavra):
    # chamada para Função de Transição
    #estadoAtual = fTransicao("q0",palavra[0])

    # chamada para Função de Transição Estendida
    estadoFinal = fEstendida('q0', palavra)

    # testes a serem posteriormente desconsiderados
    #print("Estado Atual "+estadoAtual)
    print("Estado Final: %s"%estadoFinal)

    # teste final:
    if((estadoFinal == 'q4') or (estadoFinal == 'q5') or (estadoFinal == 'q6') or (estadoFinal == 'q7')):
        print("Palavra aceita pela linguagem ")
    else:
        print("Palavra rejeitada pela linguagem ")


# método que captura a entrada do usuário
def getEntrada():
    palavra = ed1.get()
    print("Palavra informada "+palavra)
    Automato(palavra)

# implementação da Função de Transição
# apesar de já estar pronta, esta ainda pode receber algumas modificações
def fTransicao(estado, simbolo):
    if(estado=='q0'):
        if(simbolo=='a'):
            return 'q1'
        elif(simbolo=='b'):
            return 'q0'
        else:
            return 'qErr0'
    elif(estado=='q1'):
        if(simbolo=='a'):
            return 'q2'
        elif(simbolo=='b'):
            return 'q3'
        else:
            return 'qErr0'
    elif (estado=='q2'):
        if (simbolo == 'a'):
            return 'q4'
        elif (simbolo == 'b'):
            return 'q5'
        else:
            return 'qErr0'
    elif (estado=='q3'):
        if (simbolo == 'a'):
            return 'q6'
        elif (simbolo == 'b'):
            return 'q7'
        else:
            return 'qErr0'
    elif (estado=='q4'):
        if (simbolo == 'a'):
            return 'q4'
        elif (simbolo == 'b'):
            return 'q5'
        else:
            return 'qErr0'
    elif (estado=='q5'):
        if (simbolo == 'a'):
            return 'q6'
        elif (simbolo == 'b'):
            return 'q7'
        else:
            return 'qErr0'
    elif (estado=='q6'):
        if (simbolo == 'a'):
            return 'q2'
        elif (simbolo == 'b'):
            return 'q3'
        else:
            return 'qErr0'
    elif (estado=='q7'):
        if (simbolo == 'a'):
            return 'q1'
        elif (simbolo == 'b'):
            return 'q0'
        else:
            return 'qErr0'
    elif (estado == 'qErro'):
        return 'qErro'
    else:
        return 'qErro'

# implementação da Função de Transição Estendida
def fEstendida(estado, palavra):
    # teste
    print("Estado Atual: %s - Palavra atual: %s "%(estado, palavra))
    # Base
    if(palavra == ''):
        print("Estado final: %s \n Palavra: %s"%(estado, palavra))
        return estado
    # Indução
    else:
        # separando a palavra em 'xa'
        #x = palavra[:-1] # toda a palavra, exceto o último símbolo
        #a = palavra[-1:] # último símbolo da palavra
        print("Estado final: %s \n Palavra: %s" % (estado, palavra))
        fTransicao(fEstendida(estado, palavra[:-1]), palavra[-1:])
        #fEstendida(fTransicao(estado, a), x)

        # Funciona, em partes
        # separando a palavra em x e a
        #x = palavra[1:]
        #a = palavra[:1]
        #fEstendida(fTransicao(estado, a), x)



def Whenever():
    pass

#  AQUI INICIA A IMPLEMENTAÇÃO DA PARTE GRÁFICA
Janela = tk.Tk()  # instancia da Janela Principal (mainWindow)

#  principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="brown")
frame1.pack()

#  configuração de fonte, permanente para labels e outros
fonte1 = ('Ubuntu', '10')
lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
            font=('Ubuntu', '12', 'bold'), height=6, bg="white")


lb2 = Label(frame1, text="Entrada (palavra): ", font=fonte1)
ed1 = Entry(frame1, text=" ", font=fonte1)
bt1 = Button(frame1, text="Inserir e Analisar", font=fonte1, command=getEntrada)

# empacotamento:
lb1.pack()
lb2.pack()
ed1.pack()
bt1.pack()

Janela.title("Linguagens Formais & Autômatos ")
#  Largura x Altura + Esquerda + Topo
Janela.geometry("560x510+300+100")
Janela.mainloop()
