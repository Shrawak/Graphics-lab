#include<windows.h>
#include <GL/glut.h>
#include <GL/gl.h>
#include<iostream>
#include <math.h>
using namespace std;
const double twoPi = 6.283185;
int x_c,y_c,radius;

void init(){
glClearColor(1,1,1,1);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,500,0,500);
    glColor3f(1,0,0);
    glMatrixMode(GL_MODELVIEW);
}
void Midpointcircle(){
    glClear(GL_COLOR_BUFFER_BIT);
    int x=0;
    int y=radius;
    int p=1-radius;
    void circlePlotPoints(int, int);
    circlePlotPoints(x,y);
    while (x<y){
        x++;
        if(p < 0){
            p+=2*x+1;
        }else{
            y--;
            p+=2* (x-y)+1;
        }
        circlePlotPoints(x,y);
    }

}

void circlePlotPoints(int x, int y){
    glBegin(GL_POINTS);
        glVertex2i(x_c+x,y_c+y);
        glVertex2i(x_c-x,y_c+y);
        glVertex2i(x_c+x,y_c-y);
        glVertex2i(x_c-x,y_c-y);
        glVertex2i(x_c+y,y_c+x);
        glVertex2i(x_c-y,y_c+x);
        glVertex2i(x_c+y,y_c-x);
        glVertex2i(x_c-y,y_c-x);
    glEnd();
}

void DrawPieChart(){
    int slice;
    cout << "How many datas are there ? : ";
    cin>> slice;
    int dataValues[slice];
    for(int i=0;i<slice;i++){
        cin>> dataValues[i];
    }
    double sliceAngle, prev_Angle=0.0;
    float dataSum=0.0;
    int x_line,y_line;
    Midpointcircle();
    for (int k=0 ;k<slice;k++){
        dataSum+=dataValues[k];
    }

    for(int k=0; k<slice; k++){
    glColor3f(rand()%1,rand()%2,rand()%2);
        sliceAngle=twoPi * dataValues[k]/dataSum + prev_Angle;
        x_line= x_c + radius * cos(sliceAngle);
        y_line=y_c + radius * sin(sliceAngle);
        glBegin(GL_LINES);
            glVertex2i(x_c,y_c);
            glVertex2i(x_line,y_line);
        glEnd();
        prev_Angle=sliceAngle;
    }
    glFlush();

}


int main(int argc, char* argv[]){
    cout<<"Enter the center x and y"<<endl;
    cout<<"Enter x-coordinate : ";
    cin>>x_c;
    cout<<"Enter y-coordinate : ";
    cin>>y_c;
    cout<<"Enter the radius of circle : ";
    cin>>radius;
    glutInit(&argc,argv);
    glutInitWindowSize(600,600);
    glutInitWindowPosition(600,300);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutCreateWindow("Pie-Chart");
    init();
    glutDisplayFunc(DrawPieChart);
    glutMainLoop();
    return 0;
}
