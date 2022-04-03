#include<windows.h>
#include<GL/glu.h>
#include<GL/glut.h>
#include <iostream>
#include<math.h>
using namespace std;
float x_1,x_2,y_1,y_2;

void init(){
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,400,0,400);
    glMatrixMode(GL_MODELVIEW);
}

void DDAline(){
    glClear(GL_COLOR_BUFFER_BIT);
    float x,y,dy,dx,x_inc,y_inc,stepsize;
    dx=x_2-x_1;
    dy=y_2-y_1;

    if(abs(dx) > abs(dy)){
        stepsize=abs(dx);
    }else{
        stepsize=abs(dy);
    }
    x_inc=dx/stepsize;
    y_inc=dy/stepsize;
    x=x_1;
    y=y_1;
    glBegin(GL_POINTS);
        glVertex2i(x,y);
    glEnd();

    for(int i=1; i<=stepsize; i++){
        x=x+x_inc;
        y=y+y_inc;

        glBegin(GL_POINTS);
            glVertex2i(x,y);
        glEnd();
    }

    glFlush();
}

int main(int argc, char* argv[]){

    cout<<"x1 : ";
    cin>>x_1;
    cout<<"y1 : ";
    cin>>y_1;
    cout<<"x2 : ";
    cin>>x_2;
    cout<<"y2 : ";
    cin>>y_2;


    glutInit(&argc,argv);
    glutInitWindowPosition(250,150);
    glutInitWindowSize(800,800);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutCreateWindow("Line Drawing using DDA");
    init();
    glutDisplayFunc(DDAline);
    glutMainLoop();
    return 0;
}
