def lucky_numbers(n):
    p=[]
    x = 0
    for i in range (1, n+1):
        p.append (i)
    while len (p)>= x+1:
        x+=1
        for j in range (0,int (n/x)):
            p.remove (p[j*x])
            if j == len(p)
    return p