import sys
import time
from threading import Thread
from matriz import Matriz
from copy import deepcopy
from queue import PriorityQueue, Queue
from tkinter import *
import tkinter
###Calucar tredi

class Solucao():
    def __init__(self, menu):
        self.tam = 3
        self.mat = Matriz(self.tam, self.tam)
        self.mat2 = Matriz(self.tam, self.tam)
        self.mat.monta()
        self.mat2.monta()
        self.menu = menu

        self.button = tkinter.Button(menu, text="Algoritmo A*", command=lambda:self.clique1())
        self.button2 = tkinter.Button(menu, text="Algoritmo Best First", command=lambda:self.clique2())
        self.button3 = tkinter.Button(menu, text="Trocar 8-16", command=lambda:self.troca())
        self.button4 = tkinter.Button(menu, text="Embaralhar", command=lambda:self.embaralha())
        self.button.grid(row=4, column=0)
        self.button2.grid(row=4, column=1)
        self.button3.grid(row=5, column=0)
        self.button4.grid(row=5, column=1)

        self.label = Label()
        self.label1 = Label()
        self.label2 = Label()
        self.label3 = Label()
        self.label4 = Label()
        self.label5 = Label()
        self.label6 = Label()
        self.label7 = Label()
        self.label8 = Label()
        self.label9 = Label()
        self.label10 = Label()
        self.label11 = Label()
        self.label12 = Label()
        self.label13 = Label()
        self.label14 = Label()
        self.label15 = Label()







    def bestfirst(self, ini, final):
        caminho = []
        passoulist = []
        passou = PriorityQueue()
        passou.maxsize = 999999
        passou.put(ini)
        res = passou.get()
        res.qtdpecas(final.getMatriz())
        while not res.isEqual(final.getMatriz()):
            passoulist.append(deepcopy(res))
            aux = []
            mov = []
            for i in range(4):
                aux.append(deepcopy(res))

            if res.podeSubir():
                aux[0].sobe()
                mov.append(0)
                aux[0].qtdpecas(final.getMatriz())
                aux[0].inserecaminho(0)
            if res.podeDireita():
                aux[1].direita()
                mov.append(1)
                aux[1].qtdpecas(final.getMatriz())
                aux[1].inserecaminho(1)
            if res.podeEsquerda():
                aux[2].esquerda()
                mov.append(2)
                aux[2].qtdpecas(final.getMatriz())
                aux[2].inserecaminho(2)
            if res.podeDescer():
                aux[3].desce()
                mov.append(3)
                aux[3].qtdpecas(final.getMatriz())
                aux[3].inserecaminho(3)

            for j in range(len(aux)):
                if j in mov and aux[j].existe(passoulist):
                    passou.put(aux[j])


            res = passou.get()
            print(res.getMatriz())


        print(res.caminho)
        self.andar(res.caminho)


    def a_estrla(self, ini, final):
        caminho = []
        passoulist = []
        passou = PriorityQueue()
        passou.maxsize = 999999
        tempo = time.time()
        no =0
        passou.put(ini)
        res = passou.get()
        res.custo()
        while not res.isEqual(final.getMatriz()):

            passoulist.append(deepcopy(res))

            aux = []
            mov = []

            for i in range(4):
                aux.append(deepcopy(res))

            if res.podeSubir():
                aux[0].sobe()
                mov.append(0)
                aux[0].qtdpecas(final.getMatriz())
                aux[0].inserecaminho(0)
                aux[0].incg()

            if res.podeDireita():
                aux[1].direita()
                mov.append(1)
                aux[1].qtdpecas(final.getMatriz())
                aux[1].inserecaminho(1)
                aux[1].incg()
            if res.podeEsquerda():
                aux[2].esquerda()
                mov.append(2)
                aux[2].qtdpecas(final.getMatriz())
                aux[2].inserecaminho(2)
                aux[2].incg()
            if res.podeDescer():
                aux[3].desce()
                mov.append(3)
                aux[3].qtdpecas(final.getMatriz())
                aux[3].inserecaminho(3)
                aux[3].incg()

            for j in range(len(aux)):
                if j in mov and aux[j].existe(passoulist):
                    passou.put(aux[j])
            res = passou.get()
            no+=1
        fim = time.time()
        print(res.custo())
        print("Melhor caminho: ")
        print(str(res.caminho))
        print("Tempo de Solução{:.2}\n".format(fim-tempo))

        print("Passou por:"+str(float(no))+" Nóis\n")
        print(len(res.caminho))
        self.andar(res.caminho)

    def settamanho(self):
        sys.stdout.flush()
        if (self.tam == 3):
            self.label = Label(self.menu, text=self.mat.mat[0][0], font="Arial")
            self.label1 = Label(self.menu, text=self.mat.mat[0][1], font="Arial")
            self.label2 = Label(self.menu, text=self.mat.mat[0][2], font="Arial")
            self.label3 = Label(self.menu, text=self.mat.mat[1][0], font="Arial")
            self.label4 = Label(self.menu, text=self.mat.mat[1][1], font="Arial")
            self.label5 = Label(self.menu, text=self.mat.mat[1][2], font="Arial")
            self.label6 = Label(self.menu, text=self.mat.mat[2][0], font="Arial")
            self.label7 = Label(self.menu, text=self.mat.mat[2][1], font="Arial")
            self.label8 = Label(self.menu, text=self.mat.mat[2][2], font="Arial")

            self.label.grid(row=0, column=0, sticky="nsew")
            self.label1.grid(row=0, column=1, sticky="nsew")
            self.label2.grid(row=0, column=2, sticky="nsew")
            self.label3.grid(row=1, column=0, sticky="nsew")
            self.label4.grid(row=1, column=1, sticky="nsew")
            self.label5.grid(row=1, column=2, sticky="nsew")
            self.label6.grid(row=2, column=0, sticky="nsew")
            self.label7.grid(row=2, column=1, sticky="nsew")
            self.label8.grid(row=2, column=2, sticky="nsew")

            self.label9 = Label(self.menu, text="", font="Arial")
            self.label10 = Label(self.menu, text="", font="Arial")
            self.label11 = Label(self.menu, text="", font="Arial")
            self.label12 = Label(self.menu, text="", font="Arial")
            self.label13 = Label(self.menu, text="", font="Arial")
            self.label14 = Label(self.menu, text="", font="Arial")
            self.label15 = Label(self.menu, text="", font="Arial")
            self.label9.grid(row=9, column=9, sticky="nsew")
            self.label10.grid(row=9, column=9, sticky="nsew")
            self.label11.grid(row=9, column=9, sticky="nsew")
            self.label12.grid(row=9, column=9, sticky="nsew")
            self.label13.grid(row=9, column=9, sticky="nsew")
            self.label14.grid(row=9, column=9, sticky="nsew")
            self.label15.grid(row=9, column=9, sticky="nsew")
        elif (self.tam == 4):
            self.label = Label(self.menu, text=self.mat.mat[0][0], font="Arial")
            self.label1 = Label(self.menu, text=self.mat.mat[0][1], font="Arial")
            self.label2 = Label(self.menu, text=self.mat.mat[0][2], font="Arial")
            self.label3 = Label(self.menu, text=self.mat.mat[0][3], font="Arial")
            self.label4 = Label(self.menu, text=self.mat.mat[1][0], font="Arial")
            self.label5 = Label(self.menu, text=self.mat.mat[1][1], font="Arial")
            self.label6 = Label(self.menu, text=self.mat.mat[1][2], font="Arial")
            self.label7 = Label(self.menu, text=self.mat.mat[1][3], font="Arial")
            self.label8 = Label(self.menu, text=self.mat.mat[2][0], font="Arial")
            self.label9 = Label(self.menu, text=self.mat.mat[2][1], font="Arial")
            self.label10 = Label(self.menu, text=self.mat.mat[2][2], font="Arial")
            self.label11 = Label(self.menu, text=self.mat.mat[2][3], font="Arial")
            self.label12 = Label(self.menu, text=self.mat.mat[3][0], font="Arial")
            self.label13 = Label(self.menu, text=self.mat.mat[3][1], font="Arial")
            self.label14 = Label(self.menu, text=self.mat.mat[3][2], font="Arial")
            self.label15 = Label(self.menu, text=self.mat.mat[3][3], font="Arial")
            self.label.grid(row=0, column=0,sticky="nsew")
            self.label1.grid(row=0, column=1, sticky="nsew")
            self.label2.grid(row=0, column=2, sticky="nsew")
            self.label3.grid(row=0, column=3, sticky="nsew")
            self.label4.grid(row=1, column=0, sticky="nsew")
            self.label5.grid(row=1, column=1, sticky="nsew")
            self.label6.grid(row=1, column=2, sticky="nsew")
            self.label7.grid(row=1, column=3, sticky="nsew")
            self.label8.grid(row=2, column=0, sticky="nsew")
            self.label9.grid(row=2, column=1, sticky="nsew")
            self.label10.grid(row=2, column=2, sticky="nsew")
            self.label11.grid(row=2, column=3, sticky="nsew")
            self.label12.grid(row=3, column=0, sticky="nsew")
            self.label13.grid(row=3, column=1, sticky="nsew")
            self.label14.grid(row=3, column=2, sticky="nsew")
            self.label15.grid(row=3, column=3, sticky="nsew")


        #time.sleep(1)


    def clique1(self):
        self.a_estrla(self.mat, self.mat2)
        self.settamanho()

    def clique2(self):
        self.bestfirst(self.mat, self.mat2)
        self.settamanho()

    def troca(self):
        print('leo')

        if (self.tam == 3):
            self.tam = 4
        else:
            self.tam = 3
        print(self.tam)
        self.mat = Matriz(self.tam, self.tam)
        self.mat2 = Matriz(self.tam, self.tam)
        self.mat.monta()
        self.mat2.monta()
        self.settamanho()

    def embaralha(self):
        for x in range(2):
            self.mat.embaralha()
        self.settamanho()

    def andar(self, caminho):
        for i in caminho:
            if i == 0:
                self.mat.sobe()
                print("sobe")
            if i == 1:
                self.mat.direita()
                print("direita")
            if i == 2:
                self.mat.esquerda()
                print("esquerda")
            if i == 3:
                self.mat.desce()
                print("desce")
            self.settamanho()


            #time.sleep(1)
