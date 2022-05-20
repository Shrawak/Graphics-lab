from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_SIZE = 500

def get_clipped_lines(p1,p2,view_size):

    x1, y1 = p1
    x2, y2 = p2

    (x_min,y_min,x_max,y_max) = view_size
 
    p1 = x1-x2
    p2 = -p1
    p3 = y1-y2
    p4 = -p3

    q1 = x1-x_min
    q2 = x_max-x1
    q3 = y1-y_min
    q4 = y_max-y1

    umin=0
    umax=1
    parr = [p1,p2,p3,p4]
    qarr = [q1,q2,q3,q4]

    for (p,q) in zip(parr,qarr):
        if p==0 and q<0:
            return None
        elif p==0 and q>=0:
            continue
        elif p<0:
            umin = max(umin,q/p)
        elif p>0:
            umax = min(umax,q/p)

    if umin>umax:
        accept = False

    x1f = x1 + umin*(x2-x1)
    y1f = y1 + umin*(y2-y1)
    x2f = x1 + umax*(x2-x1)
    y2f = y1 + umax*(y2-y1)

    accept = True
 
    if accept:
        return [(x1f,y1f),(x2f,y2f)]
    else:
        return None
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def draw(points):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0.8, 0.8)
    glPointSize(5.0)
    # glBegin(GL_LINES)

    # X-AXIS (from (-1, 0) to (1, 0))
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)

    # Y-AXIS (from (0, 1) to (0, -1))
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)

    #plot ploygons    
    plot_polygons(points)    

    # glEnd()
    glFlush()


def plot_polygons(points):    

    # draw the frame
    window_frame = points.get("window_frame")
    draw_polygon(window_frame)


    
    lines = points.get("lines")
    clipped_lines = line_clip(lines,window_frame)

    glColor3f(0,0,0)
    if points.get("should_clip"):
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
        glBegin(GL_LINES)
        glVertex2f(x1/WINDOW_SIZE, y1/WINDOW_SIZE)
        glVertex2f(x2/WINDOW_SIZE, y2/WINDOW_SIZE)
        glEnd()
    

def draw_polygon(vertexes):
    glBegin(GL_POLYGON)
    for v in vertexes:
        glVertex2f(v[0]/WINDOW_SIZE, v[1]/WINDOW_SIZE)
    glEnd()


def line_clip(lines,window_frame):
    x_max = max([points[0] for points in window_frame])
    x_min = min([points[0] for points in window_frame])
    y_max = max([points[1] for points in window_frame])
    y_min = min([points[1] for points in window_frame])

    view_size = (x_min,y_min,x_max,y_max)
    
    clipped_points = []
    for line in lines:
        p1,p2 = line[0],line[1]
        clipped_point = get_clipped_lines(p1,p2,view_size)
        clipped_points.append(clipped_point)
    
    print ('clipped points are',clipped_points)
    return clipped_points


if __name__ == "__main__":
    points = {
    "should_clip": True,
    "window_frame": [(40,150),(350,150),(350,400),(40,400)],
    "lines":[
            [(50,0),(300,300)],
            [(0,100),(150,200)],
            [(475,200),(175,200)],
            [(40,150),(300,400)],
        ]
    }
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("Liang Barsky line clipping")
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    init()
    glutDisplayFunc(lambda:draw(points))
    glutMainLoop()
