from PyQt5.QtOpenGL import QGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin
import random
import shapes as s

class OpenGLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(OpenGLWidget, self).__init__(parent)
        self.shapes = [s.Cube(), s.Sphere(), s.Cylinder(), s.Pyramid()]
        self.camera_pos = [0.0, 0.0, -5]
        self.camera_speed = 0.5

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        # Update camera position
        glTranslatef(-self.camera_pos[0], -self.camera_pos[1], -self.camera_pos[2])
        
        # Draw shapes
        for shape in self.shapes:
            shape.draw()

    def move_camera(self, direction):
        if direction == "left":
            self.camera_pos[0] -= self.camera_speed
        elif direction == "right":
            self.camera_pos[0] += self.camera_speed
        elif direction == "up":
            self.camera_pos[1] += self.camera_speed
        elif direction == "down":
            self.camera_pos[1] -= self.camera_speed
        elif direction == "in":
            self.camera_pos[2] += self.zoom_speed
        elif direction == "out":
            self.camera_pos[2] -= self.zoom_speed

        self.updateGL()