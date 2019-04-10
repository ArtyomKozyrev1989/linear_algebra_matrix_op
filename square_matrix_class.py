class SquareMatrix:
    
    def __init__(self, matrix):
        if type(matrix) != list:
            raise TypeError("matrix should be list of lists")
        for line in matrix:
            if type(line) != list:
                raise TypeError("matrix should be list of lists")
            if len(matrix) != len(line):
                raise TypeError("matrix should be square")
            for element in line:
                if type(element) != float and type(element) != int:
                    raise TypeError("Elements of matrix should be integer or float")
                else:
                    self.matrix = matrix
                    self.determinant = SquareMatrix._calculate_matrix_determinant(self.matrix)
                    
                    
    def __str__(self):
        full_matrix = ""
        for i in range(len(self)):
            line = "  {:^22}  " * len(self)
            full_matrix += line.format(*self.matrix[i]) + "\n\n"
        return full_matrix
        
                                
    def __repr__(self):
        return "SquareMatrix({})".format(self.matrix)
    
    
    def _get_smaller_matrix(matrix, row_number, gl_line_number):
        new_matrix = []
        for line_number in range(0, len(matrix)):
            if line_number != gl_line_number:
                new_line = []
                for element_number in range(len(matrix[line_number])):
                    if element_number != row_number:
                        new_line.append(matrix[line_number][element_number])
                new_matrix.append(new_line)
        return new_matrix
    
    
    def _calculate_matrix_determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det_value = 0
            for i in range(len(matrix[0])):
                if i%2 == 0:
                    det_value += matrix[0][i] * SquareMatrix._calculate_matrix_determinant(
                        SquareMatrix._get_smaller_matrix(matrix, i, 0))
                else: 
                    det_value -= matrix[0][i] * SquareMatrix._calculate_matrix_determinant(
                        SquareMatrix._get_smaller_matrix(matrix, i, 0))
            return det_value
        
    
    def transposition(self):
        new_matrix = []
        k = 0 
        while k < len(self.matrix):
            new_matrix.append([])
            for line in self.matrix:
                new_matrix[k].append(line[k])
            k+=1
        return SquareMatrix(new_matrix)
        
        
    def inverse(self):
        if self.determinant != 0:
            new_matrix = []
            for line in range(len(self)):
                new_line = []
                for row in range(len(self)):
                    if (row + line)%2 == 0:
                        new_line.append(
                            SquareMatrix(SquareMatrix._get_smaller_matrix(self.matrix, row, line)).determinant)
                    else:
                        new_line.append(
                            -1 * SquareMatrix(SquareMatrix._get_smaller_matrix(self.matrix, row, line)).determinant)
                new_matrix.append(new_line)
            minor_matrix = SquareMatrix(new_matrix)
            inversed_matrix = (1/self.determinant) *  minor_matrix.transposition()
            return inversed_matrix
        else:
            return "Determinant is 0, there is no inverse matrix"
        
    
    def __len__(self):
        return len(self.matrix)
        
        
    def __add__(self, another):
        if type(another) != SquareMatrix:
            raise TypeError("You can add only another SquareMatrix")
        if len(self) != len(another):
            raise ValueError("The matrixes should have the same dimensions")
        else:
            new_matrix = []
            for line_index in range(len(self)):
                new_line = []
                for item_index in range(len(self)):
                    new_line.append(self.matrix[line_index][item_index] + another.matrix[line_index][item_index])
                new_matrix.append(new_line)                
            return SquareMatrix(new_matrix)
    
    
    def __sub__(self, another):
        if type(another) != SquareMatrix:
            raise TypeError("You can substract only another SquareMatrix")
        if len(self) != len(another):
            raise ValueError("The matrixes should have the same dimensions")
        else:
            new_matrix = []
            for line_index in range(len(self)):
                new_line = []
                for item_index in range(len(self)):
                    new_line.append(self.matrix[line_index][item_index] - another.matrix[line_index][item_index])
                new_matrix.append(new_line)                
            return SquareMatrix(new_matrix)
        
    
    def __eq__(self, another):
        if len(self) != len(another):
            return False
        else:
            for line_index in range(len(self)):
                for item_index in range(len(self)):
                    if self.matrix[line_index][item_index] != another.matrix[line_index][item_index]:
                        return False
            return True
    
    
    def __mul__(self, another):
        if type(another) == int or type(another) == float:
            new_matrix = []
            for line_index in range(len(self)):
                new_line = []
                for item_index in range(len(self)):
                    new_line.append(another * self.matrix[line_index][item_index])
                new_matrix.append(new_line)
            return SquareMatrix(new_matrix)
        elif type(another) == SquareMatrix:
            if len(self) != len(another):
                raise ValueError("The matrixes should have the same deimensions")
            else:
                another_tr = another.transposition()
                new_matrix = []
                for i in range(len(self)):
                    new_line = []
                    for j in range(len(self)):
                        el_sum = 0
                        for z in range(len(self)):
                            el_sum += self.matrix[i][z] * another_tr.matrix[j][z]
                        new_line.append(el_sum)
                    new_matrix.append(new_line)
                return SquareMatrix(new_matrix)     
        else:
            raise ValueError("SquareMatrix can be multiplied only by integer, float or SquareMatrix")
            
            
    def __rmul__(self, another):
        if type(another) == int or type(another) == float:
            new_matrix = []
            for line_index in range(len(self)):
                new_line = []
                for item_index in range(len(self)):
                    new_line.append(another * self.matrix[line_index][item_index])
                new_matrix.append(new_line)
            return SquareMatrix(new_matrix)
        else:
            raise ValueError("SquareMatrix can be multiplied only by integer, float or SquareMatrix")
