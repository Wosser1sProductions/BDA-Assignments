# write your code here
a = 0
a += int(input())
a += int(input()) * 2
a += int(input()) * 5
a += int(input()) * 10
a += int(input()) * 20

print("You have ", a // 100, ".", a % 10, a % 1, " euro!", sep="")