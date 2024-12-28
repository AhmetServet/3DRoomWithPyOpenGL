from OpenGL.GL import *
from shapes.shape import Shape
import math

class Pyramid(Shape):
    def __init__(self, base_size=1.0, height=1.0):
        """Initialize a pyramid with given base size and height"""
        super().__init__()
        self.name = "Pyramid"
        self.base_size = base_size
        self.height = height

    def _draw(self):
        """Draw the pyramid"""
        glBegin(GL_TRIANGLES)

        # Front face
        glVertex3f(0.0, self.height, 0.0)
        glVertex3f(-self.base_size, 0.0, self.base_size)
        glVertex3f(self.base_size, 0.0, self.base_size)

        # Right face
        glVertex3f(0.0, self.height, 0.0)
        glVertex3f(self.base_size, 0.0, self.base_size)
        glVertex3f(self.base_size, 0.0, -self.base_size)

        # Back face
        glVertex3f(0.0, self.height, 0.0)
        glVertex3f(self.base_size, 0.0, -self.base_size)
        glVertex3f(-self.base_size, 0.0, -self.base_size)

        # Left face
        glVertex3f(0.0, self.height, 0.0)
        glVertex3f(-self.base_size, 0.0, -self.base_size)
        glVertex3f(-self.base_size, 0.0, self.base_size)

        glEnd()

        glBegin(GL_QUADS)

        # Bottom face
        glVertex3f(-self.base_size, 0.0, self.base_size)
        glVertex3f(self.base_size, 0.0, self.base_size)
        glVertex3f(self.base_size, 0.0, -self.base_size)
        glVertex3f(-self.base_size, 0.0, -self.base_size)

        glEnd()

    def get_bounding_radius(self):
        # set a higher bounding radius to avoid clipping
        return math.sqrt(3) * self.base_size / 2 + 1.0

    def __del__(self):
        """Clean up the quadric object when the pyramid is deleted"""
        pass
