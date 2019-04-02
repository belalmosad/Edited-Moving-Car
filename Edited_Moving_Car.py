from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective( 60, 1, 0.1, 50)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(0.52,0.80,0.98,1)
    glClear(GL_COLOR_BUFFER_BIT)    

##Globals
angle = 0
x = 0
forward = True


move_z = 0
ball = 0
ball_F = True
def draw():
    global angle
    global x
    global forward
    global ball
    global ball_F


    ##inits
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


    ##surroundingView


    glScale(1,2,2)
    glRotate(90,0,1,0)
    glBegin(GL_POLYGON)
    glColor3f(0.45,0.45,0.45)
    glVertex(15, -1, -3)
    glVertex(15, -1, 3)
    glVertex(-15, -1, 3)
    glVertex(-30, -1, -3)
    glEnd()
    glScale(1,1,1)

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(2.5, -1, -0.3)
    glVertex(2.5, -1, 0.3)
    glVertex(-2.5, -1, 0.3)
    glVertex(-2.5, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(5, -1, -0.3)
    glVertex(5, -1, 0.3)
    glVertex(10, -1, 0.3)
    glVertex(10, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-5, -1, -0.3)
    glVertex(-5, -1, 0.3)
    glVertex(-10, -1, 0.3)
    glVertex(-10, -1, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-15, -1, -0.3)
    glVertex(-15, -1, 0.3)
    glVertex(-25, -1, 0.3)
    glVertex(-25, -1, -0.3)
    glEnd()
    
    

    ##BackTires
    
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(2.5 + x, -2.5 * 0.25, - 2.5 * 0.5 + move_z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0.5,0.6,0.7)
    glutSolidTorus(0.25,0.5,10,10)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-2.5 + x, -2.5 * 0.25, - 2.5 * 0.5  + move_z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0.5,0.6,0.7)
    glutSolidTorus(0.25,0.5,10,10)


    #carBody
    
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(x,0,move_z)
    glColor3f(0,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    
    glLoadIdentity()
    glRotate(90,0,1,0)
    glColor3f(0.44,0.184,0.21)
    glTranslate(0+x,1.25,move_z)
    glScale(0.5,0.2,0.45)
    glutSolidCube(5)

    


    ##Tires
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(2.5 + x, -2.5 * 0.25, 2.5 * 0.5 + move_z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0.5,0.6,0.7)
    glutSolidTorus(0.25,0.5,10,10)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-2.5+x, -2.5 * 0.25, 2.5 * 0.5 + move_z)
    glRotate(angle,0,0,1)
    glColor3f(0.5,0.6,0.7)
    glutSolidTorus(0.25,0.5,10,10)

    
    ##Scouts
    glLoadIdentity()
    glRotate(90,0,1,0)
    glColor3f(1,1,0)
    glTranslate(2.5+x,0,0.6 + move_z)
    glutSolidSphere(0.25,100,100)


    glLoadIdentity()
    glRotate(90,0,1,0)
    glColor3f(1, 1, 0)
    glTranslate(2.5 + x, 0,- 0.6 + move_z)
    glutSolidSphere(0.25,100,100)



    ##ball
    glLoadIdentity()
    glColor3f(0.8,0,0.3)
    glTranslate(0,0,-10 + ball)
    glutSolidSphere(0.7,100,100)


    if forward:
        x += 0.02
        angle -= 0.1
        if x > 8:
                forward = False
    else:
        x -= 0.02
        angle += 0.1
        if x < -8:
            forward = True



    if ball_F:
        ball += 0.09
        if ball > 15:
                ball_F = False
    else:
        ball -= 0.09
        if ball < -15:
            ball_F = True


    glutSwapBuffers()

def specialKey(key,x,y):
    global move_z
    if key == GLUT_KEY_RIGHT:
        move_z += 0.1
    elif key == GLUT_KEY_LEFT:
        move_z -= 0.1

    draw()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700,700)
glutCreateWindow(b"Moving car")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(specialKey)
myInit()
glutMainLoop()
