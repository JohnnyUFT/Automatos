#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: November 2016

"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import string
import sys

"""
PALAVRA SOBRE E={a,b} QUE POSSUAM 'a' COMO ANTEPENÚLTIMO SÍMBOLO.

Implementar a função de transição e função de transição estendida.
"""

def getEntrada():
    """
    Método que captura a entrada do usuário.
    :return:
    """
    palavra = ed1.get()
    print("Palavra informada "+palavra)
    Automato(palavra)

def Automato(palavra):
    """
    Envia a palavra recebida para ser testado pelo autômato.

    De acordo com o retorno da função de transição estendida,
    que é chamada aqui, informa se a palavra inserida é aceitável
    ou não, a depender das regras impostas pela linguagem que foi proposta.
    :param palavra:
    :return:
    """
    #estadoAtual = fTransicao('q0','a')
    #print("Retornou %s\n"%estadoAtual)

    # chamada para Função de Transição Estendida
    estadoFinal = fEstendida('q0', palavra)

    # teste dispensável
    print("Estado Final: %s"%estadoFinal)

    # verificação final:
    if((estadoFinal == 'q4') or (estadoFinal == 'q5') or (estadoFinal == 'q6') or (estadoFinal == 'q7')):
        messagebox.showinfo("Info", "palavra aceita! ")
    else:
        messagebox.showerror("Erro", "palavra rejeitada! ")


#
def fTransicao(estado, simbolo):
    """
    Função de Transição.

    Aqui é implementado o autômato tal como se vê no diagrama,
    ou na tabela de transições.
    :param estado:
    :param simbolo:
    :return: estado
    """
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
    """
    Função de Transição Estendida.

    Como se sabe, recebe um estado e uma palavra,
    faz uso da função de transição para cada símbolo lido na palavra,
    possui caráter recursivo.
    :param estado:
    :param palavra:
    :return: estado
    """
    # teste dispensável
    print("Estado Atual: %s - Palavra atual: %s "%(estado, palavra))
    # Base
    if(palavra == ''):
        return estado
    # Indução
    else:
        # separando a palavra em x e a
        x = palavra[1:] # toda a palavra, exceto o primeiro símbolo
        a = palavra[:1] # primeiro símbolo da palavra
        return fEstendida(fTransicao(estado, a), x)



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
