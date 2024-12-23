from lightning.light import Light
from OpenGL.GL import *
import math

class AreaLight(Light):
    def __init__(self, light_id, 
                 ambient=(0.2, 0.2, 0.2, 1.0),
                 diffuse=(0.8, 0.8, 0.8, 1.0),
                 specular=(1.0, 1.0, 1.0, 1.0),
                 position=(0.0, 5.0, 0.0, 1.0),  # Position at top of room
                 direction=(0.0, -1.0, 0.0),     # Point downward
                 cutoff=60.0,                    # Wide angle for area effect
                 exponent=2.0):                  # Soft falloff
        super().__init__(light_id, ambient, diffuse, specular, position)
        self.direction = direction
        self.cutoff = cutoff
        self.exponent = exponent
        self.attenuation = (1.0, 0.0, 0.001)    # Quadratic attenuation for realistic falloff

    def enable(self):
        super().enable()
        
        # Set spotlight parameters
        glLightfv(self.light_id, GL_SPOT_DIRECTION, self.direction)
        glLightf(self.light_id, GL_SPOT_CUTOFF, self.cutoff)
        glLightf(self.light_id, GL_SPOT_EXPONENT, self.exponent)
        
        # Set attenuation factors
        glLightf(self.light_id, GL_CONSTANT_ATTENUATION, self.attenuation[0])
        glLightf(self.light_id, GL_LINEAR_ATTENUATION, self.attenuation[1])
        glLightf(self.light_id, GL_QUADRATIC_ATTENUATION, self.attenuation[2])

    def set_cutoff(self, angle):
        """Set the cutoff angle of the area light (0-90 degrees)"""
        self.cutoff = max(0.0, min(90.0, angle))
        if self.enabled:
            glLightf(self.light_id, GL_SPOT_CUTOFF, self.cutoff)

    def set_exponent(self, exponent):
        """Set the spotlight exponent (controls light concentration)"""
        self.exponent = max(0.0, min(128.0, exponent))
        if self.enabled:
            glLightf(self.light_id, GL_SPOT_EXPONENT, self.exponent)

    def set_direction(self, direction):
        """Set the direction of the area light"""
        self.direction = direction
        if self.enabled:
            glLightfv(self.light_id, GL_SPOT_DIRECTION, self.direction)

    def set_attenuation(self, constant, linear, quadratic):
        """Set the attenuation factors of the area light"""
        self.attenuation = (constant, linear, quadratic)
        if self.enabled:
            glLightf(self.light_id, GL_CONSTANT_ATTENUATION, constant)
            glLightf(self.light_id, GL_LINEAR_ATTENUATION, linear)
            glLightf(self.light_id, GL_QUADRATIC_ATTENUATION, quadratic)