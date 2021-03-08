"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

# print the matrix such that it looks like
# the template in the top comment
def print_matrix(matrix):
    for i in range(4):
        for j in range(len(matrix)):
            print(float(matrix[j][i]), end=' ')
        print()

# turn the parameter matrix into an identity matrix
# you may assume matrix is square
def ident(matrix):
    for i in range(4):
        for j in range(4):
            if i != j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1

# multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2
def matrix_mult(m1, m2):
    mtemp = new_matrix()
    for i in range(4):  # m1 rows
        for j in range(len(m2)):  # m2 columns
            for k in range(4):  # m1 columns = m2 rows = 4
                mtemp[j][i] += m1[k][i] * m2[j][k]
    for i in range(len(m2)):
        for j in range(4):
            m2[i][j] = mtemp[i][j]





def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
