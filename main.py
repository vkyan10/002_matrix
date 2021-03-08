from display import *
from draw import *
from matrix import *

print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
m2 = []
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

print("\nTesting ident. m1 =")
m1 = new_matrix()
ident(m1)
print_matrix(m1)

print("\nTesting Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)

print("\nTesting Matrix mult. m1 =")
m1 = []
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print_matrix(m1)

print("\nTesting Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)
print()


screen = new_screen()

color = [255, 255, 255]
matrix = []
edges = [[250, 298], [292, 274], [292, 226], [250, 202], [208, 226], [208, 274]]
for i in range(len(edges)):
    edge_points(edges[i], 250, 250)
    #print(edges[i])
for i in range(6):
    curve_stitch(matrix, edges[i], edges[(i+1)%6])

edges = [[250, 346], [298, 333], [298, 333],
         [333, 298], [346, 250], [346, 250],
         [333, 202], [298, 167], [298, 167],
         [250, 154], [202, 167], [202, 167],
         [167, 202], [154, 250], [154, 250],
         [167, 298], [202, 333], [202, 333]]

for i in range(18):
    if i <= 1:
        edge_points(edges[i], 250, 298)
    elif i <= 4:
        edge_points(edges[i], 292, 274)
    elif i <= 7:
        edge_points(edges[i], 292, 226)
    elif i <= 10:
        edge_points(edges[i], 250, 202)
    elif i <= 13:
        edge_points(edges[i], 208, 226)
    elif i <= 16:
        edge_points(edges[i], 208, 274)
    else:
        edge_points(edges[i], 250, 298)
    # print(edges[i])
for i in range(18):
    curve_stitch(matrix, edges[i], edges[(i + 1) % 18])

draw_lines(matrix, screen, color)
# print_matrix(matrix)
display(screen)

