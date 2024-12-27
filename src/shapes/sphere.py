from OpenGL.GL import *
from OpenGL.GLU import *
from shapes.shape import Shape

class Sphere(Shape):
    def __init__(self, radius=1.0, slices=256, stacks=256):
        """Initialize a sphere with given radius, slices, and stacks"""
        super().__init__()
        self.name = "Sphere"
        self.radius = radius
        self.slices = slices
        self.stacks = stacks
        self.quadric = gluNewQuadric()
        gluQuadricDrawStyle(self.quadric, GLU_FILL)

    def _draw(self):
        """Draw the sphere using GLU quadrics"""
        gluSphere(self.quadric, self.radius, self.slices, self.stacks)
    
    def get_bounding_radius(self):
        return self.radius + 1.0  # Add a small offset to the radius

    def __del__(self):
        """Clean up the quadric object when the sphere is deleted"""
        if self.quadric:
            gluDeleteQuadric(self.quadric)