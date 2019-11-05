def ss_helper(s, current):
    if len(s) == 0:
        return [current]
    else:
        head = s[0]
        tail = s[1:]
        includedsets = ss_helper(tail, current + [head])
        excludedsets = ss_helper(tail, current)
        return includedsets+excludedsets



def subsets(s):
    return ss_helper(s, [])
x = input()
s = []
for element in x.split():
    s.append(int(element))

for i in subsets(s):
    for j in i:
        print(j, end=" ")
    print()