cent1 = int(input("munstukken van 1 eurocent: "))
cent2 = int(input("munstukken van 2 eurocent: "))
cent3 = int(input("munstukken van 5 eurocent: "))
cent4 = int(input("munstukken van 10 eurocent: "))
cent5 = int(input("munstukken van 20 eurocent: "))
som = cent1 + cent2*2 + cent3*5 + cent4*10 + cent5*20
euro = som // 100
ddcent  = (som % 100) // 10
ecent = som % 10
print("You have ", euro, ".", ddcent, ecent, " euro!")