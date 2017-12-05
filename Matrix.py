import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for x in range(width)] for x in range(height)] # can't use g=[[0.0 for 0.0 in range(width)]]
        return Matrix(g)   # why don't use return g ???

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h==1:
            detA=self.g[0][0]
            return detA
        if self.h==2:
            detA=self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
            return detA

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        if self.h==1:
            trace=self.g[0][0]
            return trace
        if self.h==2:
            trace=self.g[0][0]+self.g[1][1]
            return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse=[]
        if self.h==1:
            inverse.append([1/self.g[0][0]])
            return inverse
        if self.h==2:
            row_element=[(self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0])*(1/self.determinant())] # the first element of the first row
            row_element.append(0)                                               # the second element of the first row
            inverse.append(row_element)  # the first row of the inverse matrix
            row_element=[]
            row_element.append(0)
            row_element.append((self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0])*(1/self.determinant()))
            inverse.append(row_element) # the second row of the inverse matrix
            return inverse
                  

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        trans=[]
        for i in range(len(self.h)):
            t_column=[]
            for j in range(len(self.w)):
                t_column.append(self.g[self.w][self.h]) # get each column of the target Matrix
            trans.append(t_column)                # to be each row of the transposed Matrix
        return trans

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        if self.h==other.h and self.w==other.w:
            added_matrix=[]
            for i in range(self.h):
                added_row=[]
                for j in range(self.w):
                    added_row.append(self.g[i][j]+other.g[i][j])
                added_matrix.append(added_row)
            return added_matrix
            
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg_matrix=[]
        for i in range(self.h):
            neg_row=[]
            for j in range (self.w):
                neg_row.append(-1*self.g[i][j])
            neg_matrix.append(neg_row)
        return neg_matrix    

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        if self.h==other.h and self.w==other.w:
            subtracted_matrix=[]
            for i in range(self.h):
                subtracted_row=[]
                for j in range(self.w):
                    subtracted_row.append(self.g[i][j]-other.g[i][j])
                subtracted_matrix.append(subtracted_row)
            return subtracted_matrix
        
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            
