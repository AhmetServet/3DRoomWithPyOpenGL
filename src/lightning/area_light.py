from lightning.light import Light
from OpenGL.GL import *
import math

class AreaLight:
    def __init__(self, base_light_id=GL_LIGHT4, 
                 ambient=(0.2, 0.2, 0.2, 1.0),
                 diffuse=(0.8, 0.8, 0.8, 1.0),
                 specular=(1.0, 1.0, 1.0, 1.0),
                 base_position=(0.0, 10.0, 0.0),  # Base position at top of room
                 direction=(0.0, -1.0, 0.0),     # Point downward
                 cutoff=60.0,                    # Wide angle for area effect
                 exponent=2.0):                  # Soft falloff
        self.lights = []
        self.enabled = False
        self.grid_size = (1, 4)  # Adjust grid size to ensure max 8 lights
        self.spacing = 10.0  # Spacing between lights in the grid

        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                light_id = base_light_id + i * self.grid_size[1] + j
                position = (base_position[0] + i * self.spacing, 
                            base_position[1], 
                            base_position[2] + j * self.spacing, 
                            0.0)
                light = Light(light_id, ambient, diffuse, specular, position)
                light.direction = direction
                light.cutoff = cutoff
                light.exponent = exponent
                light.attenuation = (1.0, 0.0, 0.001)
                self.lights.append(light)

    def enable(self):
        self.enabled = True
        for light in self.lights:
            light.enable()
            glLightfv(light.light_id, GL_SPOT_DIRECTION, light.direction)
            glLightf(light.light_id, GL_SPOT_CUTOFF, light.cutoff)
            glLightf(light.light_id, GL_SPOT_EXPONENT, light.exponent)
            glLightf(light.light_id, GL_CONSTANT_ATTENUATION, light.attenuation[0])
            glLightf(light.light_id, GL_LINEAR_ATTENUATION, light.attenuation[1])
            glLightf(light.light_id, GL_QUADRATIC_ATTENUATION, light.attenuation[2])

    def disable(self):
        self.enabled = False
        for light in self.lights:
            light.disable()

    def set_cutoff(self, angle):
        """Set the cutoff angle of the area light (0-90 degrees)"""
        for light in self.lights:
            light.cutoff = max(0.0, min(90.0, angle))
            if self.enabled:
                glLightf(light.light_id, GL_SPOT_CUTOFF, light.cutoff)

    def set_exponent(self, exponent):
        """Set the spotlight exponent (controls light concentration)"""
        for light in self.lights:
            light.exponent = max(0.0, min(128.0, exponent))
            if self.enabled:
                glLightf(light.light_id, GL_SPOT_EXPONENT, light.exponent)

    def set_direction(self, direction):
        """Set the direction of the area light"""
        for light in self.lights:
            light.direction = direction
            if self.enabled:
                glLightfv(light.light_id, GL_SPOT_DIRECTION, light.direction)

    def set_attenuation(self, constant, linear, quadratic):
        """Set the attenuation factors of the area light"""
        for light in self.lights:
            light.attenuation = (constant, linear, quadratic)
            if self.enabled:
                glLightf(light.light_id, GL_CONSTANT_ATTENUATION, constant)
                glLightf(light.light_id, GL_LINEAR_ATTENUATION, linear)
                glLightf(light.light_id, GL_QUADRATIC_ATTENUATION, quadratic)

    def set_position(self, position):
        """Set the position of the area light"""
        self.base_position = position