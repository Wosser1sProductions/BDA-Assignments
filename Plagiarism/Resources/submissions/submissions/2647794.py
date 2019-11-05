list_int = int(input())
list = [i for i in range(1, list_int+1)]
n = int(input())

def subsets(list, r):
    data = [0] * r
    list_last_index = len(list) - 1
    subsets_rec(list, data, 0, list_last_index, 0, r)


def subsets_rec(lst, prefix, start, end, index, r):
    if index == r:
        for j in range(r):
            print(prefix[j], end=" ")
        print()
        return

    i = start
    while i <= end and end - i + 1 >= r - index:
        prefix[index] = lst[i]
        subsets_rec(lst, prefix, i + 1,
                    end, index + 1, r)
        i += 1


subsets(list, n)