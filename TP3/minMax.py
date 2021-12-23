
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



def minMaxDecision(s):
    maxScore = -2
    action = None
    for a in actionsPossibles(s):
        aux = minValue(resultat(s, a))
        if aux > maxScore:
            maxScore = aux
            action = a
    return action


def minValue(s):
    if terminal(s):  # dans ce cas min ne peux pas jouer => max a gagné
        return 1
    score = 9999
    for a in actionsPossibles(s):
        score = min(score, maxValue(resultat(s, a)))
    return score


def maxValue(s):
    if terminal(s):  # dans ce cas max ne peux pas jouer => min a gagné
        return -1
    score = -9999
    for a in actionsPossibles(s):
        score = max(score, minValue(resultat(s, a)))
    return score




def jeu():
    print("Merci de saisir un nombre n supérieur ou égal à 3: ")
    n = int(input())
    print("L'ordinateur va commencer le jeu")
    tour = 0
    s = [n]
    while(not (terminal(s))):
        if tour == 0:
            a = minMaxDecision(s)
            print("Action faite par l'ordinateur: ", minMaxDecision(s))
            s = resultat(s, a)
            print("Etat du jeu aprés l'action de l'ordinateur", s)
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
            tour=0
    if tour==0:
        print("Félicitations! Tu as gagngé!")
    else:
        print("Perdu :(")



def printActions(actions):
    for i in range(len(actions)):
        print(i+1, ": ", actions[i])

jeu()
