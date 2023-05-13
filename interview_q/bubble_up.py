

def bubble_up(l):
    #  create a bubble up algorithm to assort an array
    n = len(l)
    for i in range(n):
        flag = True
        for j in range(n-1):
            if l[j] > l[j+1]:
                (l[j], l[j+1]) = (l[j+1], l[j])
            flag = False
            
        if flag:
            break

    return l