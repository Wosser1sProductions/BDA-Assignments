# write your code here
a = input("how many of 1 eurocent?")
a = float(a)
b = input("how many of 2 eurocent?")
b = float(b)
c = input("how many of 5 eurocent?")
c = float(c)
d = input("how many of 10 eurocent?")
d = float(d)
e = input("how many of 20 eurocent?")
e = float(e)

som = (a+(2*b)+(5*c)+(10*d)+(20*e))
som = float(som)
som2 = som//100
som5 = som2
som2 = int(som2)
som3 = som2*100
som3 = float(som3)
som4 = som-som3

print("You have", som5, ".", som4,"euro!")
