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
        self.preset1_shapes = [s.Cube(), s.Sphere(), s.Cylinder(), s.Pyramid()]
        self.lights = {
            0: light.AmbientLight(GL_LIGHT0),
            1: light.PointLight(GL_LIGHT1),
            2: light.AreaLight(GL_LIGHT3),
            3: light.DirectionalLight(GL_LIGHT2)
        }
        self.camera = Camera()
        self.room = s.Room(40)
        self.preset = 0

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
        
    def timerEvent(self):
        self.lights[0].update_color_rgb()  # Update the ambient light color
        self.update()


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Draw the lights
        self.initializeLighting()

        pos = self.camera.get_position()
        print(f"Camera position: {pos}")
        if self.preset == 0:
            # Update camera position
            gluLookAt(
                pos[0], pos[1], pos[2],
                0, 0, 0,
                0, 1, 0
            )

            # Draw shapes
            for shape in self.shapes:
                print(f"Drawing shape: {shape}")
                shape.draw()

        elif self.preset == 1:
            gluLookAt(
                pos[0], pos[1], pos[2],
                10, -10, -10,
                0, 1, 0
            )
            #cube
            self.preset1_shapes[0].set_position(10.0, -10.0, -10.0)
            self.preset1_shapes[0].set_scale(0.8, 0.8, 0.8)
            self.preset1_shapes[0].set_rotation(0.0, 0.0, 0.0)
            self.preset1_shapes[0].set_color(0.0, 1.0, 1.0)
            self.preset1_shapes[0].set_material(ambient=(0.0, 0.0, 0.0, 1.0), diffuse=(0.8, 0.8, 0.8, 1.0), specular=(0.0, 0.0, 0.0, 1.0), shininess=0.0)

            #sphere
            self.preset1_shapes[1].set_position(9.75, -9.0, -9.75)
            self.preset1_shapes[1].set_scale(0.4, 0.4, 0.4)
            self.preset1_shapes[1].set_rotation(0.0, 0.0, 0.0)
            self.preset1_shapes[1].set_color(1.0, 0.0, 0.0)
            self.preset1_shapes[1].set_material(ambient=(0.25, 0.25, 0.25, 1.0), diffuse=(0.4, 0.4, 0.4, 1.0), specular=(0.774597, 0.774597, 0.774597, 1.0), shininess=78)

            #cylinder
            self.preset1_shapes[2].set_position(9.0, -9.5, -9.9)
            self.preset1_shapes[2].set_scale(0.4, 0.4, 0.4)
            self.preset1_shapes[2].set_rotation(0.25, 0.0, 0.0)
            self.preset1_shapes[2].set_color(0.5, 0.5, 0.0)
            self.preset1_shapes[2].set_material(ambient=(0.0, 0.0, 0.0, 1.0), diffuse=(0.5, 0.5, 0.5, 1.0), specular=(0.0, 0.0, 0.0, 1.0), shininess=0.0)

            #pyramid
            self.preset1_shapes[3].set_position(10.1, -10.5, -9.31)
            self.preset1_shapes[3].set_scale(0.5, 0.5, 0.5)
            self.preset1_shapes[3].set_rotation(0.156, 0.0, 0.0)
            self.preset1_shapes[3].set_position(10.1, -10.5, -9.31)
            self.preset1_shapes[3].set_scale(0.5, 0.5, 0.5)
            self.preset1_shapes[3].set_rotation(0.156, 0.0, 0.0)
            self.preset1_shapes[3].set_color(0.5, 0.0, 0.5)  # Purple color
            self.preset1_shapes[3].set_material(
                ambient=(0.24725, 0.1995, 0.0745, 1.0),
                diffuse=(0.75164, 0.60648, 0.22648, 1.0),
                specular=(0.628281, 0.555802, 0.366065, 1.0),
                shininess=51.2
            )

            for i, light in self.lights.items():
                light.set_position((5.0, 0.0, -8.0, 1.0))

            for shape in self.preset1_shapes:
                shape.draw()        

        # Draw the room
        self.room.draw()
        
        if self.lights[0].get_rgb_mode():
            self.timerEvent()

        # self.update()
        

    def move_camera(self, direction):
        self.camera.move(direction)
        self.update()

    def apply_preset1(self):
        if self.preset == 1:
            self.camera.reset_position()
            self.preset = 0
        elif self.preset == 0:
            self.camera.set_position([7.0, -7.0, -7.0]) 
            self.camera.set_radius(20.0)
            self.camera.set_can_move(False)
            self.preset = 1
        self.update()

    def randomize_shapes(self):
        for shape in self.shapes:
            shape.set_random_color()
            shape.set_random_material()
            shape.set_random_position()
            shape.set_random_rotation()

        for shape in self.shapes:
            for other in self.shapes:
                if shape != other and shape.check_collision(other):
                    shape.set_random_position()
                    shape.set_random_rotation()
                    break
        self.update()
