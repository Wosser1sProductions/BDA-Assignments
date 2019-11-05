def subset_help(l, result):
    if len(l) == 0:
        for i in result:
            print(i, end=" ")
    else:
        first = l[0]
        rest = l[1:]
        # don't add
        subset_help(rest, result)
        # add
        subset_help(rest, result + [first])

def subsets(l):
    subset_help(l, [])