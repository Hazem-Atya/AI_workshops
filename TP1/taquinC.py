import copy
import sys

# initial = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
# initial = [[2, 3], [1, 0]]
# but = [[0, 1], [3, 2]]


def toString(matrix):
    ans = ''
    for line in matrix:
        for element in line:
            ans += str(element)
    return ans


class Taquin:

    etatbut = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    etat_initial = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
    n = 0
    visited = set()

    def __init__(self, initial, but):
        self.etat_initial = initial
        self.etat_but = but
        visited = set()
        self.n = len(initial)

    def __len__(self):
        return len(self.etatInitial)
# vérifie si la case (i,j) est incluse dans la matrice

    def etatValid(self, i, j):
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            return False
        return True

# cette fonction retourne une liste des actions possibles
# à partir d'une position (x,y)
    def actionsPossibles(self, x, y):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        ans = []
        i = 0
        while i < 4:
            if self.etatValid(x+dx[i], y+dy[i]):
                ans.append((x+dx[i], y+dy[i]))
            i += 1
        # print(ans)
        return ans

# cette fonction retourne les états suivants (une liste
# de matrices), en appliquant les actions possibles
    def transition(self, etatDepart):
        etatsSuivants = []
        i = 0
        while i < len(etatDepart):

            j = 0
            while (j < len(etatDepart[i])):
                if etatDepart[i][j] == 0:
                    actions = self.actionsPossibles(i, j)
                    for (k, l) in actions:
                        aux = copy.deepcopy(etatDepart)
                        aux[i][j] = etatDepart[k][l]
                        aux[k][l] = 0
                        etatsSuivants.append(aux)
                j += 1
            i += 1
        return etatsSuivants

    def bfs(self):
        queue = []
        visitedNodes = 0
        if (self.etat_initial == self.etat_but):
            return visitedNodes
        queue.append(self.etat_initial)
        while(len(queue) > 0):
            #if(visitedNodes!=len(self.visited)):
                #print("(visitedNodes= ",visitedNodes,", len(visited)= ",len(self.visited))
            etatParent = queue[0]
            if(toString(etatParent) in self.visited):
                queue.pop(0)
                continue
            self.visited.add(toString(etatParent))
            queue.pop(0)
            visitedNodes += 1
            children = self.transition(etatParent)
            for etat in children:
                if (etat == self.etat_but):
                    # print('visitedNodes:',visitedNodes)
                    #print("length of visited", len(self.visited))
                    print("visitedNodes=", visitedNodes)
                    return
                if (toString(etat) not in self.visited):
                    queue.append(etat)
