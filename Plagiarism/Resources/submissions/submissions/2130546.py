# write your code here

x = int(input("x"))
y = int(input("y"))

output = 1

for i in range(y):
    output = output * ((x-i)/(y-i))
    
print(output)
