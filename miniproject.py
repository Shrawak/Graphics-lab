from asyncio.windows_events import NULL
from enum import Enum
from types import NoneType
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import double

M_SIDE1= 20
M_SIDE2 =21
M_BACK  =22
M_FRONT =23
M_CUSTOM =24
SIZE= 1000
x_angle = 0.0
y_angle = 0.0
z_angle = 0.0
camera_angle = 0.0
c = 1.0
pos = [ 0.0, 0.0, -10.0, 1.0 ]
white = [ 0,0,0, 0 ]
red= [0.7, 0.4, 0.0, 1.0 ]
shiny= [ 50.0 ]
Cylinder = GLUquadricObj()
class Axis(Enum):
    X = 0
    Y = 1
    Z = 2
axis = Axis.X

def change_view (sel):
    global camera_angle
    if( sel == M_CUSTOM):
        print("Enter the view angle")
        camera_angle=int(input("ENTER VIEWANGLE:"))
        glutPostRedisplay()
    elif( sel == M_SIDE1):
        camera_angle=90  
        glutPostRedisplay()
    elif( sel == M_SIDE2):
        camera_angle=-90
        glutPostRedisplay()
    elif( sel == M_BACK):
        camera_angle=180
        glutPostRedisplay()
    elif( sel == M_FRONT):
        camera_angle=0  
        glutPostRedisplay() 
    return NULL      

def initialize_menu():
    glutCreateMenu(change_view)
    glutAddMenuEntry("SIDE VIEW 1", 20)
    glutAddMenuEntry("SIDE VIEW 2", 21)
    glutAddMenuEntry("BACK VIEW", 22)
    glutAddMenuEntry("FRONT VIEW", 23)
    glutAddMenuEntry("CUSTOM VIEW", 24)
    glutAttachMenu(GLUT_MIDDLE_BUTTON)

def mouse_button ( button,  state,  x,  y):
    global c
    global axis
    if ( button == GLUT_LEFT_BUTTON):
        axis=Axis.Z
        c=c+0.4
        print("WIND SPEED DECREASE\t SPEED =",c*1.5,"Km/Hr\n\n")
        glutPostRedisplay()
    elif ( button == GLUT_RIGHT_BUTTON):
        axis = Axis.Z
        c=c-0.4
        print("WIND SPEED DECREASE\t SPEED =",c*1.5,"Km/Hr\n\n")
        glutPostRedisplay()

def spin():
    global x_angle, y_angle, z_angle,c
    if (axis == Axis.X):
        x_angle = x_angle + 1
        glutPostRedisplay()
    elif(axis == Axis.Y):
        y_angle = y_angle + 1
        glutPostRedisplay()
    elif(axis == Axis.Z):
        z_angle =z_angle + c
        glutPostRedisplay()
    glutPostRedisplay()

def display ():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Cylinder = gluNewQuadric()
    gluQuadricDrawStyle( Cylinder, GLU_FILL)
    gluQuadricNormals( Cylinder, GLU_SMOOTH)
    gluQuadricOrientation( Cylinder, GLU_OUTSIDE )
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_TEXTURE_2D)
#Bottom
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,
                              GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                               GL_NEAREST)
    glMaterialfv(GL_FRONT, GL_AMBIENT, white)
    glBegin(GL_QUADS)
    glNormal3f(0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-25.0,-25.0,-44)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-25.0,25.0,-44)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(25.0,25.0,-44)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(25.0,-25.0,-44)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glRotatef(camera_angle,0.0,1.0,0.0)
    gluCylinder(Cylinder,.4,.4,4,16,20)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, red)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, red)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shiny)
    glPushMatrix()
    glutSolidTorus (1.4, 1.4,  6,  6)
    glutSolidCube(2.5)
    glPushMatrix()
    glTranslatef(0.0,-2.0,0.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, red)
    #material property for the base of the windmill
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, red)
    glPopMatrix()
    glPushMatrix()
    glRotatef(90.0,1.0,0.0,0.0)
    glTranslatef(0.0,0.0,-2.0)
    glutPostRedisplay()
    gluCylinder(Cylinder,1.0,2.5,27,50,50)
    glPopMatrix()
    glPopMatrix()
    glRotatef(z_angle, 0.0, 0.0, 1.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, red)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, white)
    glPushMatrix()
    glTranslatef(0.0,0.0,1.5)
    glutSolidCone(1.5,2.5,50,50)
    glPopMatrix()
    glPushMatrix();		#blade 1
    glTranslatef(0.0,0.0,2.2)
    glRotatef(90.0,1.0,0.0,0.0)
    glPushMatrix()
    glRotatef(120,0.0,1.0,0.0)
    glutSolidCone(0.9, 16.0, 15, 15)
    glPopMatrix()
    glPopMatrix()
    glPushMatrix();		#blade 2
    glTranslatef(0.0,0.0,2.2)
    glRotatef(90.0,1.0,0.0,0.0)
    glPushMatrix()
    glRotatef(-120,0.0,1.0,0.0)
    glutSolidCone(0.9, 16.0, 15, 15)
    glPopMatrix()
    glPopMatrix()
    glPushMatrix();		 #blade 3
    glTranslatef(0.0,0.0,2.2)
    glRotatef(90.0,1.0,0.0,0.0)
    glutSolidCone(0.9, 16.0, 15, 15)
    glPopMatrix()
    glLightfv(GL_LIGHT1, GL_POSITION, pos)
    glutSwapBuffers()

def init ():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-25.0, 25.0, -25.0, 25.0, -250.0, 250.0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_NORMALIZE)

def special ( key,  x,  y):
    global camera_angle,axis,c,z_angle
    if key == GLUT_KEY_UP:
        z_angle = z_angle - 10.0
        if (z_angle < 0):
            z_angle = z_angle + 360
        glutPostRedisplay()
        
    elif key == GLUT_KEY_DOWN:
        z_angle = z_angle + 10.0
        if (z_angle > 360):
            z_angle = z_angle - 360
        glutPostRedisplay()
    
    elif key == GLUT_KEY_HOME:
        z_angle = z_angle - 90.0
        if (z_angle > 360):
            z_angle = z_angle - 360
        glutPostRedisplay()
        
    elif key == GLUT_KEY_END:
        z_angle = z_angle + 90.0
        if (z_angle > 360):
            z_angle = z_angle - 360
        glutPostRedisplay()
        
    elif key == GLUT_KEY_LEFT:
        axis = Axis.X
        camera_angle = camera_angle - 5.0
        if (camera_angle < 0):
            camera_angle = camera_angle + 360
        glutPostRedisplay()
        
    elif key == GLUT_KEY_RIGHT:
        axis = Axis.X
        camera_angle = camera_angle + 5.0
        if (camera_angle > 360):
            camera_angle = camera_angle - 360
        glutPostRedisplay()
        
def reshape ( width,  height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-25.0, 25.0, -25.0, 25.0, -250.0, 250.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main ():
    glutInit() 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(SIZE, SIZE)
    glutInitWindowPosition(1000, 100)
    glutCreateWindow("SIMULATION OF WINDMILL")
    glutIdleFunc(spin)
    glutDisplayFunc(display)
    glutSpecialFunc(special)
    glutMouseFunc(mouse_button)
    initialize_menu()
    glutReshapeFunc(reshape)
    init()
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()

if __name__ == "__main__":
    main()
