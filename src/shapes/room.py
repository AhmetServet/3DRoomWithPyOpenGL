from shapes.shape import Shape
from OpenGL.GL import *
from OpenGL.GLUT import *

class Room(Shape):
    def __init__(self, room_size=40):
        super().__init__()
        self.name = "Room"
        self.set_position(0, 0, 0)
        self.set_rotation(0, 0, 0)
        self.set_scale(1, 1, 1)
        self.room_size = room_size
        self.set_default_material()

    def set_default_material(self):
        """Set default material properties for the room"""
        self.material_ambient = [0.3, 0.3, 0.3, 1.0]
        self.material_diffuse = [0.6, 0.6, 0.6, 1.0]
        self.material_specular = [0.9, 0.9, 0.9, 1.0]
        self.material_shininess = 50.0

    def _draw(self):
        """Draw a cube centered at (0, 0, 0)"""
        # Apply material properties
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, self.material_ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, self.material_diffuse)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, self.material_specular)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, self.material_shininess)

        # Draw solid cube
        glColor3f(0.7, 0.7, 0.7)
        glutSolidCube(self.room_size)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, self.material_ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, self.material_diffuse)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, self.material_specular)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, self.material_shininess)
        
        # Draw wireframe cube
        glColor3f(0.0, 0.0, 0.0)
        glutWireCube(self.room_size - 0.1)  # Offset to slightly shrink the wireframe

        # Draw wireframe edges
        glColor3f(1.0, 0.0, 0.0)
        glutWireCube(self.room_size + 0.1)