sp = []
while s := input():
    sp.append([int(x) for x in s.split(',')])
matrix1 = sp[:len(sp[0])]
matrix2 = sp[len(sp[0]):]
result_matrix = [[0] * len(matrix1) for _ in range(len(matrix1))]
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        for k in range(len(matrix1)):
            result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
for elem in result_matrix:
    print(','.join([str(x) for x in elem]))
