def _get_smaller_matrix(matrix, row_number):
    new_matrix = []
    for line_number in range(1, len(matrix)):
        new_line = []
        for element_number in range(len(matrix[line_number])):
            if element_number != row_number:
                new_line.append(matrix[line_number][element_number])
        new_matrix.append(new_line)
    return new_matrix
    
    
def matrix_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det_value = 0
        for i in range(len(matrix[0])):
            if i%2 == 0:
                det_value += matrix[0][i] * matrix_determinant(_get_smaller_matrix(matrix, i))
            else: 
                det_value -= matrix[0][i] * matrix_determinant(_get_smaller_matrix(matrix, i))
        return det_value
        
        
# Test
# matrix_determinant([[7, 8, 9], [4, 2, 1], [9, 8, 1]])
# should be 124   
