
Tab = [10,9,8,7,6,5,4,3,2,1]
#Tab = Tab[::-1]

def tri_selction(Tab) :
    c = 0
    a = 0
    nomb = len(Tab)
    for i in range(0,nomb) :
        mini = i
        a +=1
        for j in range (i + 1,nomb) :
            c += 1
            if Tab[j] < Tab[mini] :
                mini = j
                a +=1
        c +=1
        if min is not i:
            temp = Tab[i]
            Tab[i] = Tab[mini]
            Tab[mini] = temp
            a +=3
    print(c, a)
    print(Tab)
    return Tab

tri_selction(Tab)


