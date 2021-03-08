from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for i in range(0, len(matrix)-1, 2):
        draw_line(matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1], screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = int(x0)
        yt = int(y0)
        x0 = int(x1)
        y0 = int(y1)
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line


# added for generating the image
def edge_points(edges1, x, y):
    x0 = edges1[0]
    y0 = edges1[1]
    midpoints = [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0]
    midpoints[6] = (x + x0) / 2
    midpoints[7] = (y + y0) / 2
    midpoints[2] = (x + midpoints[6]) / 2
    midpoints[3] = (y + midpoints[7]) / 2
    midpoints[0] = (x + midpoints[2]) / 2
    midpoints[1] = (y + midpoints[3]) / 2
    midpoints[4] = (midpoints[2] + midpoints[6]) / 2
    midpoints[5] = (midpoints[3] + midpoints[7]) / 2
    midpoints[10] = (x0 + midpoints[6]) / 2
    midpoints[11] = (y0 + midpoints[7]) / 2
    midpoints[12] = (x0 + midpoints[10]) / 2
    midpoints[13] = (y0 + midpoints[11]) / 2
    midpoints[8] = (midpoints[6] + midpoints[10]) / 2
    midpoints[9] = (midpoints[7] + midpoints[11]) / 2
    edges1[0] = x
    edges1[1] = y
    for i in range(len(midpoints)):
            edges1.append(int(midpoints[i]))
    edges1.append(x0)
    edges1.append(y0)

def curve_stitch(matrix, edges1, edges2):
    for i in range(0, len(edges1), 2):
        add_edge(matrix, edges1[i], edges1[i+1], 0, edges2[16-i], edges2[17-i], 0)
