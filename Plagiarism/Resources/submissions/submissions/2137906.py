woord= input()
lengthe=len(woord)
i=0
teller=0
prindbaar=0
for x in "abcdefghijklmnopqrstuvwxyz":
    i=0
    prindbaar=0
    while i+1< lengthe+1:
        if woord[i] == x:
            prindbaar+=1
            i+=1
        elif i+1 == lengthe:
            i+=1
        else:
            i+=1
    print(x,": ", prindbaar, sep="")
teller+=1