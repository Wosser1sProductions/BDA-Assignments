euro1 = input("schrijf hier het aantal 1 eurocents")
euro2 = input("schrijf hier het aantal 2 eurocents")
euro5 = input("schrijf hier het aantal 5 eurocents")
euro10 = input("schrijf hier het aantal 10 eurocents"
euro20 = input("schrijf hier het aantal 20 eurocents")
x = (int(euro10)*10) + int(euro1) + (int(euro5)*5) + (int(euro2)*2) + (int(euro20)*20)
print("You have", (int(x)/100), "euro")
