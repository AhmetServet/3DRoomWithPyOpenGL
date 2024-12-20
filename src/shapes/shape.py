from OpenGL.GL import *
from OpenGL.GLU import *
import random

class Shape:
    def __init__(self):
        """Initialize basic properties common to all shapes"""
        self.name = "Shape"               # default name
        self.set_random_position()  # Set a random position
        self.set_random_color()     # Set a random color
        self.set_random_rotation()  # Set random rotation angles
        self.scale = [0.8, 0.8, 0.8]      # scale factors for x, y, z

    def set_color(self, r=None, g=None, b=None):
        """Set the color of the shape using RGB values (0.0 to 1.0)"""
        if r is None:  # If no color provided, set random color
            self.set_random_color()
        else:
            self.color = [r, g, b]
    
    def set_random_color(self):
        """Set a random color for the shape"""
        self.color = [random.random(), random.random(), random.random()]

    def set_position(self, x, y, z):
        """Set the position of the shape"""
        self.position = [x, y, z]
    
    def set_random_position(self):
        """Set a random position for the shape"""
        self.position = [random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2)]

    def set_rotation(self, x, y, z):
        """Set the rotation angles of the shape"""
        self.rotation = [x, y, z]

    def set_random_rotation(self):
        """Set random rotation angles for the shape"""
        self.rotation = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]

    def set_scale(self, x, y, z):
        """Set the scale factors of the shape"""
        self.scale = [x, y, z]

    def draw(self):
        """Base draw method to be overridden by subclasses"""
        glPushMatrix()
        glTranslatef(*self.position)
        glRotatef(self.rotation[0] * 360, 1, 0, 0)
        glRotatef(self.rotation[1] * 360, 0, 1, 0)
        glRotatef(self.rotation[2] * 360, 0, 0, 1)
        glScalef(*self.scale)
        
        # Draw the shape with the specified color
        glColor3f(*self.color)
        self._draw()
        
        # Draw the edges in black
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLineWidth(0.5)
        glColor3f(0.0, 0.0, 0.0)
        self._draw()
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        
        glPopMatrix()

    def _draw(self):
        """Protected method to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement _draw()")
