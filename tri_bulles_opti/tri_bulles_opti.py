def tri_bulle(tab):
    permutation = True
    comparaisons = 0
    echanges_affections = 0
    passage = 0
    while permutation:
        permutation = False
        passage += 1
        for en_cours in range(0, len(tab) - passage):
            comparaisons += 1
            if tab[en_cours] > tab[en_cours + 1]:
                echanges_affections += 3
                permutation = True
                # On echange les deux elements
                tab[en_cours], tab[en_cours + 1] = \
                    tab[en_cours + 1], tab[en_cours]
    return comparaisons+echanges_affections

