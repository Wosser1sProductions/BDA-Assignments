import sys

p = ["A", "C", "G", "T"]


def perm(nlist, m):
    if m == 0:
        yield []
        return
    for list_i in nlist:
        temp = list(nlist)
        for p in perm(temp, m - 1):
            yield [list_i] + p


combination = int(input())
mygenerator = perm(p, combination)
for i in mygenerator:
    for j in i:
        print(j, end="")
    print()