n = input("n")
m = input("m")
teprinten=""
def functie_voornu (n,m,tp):
    n=int(n)
    m=int(m)
    for i in range (m,n+1):
        if m>0:
            tp += str(i) + " "
            m-=1
            functie_voornu (n-1,m,tp)
        print (teprinten)
        teprinten = ""

functie_voornu (n,m,teprinten)    