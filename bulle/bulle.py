def bulle(tab):
    comparaison = 0
    affectation = 0
    for i in range(len(tab)):
        for j in range(0, len(tab) - i - 1):
            comparaison += 1
            if tab[j + 1] < tab[j]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
                affectation += 3
    print(comparaison, affectation)
    print(tab)


tab = [1, 2, 1, 2, 9, 5, 2, 5, 6, 0]
bulle(tab)

