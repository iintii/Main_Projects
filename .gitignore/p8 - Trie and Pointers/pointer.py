def move_zeroes_to_the_end(alist):
    p1 = 0
    for p2 in range(len(alist)):
        if alist[p2] != 0: 
            alist[p1] = alist[p2]
            p1 += 1 #Increment p1 only when its non zero
    return alist
