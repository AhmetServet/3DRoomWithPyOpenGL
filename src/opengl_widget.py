from PyQt5.QtOpenGL import QGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import shapes as s
from camera import Camera
import lightning as light

class OpenGLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(OpenGLWidget, self).__init__(parent)
        self.shapes = [s.Cube(), s.Sphere(), s.Cylinder(), s.Pyramid()]
        self.lights = {
            0: light.AmbientLight(GL_LIGHT0),
            1: light.PointLight(GL_LIGHT1),
            2: light.AreaLight(GL_LIGHT2),
            3: light.DirectionalLight(GL_LIGHT3)
        }
        self.camera = Camera()
        self.room = s.Room(20)

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # Set the perspective with a far clipping plane distance of 1000.0
        gluPerspective(45.0, self.width() / self.height(), 0.1, 100)
        glMatrixMode(GL_MODELVIEW)


    def initializeLighting(self):
        glEnable(GL_LIGHTING)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Update camera position
        pos = self.camera.get_position()
        print(f"Camera position: {pos}")
        gluLookAt(
            pos[0], pos[1], pos[2],
            0, 0, 0,
            0, 1, 0
        )
        # Draw the lights
        self.initializeLighting()
        

        # Draw the room
        self.room.draw()
        
        # Draw shapes
        for shape in self.shapes:
            print(f"Drawing shape: {shape}")
            shape.draw()
        

    def move_camera(self, direction):
        self.camera.move(direction)
        self.update()

    def randomize_shapes(self):
        for shape in self.shapes:
            shape.set_random_color()
            shape.set_random_position()
            shape.set_random_rotation()

        for shape in self.shapes:
            for other in self.shapes:
                if shape != other and shape.check_collision(other):
                    shape.set_random_position()
                    shape.set_random_rotation()
                    break
        self.update()
