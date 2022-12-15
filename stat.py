from random import randint
from tri_bulles_opti import tri_bulles_opti
from selection import selection
from insertion import insertion


def stat(minimum: int, maximum: int, step: int, nbr: int, tri: str) -> None:
    #vérifie que les paramètres sont corrects
    if maximum > minimum and step > 0:
        #calcul le nombre de boucle nécessaire
        diff = maximum - minimum
        diff = (diff // step) + 1

        #initilise la taille du tableau à la taille minimum
        taille_tableau = minimum

        #boucle sur le nombre de liste de tableaux
        for _ in range(diff):
            total = 0
            #boucle sur le nombre de tableaux
            for _ in range(nbr):
                #créer une liste par compréhension de la taille voulue
                tableau = [randint(0, taille_tableau) for _ in range(0, taille_tableau)]
                #choisi la bonne méthode de tri parmi les 4
                if tri == "bulles_opti":
                    total += tri_bulles_opti.tri_bulle(tableau)
                elif tri == "selection":
                    total += selection.tri_selction(tableau)
                elif tri == "insertion":
                    total += insertion.tri_insertion(tableau)
                else:
                    print('Tri inconnu')
                    break
            #dis le résultat et passe au pas suivant
            print(taille_tableau, total / nbr)
            taille_tableau += step
    else:
        print('Veuillez rentrer des valeurs correctes')


stat(10, 20, 5, 10, "insertion")
