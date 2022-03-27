import numpy as np
class Matriz():

    def __init__(self,linhas,colunas):

        self.lin = linhas
        self.col = colunas
        self.mat = np.zeros((linhas,colunas), dtype=int)
        self.posx=0
        self.posy=0


    def monta(self,num):
        cont = 0
        for x in range (self.lin, 2):
            for y in range (self.col/2):
                self.mat[x][y] = num [cont]
                cont+=1


    def Monta (self):
        aux =0
        for x in range (self.lin):
            for y in range (self.col):
                self.mat[x][y] = aux
                aux += 1
        self.posX=x
        self.posY=y


    def GetMatriz(self):
        return self.mat

    def isEqual(self,matriz):
        return self.mat == matriz



    def Sobe(self):
        Aux = self.mat[self.posx][self.posy]
        self.mat[self.posx][self.posy] = self.mat[self.posx-1][self.posy]
        self.mat[self.posx - 1][self.posy ] = Aux
        self.posx = self.posx-1

    def Desce(self):
        Aux = self.mat[self.posx][self.posy]
        self.mat[self.posx][self.posy] = self.mat[self.posx+1][self.posy]
        self.mat[self.posx + 1][self.posy] = Aux
        self.posx = self.posx+1


    def Direita(self):
        Aux = self.mat[self.posx][self.posy]
        self.mat[self.posx][self.posy] = self.mat[self.posx][self.posy+1]
        self.mat[self.posx][self.posy + 1] = Aux

    def Esquerda(self):
        Aux = self.mat[self.posx][self.posy]
        self.mat[self.posx][self.posy] = self.mat[self.posx][self.posy+1]
        self.mat[self.posx][self.posy + 1] = Aux

    def Mostra(self):
        for x in range(self.lin, 2):
            for y in range(self.col/2):
                print(self.mat[x][y])
            print("\n")
        print(self.mat)
        print("" + str(self.lin) + "" + str(self.col))
        print(""+str(self.posx)+""+str(self.posy))



