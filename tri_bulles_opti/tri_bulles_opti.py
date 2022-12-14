tableau = [12, 3, 45, 67, 87, 65, 57, 8, 90, 9876, 43, 2]


def tri_bulle(tableau):
    permutation = True
    passage = 0
    while permutation:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = \
                    tableau[en_cours + 1], tableau[en_cours]
    return tableau


print(tri_bulle(tableau))
