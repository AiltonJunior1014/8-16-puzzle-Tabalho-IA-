from matriz import Matriz
from solucao import Solucao


mat = Matriz(3, 3)
mat2 = Matriz(3, 3)

mat.monta()
mat2.monta()
#mat2.mostra()
#mat.sobe()
print(mat.isEqual(mat2.getMatriz()))
#for x in range (2):
mat.embaralha()
#while mat.isEqual(mat2.getMatriz()).all():
 #   mat.embaralha()
mat.mostra()

#mat.qtdpecas(mat2.getMatriz())
print("inicia bestfirst")

sol = Solucao(3,3)

#sol.bestfirst(mat,mat2)
sol.a_estrla(mat,mat2)

