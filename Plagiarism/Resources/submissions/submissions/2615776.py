x = int(input("geef nummer: "))
y = int(input("geef nummer: "))

totaal =1
for i in range(0, y ):
    totaal *=  int((x-i))/int((y-i))
print(totaal)
# write your code here