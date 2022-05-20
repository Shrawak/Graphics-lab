from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_SIZE = 500

def clip(subjectPolygon, clipPolygon):
    def inside(p):
        return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
     
    def computeIntersection():
        dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
        dp = [s[0] - e[0], s[1] - e[1]]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0]
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
    outputList = subjectPolygon
    cp1 = clipPolygon[-1]

    for clipVertex in clipPolygon:
        cp2 = clipVertex
        inputList = outputList
        outputList = []
        s = inputList[-1]

        for subjectVertex in inputList:
            e = subjectVertex
            if inside(e):
                if not inside(s):
                    outputList.append(computeIntersection())
                outputList.append(e)
            elif inside(s):
                outputList.append(computeIntersection())
            s = e
        cp1 = cp2
    return(outputList)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


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

    # plot ploygons
    plot_polygons(points)

    # glEnd()
    glFlush()


def plot_polygons(points):

    # draw the frame
    window_frame = points.get("window_frame")
    draw_polygon(window_frame)

    polygon = points.get("polygon")
    clipped_polygon = clip(polygon, window_frame)
    print('The polygon vertex in windows are',clipped_polygon)

    glColor3f(1, 0, 0)
    if points.get("should_clip"):
        draw_polygon(clipped_polygon)
    else:
        draw_polygon(polygon)
    # draw polygon


def draw_polygon(vertexes):
    glBegin(GL_POLYGON)
    for v in vertexes:
        glVertex2f(v[0]/WINDOW_SIZE, v[1]/WINDOW_SIZE)
    glEnd()


if __name__ == "__main__":
    points = {
        "polygon": [(10, 120), (150, 400), (450, 50)],
        "window_frame": [(40, 150), (350, 150), (350, 400), (40, 400)],
        "should_clip": True
    }
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("Cohen Sutherland Polygon clipping")
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    init()
    glutDisplayFunc(lambda: draw(points))
    glutMainLoop()
