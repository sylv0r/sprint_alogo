from random import randint
from tri_bulles_opti import tri_bulles_opti
from selection import selction


def stat(minimum: int, maximum: int, step: int, nbr: int, tri: str):
    if maximum>minimum and step>0:
        diff = maximum - minimum
        diff = (diff // step) + 1

        taille_tableau = minimum

        for _ in range(diff):
            total = 0
            for _ in range(nbr):
                tableau = [randint(0, taille_tableau) for _ in range(0, taille_tableau)]
                if tri == "bulles_opti":
                    total += selction.tri_selction(tableau)
            print(taille_tableau, total/nbr)
            taille_tableau += step
    else:
        print('Veuillez rentrer des valeurs correctes')


stat(10, 20, 5, 10, "bulles_opti")
