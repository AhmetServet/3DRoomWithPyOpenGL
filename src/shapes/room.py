from shapes.shape import Shape
from OpenGL.GL import *
from OpenGL.GLUT import *

class Room(Shape):
    def __init__(self, room_size=100):
        super().__init__()
        self.name = "Room"
        self.set_position(0, 0, 0)
        self.set_rotation(0, 0, 0)
        self.set_scale(2, 2, 2)
        self.room_size = room_size

    def _draw(self):
        """Draw a cube centered at (0, 0, 0)"""
        # Draw solid cube
        glColor3f(0.5, 0.5, 0.5)
        glutSolidCube(self.room_size)

        # Draw wireframe cube
        glColor3f(0.0, 0.0, 0.0)
        glutWireCube(self.room_size - 0.1)  # Offset to slightly shrink the wireframe

        # Draw wireframe edges
        glColor3f(1.0, 0.0, 0.0)
        glutWireCube(self.room_size + 0.1)