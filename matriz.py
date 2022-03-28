import random
from copy import deepcopy

import numpy as np
class Matriz():

    def __init__(self,linhas,colunas):
        self.g = 0 #distancia do inicio
        self.lin = linhas
        self.col = colunas
        self.mat = np.zeros((linhas,colunas), dtype=int)
        self.posx = 0
        self.posy = 0

    def custo(self, matriz):
        return self.g + self.qtdpecas(matriz)

    def getg(self):
        return self.g
    def monta(self, num):
        cont = 0
        for x in range (self.lin, 2):
            for y in range (self.col/2):
                self.mat[x][y] = num [cont]
                cont += 1

    def getlin(self):
        return self.lin

    def getcol(self):
        return self.col

    def monta(self):
        aux = 0
        for x in range (self.lin):
            for y in range (self.col):
                self.mat[x][y] = aux
                aux += 1


    def getMatriz(self):
        return self.mat

    def isEqual(self,matriz):
        return self.mat == matriz



    def sobe(self):
        Aux = self.mat[self.posy][self.posx]
        self.mat[self.posy][self.posx] = self.mat[self.posy-1][self.posx]
        self.mat[self.posy - 1][self.posx ] = Aux
        self.posy = self.posy-1

    def desce(self):
        Aux = self.mat[self.posy][self.posx]
        self.mat[self.posy][self.posx] = self.mat[self.posy+1][self.posx]
        self.mat[self.posy + 1][self.posx] = Aux
        self.posy = self.posy+1


    def direita(self):
        Aux = self.mat[self.posy][self.posx]
        self.mat[self.posy][self.posx] = self.mat[self.posy][self.posx+1]
        self.mat[self.posy][self.posx + 1] = Aux
        self.posx = self.posx+1

    def esquerda(self):
        Aux = self.mat[self.posy][self.posx]
        self.mat[self.posy][self.posx] = self.mat[self.posy][self.posx-1]
        self.mat[self.posy][self.posx - 1] = Aux
        self.posx = self.posx -1

    def mostra(self):
        print(self.mat)
        print("" + str(self.lin) + "" + str(self.col))
        print(""+str(self.posx)+""+str(self.posy))

    def podeSubir(self):
        return not(self.posy == 0)

    def podeDescer(self):
        return not(self.posy == self.lin-1)

    def podeEsquerda(self):
        return not(self.posx == 0)

    def podeDireita(self):
        return not(self.posx == self.col-1)

    def embaralha(self):
        random.seed()
        for x in range(self.lin+self.col):
            num = random.randint(0, 3)
            if num == 0:
                if self.podeSubir():
                    self.sobe()
            elif num == 1:
                if self.podeEsquerda():
                    self.esquerda()
            elif num == 2:
                if self.podeDescer():
                    self.desce()
            elif num == 3:
                if self.podeDireita():
                    self.direita()

    def qtdpecas(self, matriz):# distancia para final
        if not self.isEqual(matriz).all():
            count = 0
            for x in range (self.lin):
                for y in range (self.col):
                    if self.mat[x][y] != matriz[x][y]:
                        count += 1
            return count

    def bestfirst(self, final):
        res = self
        caminho = []


        while not(self.isEqual(final.getMatriz()).all()):
            aux = []
            mov = []

            for i in range(4):
                aux.append(deepcopy(res))

            if res.podeSubir():
                aux[0].sobe()
                mov.append(0)
            if res.podeDireita():
                aux[1].direita()
                mov.append(1)
            if res.podeEsquerda():
                aux[2].esquerda()
                mov.append(2)
            if res.podeDescer():
                aux[3].desce()
                mov.append(3)

            menorcusto = 99999
            posmenor = 0
            for i in range(4):
                cust = aux[i].custo(final.getMatriz())
                if menorcusto > cust and i in mov:
                    menorcusto = cust
                    posmenor = i

            res = aux[posmenor]
            caminho.append(posmenor)
            res.g += 1
            print(res.getg())
        print(res)