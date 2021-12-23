
def minValue(s, alpha, beta,branchesElagees):
    if terminal(s):  # dans ce cas min ne peux pas jouer => max a gagné
        return (None, 1)
    (action, v) = (None, 9999)
    count = 0
    possibleActions = actionsPossibles(s)
    for a in possibleActions:
        count += 1
        (a1, v1) = maxValue(resultat(s, a), alpha, beta,branchesElagees)
        if(v1 < v):
            action = a
            v = v1
        if v <= alpha:
            branchesElagees += len(possibleActions)-count
            return (action, v)
        beta = min(beta, v)
    return (action, v)


def maxValue(s, alpha, beta,branchesElagees):
    if terminal(s):  # dans ce cas max ne peux pas jouer => min a gagné
        return (None, -1)
    (action, v) = (None, -9999)
    count = 0
    possibleActions = actionsPossibles(s)
    for a in possibleActions:
        (a1, v1) = minValue(resultat(s, a), alpha, beta,branchesElagees)
        if(v1 > v):
            action = a
            v = v1
        if v >= beta:
            branchesElagees += len(possibleActions)-count
            return (action, v)
        alpha = max(alpha, v)
    return (action, v)

