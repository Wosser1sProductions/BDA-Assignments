c1 = str(input())
c2 = str(input())
c5 = str(input())
c10 = str(input())
c20 = str(input())
cents = (c1 * 1 + c2 * 2 + c5 * 5) % 10
cents10 = ((c1 * 1 + c2 * 2 + c5 * 5) // 10 + c10 * 10 + c20 * 20) % 100
euros = ((c1 * 1 + c2 * 2 + c5 * 5) // 10 + c10 * 10 + c20 * 20) // 100
print("You have ", str(euros), ".", str(cents10), str(cents), "euro!", sep="")