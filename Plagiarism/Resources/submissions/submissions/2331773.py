c1 = int(input())
c2 = int(input())
c5 = int(input())
c10 = int(input())
c20 = int(input())
cents = (c1 * 1 + c2 * 2 + c5 * 5) % 10
cents10 = ((c1 * 1 + c2 * 2 + c5 * 5) // 10 + c10 * 10 + c20 * 20) % 100
euros = ((c1 * 1 + c2 * 2 + c5 * 5) // 10 + c10 * 10 + c20 * 20) // 100
print("You have ", str(euros), ".", str(cents10), str(cents), "euro!", sep="")