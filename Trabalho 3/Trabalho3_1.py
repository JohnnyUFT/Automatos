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
import sys
from tkinter import messagebox
from tkinter import ttk

def obterAlfbabeto():
    alfabeto = ent1.get()

    q0(alfabeto)# começa a verificar o formalismo para o conjunto dado

    estInicial = ent3.get()
    estFinal = ent4.get()
    print(alfabeto, estInicial, estFinal)

    print(type(estFinal))
    lestFinais = estFinal.split(',')

    print("lestFinais em obterAlfabeto: %s"%lestFinais)

    # enviar lesFinais para quem?

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
        elif alfabeto[i] == '}' and i == len(alfabeto)-1: # não há mais simbolos na fita
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

def analisaPalavra():
    """
    Realiza última verificação para atestar se a palavra foi aceita, ou não.
    :param palavra:
    :return: void
    """
    palavra = ent5.get()# palavra a ser lida na 'fita'
    print(palavra)# a remover
    estado = ent3.get() # estado inicial, conforme informado na GUI

    # estados finais a serem comparados
    estFinal = ent4.get()
    lestFinais = estFinal.split(',') # guarda estados finais

    ultimoEstado = fEstendida(estado, palavra)
    if(ultimoEstado in lestFinais):# essa comparação funciona?
        messagebox.showinfo("Parabéns", "Palavra aceita!")
    else:
        messagebox.showerror("Desculpe", "Palavra rejeitada!")


def preencheListaEstados(qtdEstados):
    lista = []
    for i in range(qtdEstados):
        estado = 'q'+str(i)
        print(type(i))
        lista.append(estado)
    print(lista, type(estado))# a remover
    return lista

def gerarTabela():
    alfabeto = ent1.get()
    print("Onononono: %s" %alfabeto)

    qtdEstados = int(ent2.get())
    print(qtdEstados)

    listaEstados = preencheListaEstados(qtdEstados)

    # tratamento necessário
    simbolo = []
    tam = len(alfabeto)-1
    for i in range(tam):
        if(verAlfaNumerico(alfabeto,i)):
            simbolo.append(alfabeto[i])

    print(simbolo, listaEstados)

    # criando widgets dinamicos
    for i in range(len(listaEstados)):
        for j in range(len(simbolo)):
            l = Entry(frame9, text='%d.%d' % (i, j), relief=RIDGE)
            l.grid(row=i, column=j, sticky=NSEW)

# método encontrada em: http://stackoverflow.com/questions/8369560/finding-widgets-on-a-grid-tkinter-module
def find_in_grid(frame9, row, column):
    """
    Encontra o widget a partir de linha e coluna
    e retorna o widget com as coordenadas dadas
    :param frame: str
    :param row: str
    :param column: str
    :return: widget
    """
    for children in frame9.children.values():
        info = children.grid_info()
        # perceba que os numeros das linhas e colunas numbers são guardados como string
        if info['row'] == str(row) and info['column'] == str(column):
            return children
    return None

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

def fTransicao(estado, a):
    """
    Trabalha em conjunto com find_in_grid().
    A intenção aqui é encontrar os parâmetros que find_in_grid necessita,
    receber o retorno de find_in_grid e devolvê-lo a fEstendida,
    que a chamou.
    """
    #estado = ent3.get() # estado inicial, conforme informado na GUI
    info = ent3.grid_info()

    alfabeto = ent1.get()
    alfabeto2 = alfabeto.replace("{", "")# remove as '{'
    alfabeto3 = alfabeto2.replace("}","")

    row = info['row']# a referência da linha é dada diretamente
    # ... através do atributo row do estado recebido como parâmetro

    lista = []
    # try
    lista = alfabeto3.split(',')
    # exception
    # caso não tenha ',' no alfabeto, por exemplo
    print(lista)# a remover

    tam = len(lista)
    column = -1
    for i in range(tam):# saber qual o simbolo a ser processado
        if(a == lista[i]):# simbolo pertence á coluna i
            #row = ?
            column = i
    if(column >= 0):# encontrou o simbolo da palavra
        # chamada do metodo find_in_grid:
        pass
    else:
        pass
        # retorna alguma coisa?
        # mensagem de erro:
        # palavra rejeitada!

    # comparando-o com a lista de simbolos
    # para saber qnts incrementos serão necessários para correta
    # identificação da coluna (simbolo do alfabeto)
    estadoAtual = find_in_grid(frame9, info['row'], info['column'])

    # estadoAtual é uma string ou um widget?
    print(type(estadoAtual))
    # se for um widget, será necessário fazer o seguinte:
    # nomeEstadoAtual = estadoAtual['text'] # ou algo assim

    #return nomeEstadoAtual
    return estadoAtual


