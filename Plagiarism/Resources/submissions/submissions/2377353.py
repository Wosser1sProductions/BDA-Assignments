# write your code here
x=int(input("give an integer"))
product=1
sum=0
for i in range(x):
    product*=(i+1)
    sum+=product
print(sum)
