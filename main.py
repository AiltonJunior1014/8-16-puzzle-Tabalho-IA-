from matriz import Matriz


mat = Matriz(3, 3)
mat2 = Matriz(3, 3)

mat.monta()
mat2.monta()
mat2.mostra()
#mat.sobe()
for x in range (4):
    mat.embaralha()
mat.mostra()

#mat.qtdpecas(mat2.getMatriz())

mat.bestfirst(mat2)


