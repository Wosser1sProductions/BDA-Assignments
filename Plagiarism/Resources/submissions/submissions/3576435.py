# write your code here

sum = int(input())
sum += int(input())* 2
sum += int(input())*5
sum += int(input())*10
sum += int(input())*20

euro = sum // 100
sum -= euro*100

print("You have", euro, end="")
print(".", end="")
print(sum, "euro!")