n = int(input("Give value, greater than 0: "))
while n < 1:
    n = int(input("Give value, greater than 0: "))

bases = ["A", "C", "G", "T"]

if n == 1:
    for i in bases:
        print(i)


if n == 2:
    for i in range(len(bases)):
        for j in range(len(bases)):
            print(bases[i], bases[j], sep="")

if n == 3:
    for i in range(len(bases)):
        for j in range(len(bases)):
            for k in range(len(bases)):
                print(bases[i], bases[j], bases[k], sep="")

if n == 4:
    for i in range(len(bases)):
        for j in range(len(bases)):
            for k in range(len(bases)):
                for l in range(len(bases)):
                    print(bases[i], bases[j], bases[k], bases[l], sep="")

if n == 5:
    for i in range(len(bases)):
        for j in range(len(bases)):
            for k in range(len(bases)):
                for l in range(len(bases)):
                    for m in range(len(bases)):
                        print(bases[i], bases[j], bases[k], bases[l], bases[m], sep="")
