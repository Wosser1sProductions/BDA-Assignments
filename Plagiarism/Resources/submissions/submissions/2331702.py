c1 = input()
c2 = input()
c5 = input()
c10 = input()
c20 = input()
cents = (c1 * 1 + c2 * 2 + c5 * 5) % 10
cents10 = ((c1 * 1 + c2 * 2 + c5 * 5) // 10 + c10 * 10 + c20 * 20) % 100
euros = ((c1 * 1 + c2 * 2 + c5 * 5) // 10 + c10 * 10 + c20 * 20) // 100
print("You have ", euros, ".", cents10, cents, "euro!", sep = "")