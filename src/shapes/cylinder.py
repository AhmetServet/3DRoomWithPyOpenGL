from OpenGL.GL import *
from OpenGL.GLU import *
from shapes.shape import Shape

class Cylinder(Shape):
    def __init__(self, base_radius=1.0, top_radius=1.0, height=2.0, slices=256, stacks=256):
        """Initialize a cylinder with given base radius, top radius, height, slices, and stacks"""
        super().__init__()
        self.name = "Cylinder"
        self.base_radius = base_radius
        self.top_radius = top_radius
        self.height = height
        self.slices = slices
        self.stacks = stacks
        self.quadric = gluNewQuadric()
        gluQuadricDrawStyle(self.quadric, GLU_FILL)

    def _draw(self):
        """Draw the cylinder using GLU quadrics"""
        # Draw the cylinder body
        gluCylinder(self.quadric, self.base_radius, self.top_radius, self.height, self.slices, self.stacks)
        
        # Draw the bottom disk
        glPushMatrix()
        glRotatef(180, 1, 0, 0)
        gluDisk(self.quadric, 0, self.base_radius, self.slices, 1)
        glPopMatrix()
        
        # Draw the top disk
        glPushMatrix()
        glTranslatef(0, 0, self.height)
        gluDisk(self.quadric, 0, self.top_radius, self.slices, 1)
        glPopMatrix()

    def get_bounding_radius(self):
        return max(self.base_radius, self.top_radius)  + 1.0  # Add a small offset to the radius

    def __del__(self):
        """Clean up the quadric object when the cylinder is deleted"""
        if self.quadric:
            gluDeleteQuadric(self.quadric)