from matriz import Matriz
from copy import deepcopy
from queue import PriorityQueue, Queue

class Solucao():
    def __init__(self,x,y):
        self.x = x
        self.y = y



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

        ini.andar(res.caminho)
        print("terminouu")
        print(res.caminho)


    def a_estrla(self, ini, final):
        caminho = []
        passoulist = []
        passou = PriorityQueue()
        passou.maxsize = 999999
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
            print(res.getMatriz())

        ini.andar(res.caminho)
        print("terminouu")
        print(res.custo())
        print(res.caminho)
        print(len(res.caminho))
