def diagonalDiference(matrix):
    diagonal = 0
    reverse = 0

    for i in range(len(matrix)):
        diagonal = diagonal +  matrix[i][i]
        reverse = reverse + matrix[i][len(matrix)-1-i]

    return abs(diagonal - reverse)
