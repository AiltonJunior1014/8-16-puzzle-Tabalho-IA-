import sys
import time
from threading import Thread
from matriz import Matriz
from copy import deepcopy
from queue import PriorityQueue
from tkinter import *
import tkinter


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
        self.button.place(relx=0.6, rely=0.3, anchor=CENTER)
        self.button2.place(relx=0.36, rely=0.3, anchor=CENTER)
        self.button3.place(relx=0.6, rely=0.4, anchor=CENTER)
        self.button4.place(relx=0.4, rely=0.4, anchor=CENTER)

        self.labelresp = Label()
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

        Thread(target = self.settamanho, daemon=True).start()


    def resposta (self, tempo, res, no):
        resp = "Melhor caminho: \n" \
               ""+str(res.caminho)+"\n\n" \
               "Tempo de Solução:"+str(tempo)+"\n" \
               "Passou por:" + str(float(no)) + " Nós\n"
        self.labelresp = Label(self.menu, text=resp, font=("Arial", 8))
        self.labelresp.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.andar(res.caminho)



    def bestfirst(self, ini, final):
        passou = PriorityQueue()
        tempo = time.time()
        passou.maxsize = 999
        passou.put(ini)
        no = 0
        res = passou.get()
        res.qtdpecas(final.getMatriz())
        while not res.isEqual(final.getMatriz()):
            res.appendpassou(deepcopy(res.getMatriz()))
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
                if j in mov and not(aux[j].existe(deepcopy(res.passoulist))):
                    passou.put(aux[j])

            print("i")
            no=+1
            print(res.mat)
            res = passou.get()

        fim = time.time()
        self.resposta(fim - tempo,res,no)

    def a_estrla(self, ini, final):
        passou = PriorityQueue()
        passou.maxsize = 999
        tempo = time.time()
        no = 0
        passou.put(ini)
        res = passou.get()
        while not res.isEqual(final.getMatriz()) and passou.not_empty:
            res.custo()
            aux = []
            mov = []
            res.appendpassou(deepcopy(res.getMatriz()))

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
                if j in mov and not(aux[j].existe(deepcopy(res.passoulist))):
                    passou.put(aux[j])

            print("i")
            res = passou.get()
            no += 1
            print(res.mat)

        fim = time.time()
        Thread(target= self.resposta(fim - tempo, res, no)).start()

    def settamanho(self):
        sys.stdout.flush()

        if self.tam == 3:
            self.label = Label(self.menu, text=self.mat.mat[0][0], font="Arial", width=10)
            self.label1 = Label(self.menu, text=self.mat.mat[0][1], font="Arial", width=10)
            self.label2 = Label(self.menu, text=self.mat.mat[0][2], font="Arial", width=10)
            self.label3 = Label(self.menu, text=self.mat.mat[1][0], font="Arial", width=10)
            self.label4 = Label(self.menu, text=self.mat.mat[1][1], font="Arial", width=10)
            self.label5 = Label(self.menu, text=self.mat.mat[1][2], font="Arial", width=10)
            self.label6 = Label(self.menu, text=self.mat.mat[2][0], font="Arial", width=10)
            self.label7 = Label(self.menu, text=self.mat.mat[2][1], font="Arial", width=10)
            self.label8 = Label(self.menu, text=self.mat.mat[2][2], font="Arial", width=10)
            self.label9 = Label(self.menu, text="", font="Arial")
            self.label10 = Label(self.menu, text="", font="Arial")
            self.label11 = Label(self.menu, text="", font="Arial")
            self.label12 = Label(self.menu, text="", font="Arial")
            self.label13 = Label(self.menu, text="", font="Arial")
            self.label14 = Label(self.menu, text="", font="Arial")
            self.label15 = Label(self.menu, text="", font="Arial")

            self.label.grid(row=0, column=0, sticky="nsew")
            self.label1.grid(row=0, column=1, sticky="nsew")
            self.label2.grid(row=0, column=2, sticky="nsew")
            self.label3.grid(row=1, column=0, sticky="nsew")
            self.label4.grid(row=1, column=1, sticky="nsew")
            self.label5.grid(row=1, column=2, sticky="nsew")
            self.label6.grid(row=2, column=0, sticky="nsew")
            self.label7.grid(row=2, column=1, sticky="nsew")
            self.label8.grid(row=2, column=2, sticky="nsew")
            self.label9.grid(row=0, column=3, sticky="nsew")
            self.label10.grid(row=1, column=3, sticky="nsew")
            self.label11.grid(row=2, column=3, sticky="nsew")
            self.label12.grid(row=3, column=0, sticky="nsew")
            self.label13.grid(row=3, column=1, sticky="nsew")
            self.label14.grid(row=3, column=2, sticky="nsew")
            self.label15.grid(row=3, column=3, sticky="nsew")


        elif (self.tam == 4):
            self.label = Label(self.menu, text=self.mat.mat[0][0], font="Arial", width=10)
            self.label1 = Label(self.menu, text=self.mat.mat[0][1], font="Arial", width=10)
            self.label2 = Label(self.menu, text=self.mat.mat[0][2], font="Arial", width=10)
            self.label3 = Label(self.menu, text=self.mat.mat[0][3], font="Arial", width=10)
            self.label4 = Label(self.menu, text=self.mat.mat[1][0], font="Arial", width=10)
            self.label5 = Label(self.menu, text=self.mat.mat[1][1], font="Arial", width=10)
            self.label6 = Label(self.menu, text=self.mat.mat[1][2], font="Arial", width=10)
            self.label7 = Label(self.menu, text=self.mat.mat[1][3], font="Arial", width=10)
            self.label8 = Label(self.menu, text=self.mat.mat[2][0], font="Arial", width=10)
            self.label9 = Label(self.menu, text=self.mat.mat[2][1], font="Arial", width=10)
            self.label10 = Label(self.menu, text=self.mat.mat[2][2], font="Arial", width=10)
            self.label11 = Label(self.menu, text=self.mat.mat[2][3], font="Arial", width=10)
            self.label12 = Label(self.menu, text=self.mat.mat[3][0], font="Arial", width=10)
            self.label13 = Label(self.menu, text=self.mat.mat[3][1], font="Arial", width=10)
            self.label14 = Label(self.menu, text=self.mat.mat[3][2], font="Arial", width=10)
            self.label15 = Label(self.menu, text=self.mat.mat[3][3], font="Arial", width=10)
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



