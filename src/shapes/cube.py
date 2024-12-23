from OpenGL.GL import *
from shapes.shape import Shape
from OpenGL.GLUT import *
import math

class Cube(Shape):
    def __init__(self, size=1.0):
        """Initialize a cube with given size"""
        super().__init__()
        self.name = "Cube"
        self.size = size

    def _draw(self):
        """Draw the cube"""
        glutSolidCube(self.size)

    def get_bounding_radius(self):
        return math.sqrt(3) * self.size / 2 + 1.0
    
    def __del__(self):
        """Clean up resources if needed"""
        pass