#  AQUI INICIA A IMPLEMENTAÇÃO DA PARTE GRÁFICA
Janela = tk.Tk()  # instancia da Janela Principal (mainWindow)
"""
Posteriomente, separar este método em uma classe separada
e trabalhar com implementação OO e GUI.
"""

values = StringVar()

#  principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="white")
frame2 = Frame(Janela, height=100, bg="white")
frame3 = Frame(Janela, height=100, bg="white")
frame4 = Frame(Janela, height=100, bg="white")
#frame5 = Frame(Janela, height=100, bg="white")
frame6 = Frame(Janela, width=30, bg="white")# serve apenas para definir uma margem
frame7 = Frame(Janela, width=30, bg="white")# serve apenas para definir uma margem
frame8 = Frame(Janela, height=100, bg="white")# guarda o título: Tabela de Transição
frame9 = Frame(Janela, height=100, bg="white")# guarda a tabela de transição em si

# empacotamento e disposição em que aparecem na tela
frame1.pack(side=TOP, fill=X)
frame6.pack(side=LEFT, fill=Y)# margem esquerda
frame7.pack(side=RIGHT, fill=Y)# margem direita
frame2.pack(side=TOP, fill=X)
frame8.pack(side=TOP, fill=X)
frame9.pack(side=TOP, fill=X)
frame3.pack(side=TOP, fill=X)
frame4.pack(side=TOP, fill=X)

#  configuração de fonte, permanente para labels e outros
fonte1 = ('Ubuntu', '10')
fonte2 = ('Ubuntu', '10', 'italic')
# elementos contidos no frame1
lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
            font=('Ubuntu', '12', 'bold'), height=6, bg="white")
logo = Image.open("uft4.jpg")
photo1 = ImageTk.PhotoImage(logo)
lb11 = Label(frame1, image=photo1, bg="white")
lb1.grid(row=0, column=1, stick=W)
lb11.grid(row=0, column=0, stick=W)

#  elementos contidos no frame2
lb2 = Label(frame2, text="Alfabeto: ", font=fonte1, bg="white")
ent1 = Entry(frame2, text="", font=fonte1)
lb3 = Label(frame2, text="Qtd estados: ", font=fonte1, bg="white")
ent2 = Entry(frame2, text="", font=fonte1)
lb4 = Label(frame2, text="Estado Inicial: ", font=fonte1, bg="white")
ent3 = Entry(frame2, text="0", font=fonte2)
ent3.insert(0, "q0")
lb5 = Label(frame2, text="Estado Final: ", font=fonte1, bg="white")
ent4 = Entry(frame2, text='', font=fonte2)
ent4.insert(0, "q9")

btn2 = Button(frame2, text="Ok ", font=fonte1, command=obterAlfbabeto, bg="white")

# elementos contidos no frame8
lb6 = Label(frame8, text="Função de Transição: ", font=fonte1, bg="white")
btn4 = Button(frame8, text="Gerar tabela", bg="white", command=gerarTabela)

# elementos contidos no frame3
lb8 = Label(frame3, text="Palavra informada:", bg="white")
ent5 = Entry(frame3, text="", font=fonte1)
btn3 = Button(frame3, text="Inserir e Processar", command=analisaPalavra, bg="white")

# frame4 possui apenas uma imagem (caráter decorativo)
image = Image.open("cinema.png")
photo = ImageTk.PhotoImage(image)
lb9 = Label(frame4, image=photo, bg="white")

#  disposição dos widgets do frame2
lb2.grid(row=0, column=0, stick=W)
ent1.grid(row=1, column=0, stick=W)
lb3.grid(row=0, column=1, stick=W)
ent2.grid(row=1, column=1, stick=W)
lb4.grid(row=0, column=3, stick=W)
ent3.grid(row=1, column=3, stick=W)
lb5.grid(row=0, column=4, stick=W)
ent4.grid(row=1, column=4, stick=W)
btn2.grid(row=1, column=5, stick=W)

# disposição dos widgets do frame3
lb6.grid(row=0, column=0, stick=W)
btn4.grid(row=0, column=1, stick=W)
lb8.grid(row=2, column=0, stick=W)
ent5.grid(row=3, column=0, stick=W)
btn3.grid(row=3, column=1, stick=W)

# disposição dos widgets do frame4
lb9.pack()

Janela.title("Linguagens Formais & Autômatos - Trabalho #3")
#  Largura x Altura + Esquerda + Topo
Janela.geometry("770x650+300+100")
Janela.mainloop()
