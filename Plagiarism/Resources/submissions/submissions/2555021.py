inp = input().split()
print(inp)

def subset(lst):
    if len(lst) == 1:
        return ['', lst[0]]
    else:
        result = []
        subsub = subset(lst[1:])
        for item in subsub:
            result.append(subsub)
            result.append(lst[0] + subsub)
        return result
    
for x in subset(inp):
    print(x)