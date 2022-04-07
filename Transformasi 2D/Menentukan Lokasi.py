#Nama   : Jasmine Sarah Maqnolia
#NIM    : 20051397078
#Kelas  : 2020B
#Prodi  : Manajemen Informatika

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-6, 6, -6, 6, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(3.00, 1.00)
    glVertex2f(6.00, 2.00)
    glVertex2f(7.00, 4.00)
    glVertex2f(2.00, 5.00)
    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutCreateWindow("Praktikum 3 Menentukan Lokasi")
glutDisplayFunc(draw)
glutMainLoop()