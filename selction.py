
Tab = [1,9,2,8,3,7,4,6,5]

def tri_selction(Tab) :
    nomb = len(Tab)
    for cours in range(0,nomb) :
        plus_petit = cours
        for j in range (cours + 1,nomb) :
            print(cours, j)
            if Tab[j] < Tab[plus_petit] :
                plus_petit = j
        if min is not cours:
            temp = Tab[cours]
            Tab[cours] = Tab[plus_petit]
            Tab[plus_petit] = temp
    return Tab


print(tri_selction(Tab))

