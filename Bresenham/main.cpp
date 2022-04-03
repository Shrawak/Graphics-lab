#include<windows.h>
#include<iostream>
#include<GL/glut.h>
#include<GL/gl.h>
using namespace std;
    int x1,y1,x2,y2;

void init(){
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,400,0,400);
    glMatrixMode(GL_MODELVIEW);
}

void Bresenhamline(){
    glClear(GL_COLOR_BUFFER_BIT);
    int dx=abs(x2-x1),dy=abs(y2-y1);
    float m;
    int x,y, xEnd,yEnd;
    if(dx !=0){
        m=dy/dx;
    }else{
        m=dy;
    }
    if(abs(m) < 1){
        int  _2dy=2* dy,_2dydx=2*(dy-dx);
        int p=2*dy-dx;

        if(x1> x2){
            x=x2;
            y=y2;
            xEnd=x1;
        }else{
            x=x1;
            y=y1;
            xEnd=x2;
        }
        glBegin(GL_POINTS);
            glVertex2i(x,y);
        glEnd();

        while (x< xEnd){
            x++;
            if(p<0){
                p+=_2dy;
            }else{
                y++;
                p+=_2dydx;
            }
            glBegin(GL_POINTS);
            glVertex2i(x,y);
            glEnd();
        }
        glFlush();
    }else{
        int  _2dx=2* dx,_2dxdy=2*(dx-dy);
        int p=2*dx-dy;

        if(y1> y2){
            x=x2;
            y=y2;
            yEnd=y1;
        }else{
            x=x1;
            y=y1;
            yEnd=y2;
        }
        glBegin(GL_POINTS);
            glVertex2i(x,y);
        glEnd();

        while (y< yEnd){
            y++;
            if(p<0){
                p+=_2dx;
            }else{
                x++;
                p+=_2dxdy;
            }
            glBegin(GL_POINTS);
            glVertex2i(x,y);
            glEnd();
        }
        glFlush();
        }
}

int main(int argc, char* argv[]){


    cout<<"x1 : ";
    cin>>x1;
    cout<<"y1 : ";
    cin>>y1;
    cout<<"x2 : ";
    cin>>x2;
    cout<<"y2 : ";
    cin>>y2;


    glutInit(&argc,argv);
    glutInitWindowPosition(250,150);
    glutInitWindowSize(800,800);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutCreateWindow("Line drawing using Breseham algorithm");
    init();


    glutDisplayFunc(Bresenhamline);
    glutMainLoop();
    return 0;
}
