import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from clip import line_clip

WINDOW_SIZE = 500

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def draw(config):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 1)
    glPointSize(5.0)
    # glBegin(GL_LINES)

    # X-AXIS (from (-1, 0) to (1, 0))
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)

    # Y-AXIS (from (0, 1) to (0, -1))
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)

    #plot ploygons    
    plot_polygons(config)    

    # glEnd()
    glFlush()



def plot_polygons(config):    

    # draw the frame
    window_frame = config.get("window_frame")
    draw_polygon(window_frame)


    
    lines = config.get("lines")
    clipped_lines = line_clip(lines,window_frame)

    glColor3f(1,0,0)
    if config.get("should_clip"):
        draw_lines(clipped_lines)
    else:
        draw_lines(lines)
    # draw polygon
    

def draw_lines(lines):
    for line in lines:
        if line == None:
            continue

        x1,y1 = line[0]
        x2,y2 = line[1]
        print(x1,y1)
        glBegin(GL_LINES)
        glVertex2f(x1/WINDOW_SIZE, y1/WINDOW_SIZE)
        glVertex2f(x2/WINDOW_SIZE, y2/WINDOW_SIZE)
        glEnd()
    

def draw_polygon(vertexes):
    glBegin(GL_POLYGON)
    for v in vertexes:
        glVertex2f(v[0]/WINDOW_SIZE, v[1]/WINDOW_SIZE)
    glEnd()



def drawer(config):
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("Clipping")
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    init()
    glutDisplayFunc(lambda:draw(config))
    glutMainLoop()