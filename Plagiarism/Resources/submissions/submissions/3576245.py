# write your code here

n = int(input())
sum = 0
for j in range(n):
    product = 1
    for i in range(1, j+1):
        product *= i
    sum += product
    
print(sum)