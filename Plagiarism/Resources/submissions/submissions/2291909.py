def fibonacci_values(i):
    A = [0, 1]
    if i == 0:
        return([])
    elif i == 1:
        return([0])
    else:
        for aantal in range(2, i):
            A += int(A[aantal-1]) + int(A[aantal-2])
        return(A)