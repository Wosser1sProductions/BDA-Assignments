def lucky_numbers(n):
    p=[]
    x = 0
    for i in range (1, n+1):
        p.append (i)
    while len (p)>= x:
        x+=1
        y = int((len(p)+x)/(x+1))
        for j in range (1,y+1):
            p.remove (p[(j*x)])
    return p