def tri_insertion(tableau):
    a=0
    c=0
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        a += 2
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            a += 2
            tableau[j]=tableau[j-1]
            j = j-1
        #on insère l'élément à sa place
        a += 1
        tableau[j]=en_cours
    return a+c