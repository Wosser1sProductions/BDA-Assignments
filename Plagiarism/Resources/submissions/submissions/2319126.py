# write your code here
a=int(input("stukken van 1 cent"))
b=int(input("stukken van 2 cent"))
c=int(input("stukken van 5 cent"))
d=int(input("stukken van 10 cent"))
e=int(input("stukken van 20 cent"))

a=float(a*0.01)
b=float(b*0.02)
c=float(c*0.05)
d=float(d*0.1)
e=float(e*0.2)

euros=int(a+b+c+d+e)
cents_2=int(((a+b+c+d+e)*100)%10)
cents=int(((a+b+c+d+e)*100)%10 - cents_2 )


print("You have "+ str(euros) + "." + str(cents) + str(cents_2) + " euro!", sep="")