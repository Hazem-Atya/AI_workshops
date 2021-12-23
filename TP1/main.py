import taquinC
import sys
from datetime import datetime

#sys.stdout = open('test.txt', 'w')

but = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
initial = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
before = datetime.now()

#taq2=taquinC.Taquin([[2,3],[1,0]], [[0,1],[3,2]])

#taq2.bfs()
taq3= taquinC.Taquin(initial, but)
taq3.bfs()
after = datetime.now()
#print(ans)
print("Temps de l'exécution:",after-before)
