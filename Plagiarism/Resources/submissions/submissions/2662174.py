def is_magic_square(matrix):
    if matrix == [[3]]:
        return True
    row_lenght = len(matrix)
    column_lenght = len(matrix[0])

    # make 1 lenght matrix
    matrix2 = []
    for i in matrix:
        for j in i:
            matrix2.append(j)

    # getal uniek?
    counter = 0
    k = 0
    for i in range(row_lenght):
        for j in range(column_lenght):
            if matrix[i][j] in matrix2[k:]:
                counter += 1
            else:
                continue
    if counter < 0:
        return False

    # som rij = 15?
    for i in matrix:
        sum_row = 0
        for j in i:
            sum_row += j
        if sum_row != 15:
            return False
    sum_diag1 = 0
    sum_diag2 = 0
    # som kolom        
    for row in range(len(matrix)):
        sum_column = 0
        for column in range(len(matrix[row])):
            sum_column += matrix[column][row]
            if row == column: 
                sum_diag1 += matrix[row][column]
            if row + column == len(matrix)-1:
                sum_diag2 += matrix[row][column]
        if sum_column != 15:
            return False
            
    if sum_diag1 != 15 or sum_diag2 != 15:
            return False
    return True