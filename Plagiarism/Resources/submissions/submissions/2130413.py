x = int(input())
y = int(input())

total = 1;

for i in range(y):
    total*=(x-(i*y))/(y-i)

print(total)