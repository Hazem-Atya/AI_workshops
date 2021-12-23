
# cette fonction retourne les actions possibles
# à partir d'un état s qui est une liste contenant
# chaque action est un triplet, le premier élement est l'éelemnt à éclater
# les deux autres élements sont les deux nouveaux piles obetenues.
def actionsPossibles(s):
    ans = []
    for index in range(len(s)):
        for i in range(s[index]//2+1):
            j = s[index]-i
            if j != i and i != 0 and j != 0:
                ans.append((index, i, j))
    return ans

# cette fonction retourne un état s1 aprés avoir appliqué une action a
# à un état s (l'action a est un tuple contenant 3 valeurs comme dans la fonction précédente)


def resultat(s, a):
    s1 = s.copy()
    s1.pop(a[0])
    s1.append(a[1])
    s1.append(a[2])
    return s1

# cette fonction retourne un booléen:
#   - Vrai si   le jeu est terminé
#   - Faux sinon


def terminal(s):
    if len(actionsPossibles(s)) == 0:
        return True
    return False


# la variable score contient le score du jeu
# elle va prendre la valeur 1 si max gagne et -1 sinon

def alphaBeta(s):
    branchesElagees = 0
    (action, v,branchesElagees) = maxValue(s, -9999, 9999, branchesElagees)
    print()
    return (action, branchesElagees)


def minValue(s, alpha, beta, branchesElagees):
    if terminal(s):  # dans ce cas min ne peux pas jouer => max a gagné
        return (None, 1,0)
    (action, v) = (None, 9999)
    count = 0
    possibleActions = actionsPossibles(s)
    for a in possibleActions:
        count += 1
        (a1, v1,branchesElagees) = maxValue(resultat(s, a), alpha, beta, branchesElagees)
        if(v1 < v):
            action = a
            v = v1
        if v <= alpha:
            branchesElagees += len(possibleActions)-count
            return (action, v,branchesElagees)
        beta = min(beta, v)
    return (action, v,branchesElagees)


def maxValue(s, alpha, beta, branchesElagees):
    if terminal(s):  # dans ce cas max ne peux pas jouer => min a gagné
        return (None, -1,0)
    (action, v) = (None, -9999)
    count = 0
    possibleActions = actionsPossibles(s)
    for a in possibleActions:
        (a1, v1,branchesElagees) = minValue(resultat(s, a), alpha, beta, branchesElagees)
        if(v1 > v):
            action = a
            v = v1
        if v >= beta:
            branchesElagees += len(possibleActions)-count
            return (action, v,branchesElagees)
        alpha = max(alpha, v)
    return (action, v,branchesElagees)


def jeu():
    print("Merci de saisir un nombre n supérieur ou égal à 3: ")
    n = int(input())
    print("L'ordinateur va commencer le jeu")
    tour = 0
    s = [n]
    while(not (terminal(s))):
        if tour == 0:
            (a, nbBranches) = alphaBeta(s)
            print("Action faite par l'ordinateur: ", alphaBeta(s))
            s = resultat(s, a)
            print("Etat du jeu aprés l'action de l'ordinateur", s)
            print("Nombre de branches élaguées:", nbBranches)
            tour = 1
        else:
            print("À toi de jouer !")
            print("Merci de saisir l'indice de l'action à faire")
            actions = actionsPossibles(s)
            printActions(actions)
            choix = int(input())
            choix -= 1
            s = resultat(s, actions[choix])
            print("Etat du jeu aprés ton action: ", s)
            tour = 0
    if tour == 0:
        print("Félicitations! Tu as gagngé!")
    else:
        print("Perdu :(")


def printActions(actions):
    for i in range(len(actions)):
        print(i+1, ": ", actions[i])


jeu()
# print(alphaBeta([6]))
