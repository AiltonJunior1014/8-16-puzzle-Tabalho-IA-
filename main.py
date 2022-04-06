from matriz import Matriz
from solucao import Solucao
from tkinter import *
import tkinter

tam=3
sol = Solucao(tam, tam)

mat = Matriz(tam, tam)
mat2 = Matriz(tam, tam)
mat.monta()
mat2.monta()


# for x in range (2):
#     mat.embaralha()


def clique1():
    sol.a_estrla(mat, mat2)

def clique2():
    sol.bestfirst(mat, mat2)


def troca():
    print('leo')
    global tam, mat, mat2
    if(tam == 3):
        tam=4
    else:
        tam=3
    print(tam)
    mat = Matriz(tam,tam)
    mat2 = Matriz(tam, tam)
    mat.monta()
    mat2.monta()


def embaralha():
    for x in range(2):
        mat.embaralha()

menu = Tk()
menu.title("8-16 Puzlle")
menu.geometry("500x500")


if(tam == 3):
    label = Label(menu, text=mat.mat[0][0], font="Arial")
    label1 = Label(menu, text=mat.mat[0][1], font="Arial")
    label2 = Label(menu, text=mat.mat[0][2], font="Arial")
    label3 = Label(menu, text=mat.mat[1][0], font="Arial")
    label4 = Label(menu, text=mat.mat[1][1], font="Arial")
    label5 = Label(menu, text=mat.mat[1][2], font="Arial")
    label6 = Label(menu, text=mat.mat[2][0], font="Arial")
    label7 = Label(menu, text=mat.mat[2][1], font="Arial")
    label8 = Label(menu, text=mat.mat[2][2], font="Arial")
elif(tam == 4):
    label = Label(menu, text=mat.mat[0][0], font="Arial")
    label1 = Label(menu, text=mat.mat[0][1], font="Arial")
    label2 = Label(menu, text=mat.mat[0][2], font="Arial")
    label3 = Label(menu, text=mat.mat[0][3], font="Arial")
    label4 = Label(menu, text=mat.mat[1][0], font="Arial")
    label5 = Label(menu, text=mat.mat[1][1], font="Arial")
    label6 = Label(menu, text=mat.mat[1][2], font="Arial")
    label7 = Label(menu, text=mat.mat[1][3], font="Arial")
    label8 = Label(menu, text=mat.mat[2][0], font="Arial")
    label9 = Label(menu, text=mat.mat[2][1], font="Arial")
    label10 = Label(menu, text=mat.mat[2][2], font="Arial")
    label11 = Label(menu, text=mat.mat[2][3], font="Arial")
    label12 = Label(menu, text=mat.mat[3][0], font="Arial")
    label13 = Label(menu, text=mat.mat[3][1], font="Arial")
    label14 = Label(menu, text=mat.mat[3][2], font="Arial")
    label15 = Label(menu, text=mat.mat[3][3], font="Arial")


if(tam==3):
    label.grid(row=0, column=0)
    label1.grid(row=0, column=1)
    label2.grid(row=0, column=2)
    label3.grid(row=1, column=0)
    label4.grid(row=1, column=1)
    label5.grid(row=1, column=2)
    label6.grid(row=2, column=0)
    label7.grid(row=2, column=1)
    label8.grid(row=2, column=2)
elif(tam==4):
    label.grid(row=0, column=0)
    label1.grid(row=0, column=1)
    label2.grid(row=0, column=2)
    label3.grid(row=0, column=3)
    label4.grid(row=1, column=0)
    label5.grid(row=1, column=1)
    label6.grid(row=1, column=2)
    label7.grid(row=1, column=3)
    label8.grid(row=2, column=0)
    label9.grid(row=2, column=1)
    label10.grid(row=2, column=2)
    label11.grid(row=2, column=3)
    label12.grid(row=4, column=0)
    label13.grid(row=4, column=1)
    label14.grid(row=4, column=2)
    label15.grid(row=4, column=3)


button = tkinter.Button(menu, text="Algoritmo A*", command=clique1)
button2 = tkinter.Button(menu, text="Algoritmo Best First", command=clique2)
button3 = tkinter.Button(menu, text="Trocar 8-16", command=troca)
button4 = tkinter.Button(menu, text="Embaralhar", command=embaralha)

button.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=4, column=0)
button4.grid(row=4, column=1)


#mat2.mostra()
#mat.sobe()
#print(mat.isEqual(mat2.getMatriz()))

#while mat.isEqual(mat2.getMatriz()).all():
 #   mat.embaralha()
#mat.mostra()

#mat.qtdpecas(mat2.getMatriz())
print("inicia bestfirst")


#sol.bestfirst(mat,mat2)
#sol.a_estrla(mat,mat2)
menu.mainloop()
