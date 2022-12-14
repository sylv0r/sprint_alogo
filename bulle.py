def bulle(tab):
    for i in range(len(tab)):
        for j in range(0, len(tab) - i - 1):
            if tab[j + 1] < tab[j]:
                tab[j] = tab[j + 1]
                tab[j + 1] = tab[j]
    print(tab)


tab = [1, 2, 1, 2, 9, 5, 2, 5]
bulle(tab)

