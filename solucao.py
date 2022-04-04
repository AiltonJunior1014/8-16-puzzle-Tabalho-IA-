from matriz import Matriz
from copy import deepcopy
from queue import PriorityQueue, Queue

class Solucao():
    def __init__(self,x,y):
        self.x = x
        self.y = y



    def bestfirst(self, ini, final):
        # res = self
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
            if res.podeDireita():
                aux[1].direita()
                mov.append(1)
                aux[1].qtdpecas(final.getMatriz())
            if res.podeEsquerda():
                aux[2].esquerda()
                mov.append(2)
                aux[2].qtdpecas(final.getMatriz())
            if res.podeDescer():
                aux[3].desce()
                mov.append(3)
                aux[3].qtdpecas(final.getMatriz())

            # menorcusto = []
            # for i in range(4):
            #     cust = aux[i].dist
            #     if i in mov and aux[i].existe(possoulist):
            #         menorcusto.append(cust)
            #         posmenor = i
            #
            # menorcusto = sorted(menorcusto)
            #
            # for j in range(len(menorcusto)):
            #     for i in range(len(aux)):
            #         if menorcusto[j] == aux[i].dist:
                for j in range(len(aux)):
                    if j in mov and aux[j].existe(passoulist):
                        passou.put(aux[j])

            #caminho.append(posmenor)
            res = passou.get()
            print(res.getMatriz())


        print("terminouu")
        print(caminho)
