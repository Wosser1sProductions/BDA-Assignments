# write your code here

c1 = float(input("Hoeveel 1 eurocenten heb je:"))
c2 = float(input("Hoeveel 2 eurocenten heb je:"))
c5 = float(input("Hoeveel 5 eurocenten heb je:"))
c10 = float(input("Hoeveel 10 eurocenten heb je:"))
c20 = float(input("Hoeveel 20 eurocenten heb je:"))

total = c1 * 1 + c2 * 2 + c5 * 5 + c10 * 10 + c20 * 20

print("You have " + str(total / 100.00) + " euro!", sep="")