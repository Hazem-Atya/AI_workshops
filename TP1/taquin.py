import copy
import sys
but = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
initial = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
#initial = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
#initial = [[2, 3], [1, 0]]
#but = [[0, 1], [3, 2]]
visited = set()


def toString(matrix):
    ans = ''
    for line in matrix:
        for element in line:
            conv = str(element)
            ans += str(element)
    return ans
# class taquin:

#   etat_initial = []
#  etat_but = []

# def __init__(self, initial, but):
#    self.etat_initial = initial
#   self.etat_but = but

# Actions


n = len(initial)


def etatValid(i, j):
    if i < 0 or j < 0 or i >= n or j >= n:
        return False
    return True


def actionsPossibles(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans = []
    i = 0
    while i < 4:
        if etatValid(x+dx[i], y+dy[i]):
            ans.append((x+dx[i], y+dy[i]))
        i += 1
    return ans


def transition(etatDepart):
    etatsSuivants = []
    i = 0
    while i < len(etatDepart):
        j = 0
        while (j < len(etatDepart[i])):
            if etatDepart[i][j] == 0:
                actions = actionsPossibles(i, j)
                for (k, l) in actions:
                    aux = copy.deepcopy(etatDepart)
                    aux[i][j] = etatDepart[k][l]
                    aux[k][l] = 0
                    etatsSuivants.append(aux)
                 

            j += 1
        i += 1

    return etatsSuivants


def bfs(etatInitial):

    queue = []
    visitedNodes = 1
    if (etatInitial == but):
        return visitedNodes
    queue.append(etatInitial)

    while(len(queue) > 0):
        etatParent = queue[0]
        visited.add(toString(etatParent))
        queue.pop(0)

        children = transition(etatParent)

        #print("parent", etatParent)
        for etat in children:
        
            if (etat == but):
                #print('visitedNodes:',visitedNodes)
                return visitedNodes
            if toString(etat) not in visited:
                visitedNodes += 1
                queue.append(etat)


#sys.stdout = open('test.txt', 'w')

print(toString(initial))
print("nb=", bfs(initial))
#print(visited)

