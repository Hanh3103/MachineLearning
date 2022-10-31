
from copy import deepcopy


def transp(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T= []
    for j in range(columns):
        row_of_trans = []
        for row in matrix:
            row_of_trans.append(row[j])
        matrix_T.append(row_of_trans)
    print(matrix_T)

x = [[1,2,3],[4,5,6],[7,8,9]]
#transp(x)

def modified_matrix(matrix, j):
    copy_x = deepcopy(matrix)
    print('dee ' , copy_x)
    #copy_x = matrix[:]
    #print(copy_x)
    if len(matrix) == 2:
        return copy_x
    else:
        copy_x.pop(0)
        for row in copy_x:
            row.pop(j)
        print('r' , copy_x)
        return copy_x


def determinate(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    if rows == 1: # det of 1x1 matrix
        det = matrix[0]
        return det
    elif rows == 2: # det of 2x2 matrix
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det
    else:
        det = 0
        for j in range(columns):
            det += ((-1)**j)*matrix[0][j]*determinate(modified_matrix(matrix,j))
        return det

B = [[1,2,8],[3,5,7],[5,2,7]]
print("The determinant of B --> ",determinate(B))

def multiplikation(matrix, other):
    pass



#arr = x[:]
#arr.pop(0)
#print(arr)


