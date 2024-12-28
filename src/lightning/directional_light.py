from lightning.light import Light
from OpenGL.GL import *

class DirectionalLight(Light):
    def __init__(self, light_id, 
                 ambient=(0.0, 0.0, 0.0, 1.0),
                 diffuse=(0.8, 0.8, 0.8, 1.0),
                 specular=(1.0, 1.0, 1.0, 1.0),
                 direction=(0.0, -1.0, 0.0)):  # Default direction pointing downwards
        super().__init__(light_id, ambient, diffuse, specular, position=(0.0, 10.0, 0.0, 0.0))
        self.direction = direction

    def enable(self):
        super().enable()
        # glLightfv(self.light_id, GL_SPOT_DIRECTION, self.direction)
        glLightf(self.light_id, GL_SPOT_CUTOFF, 180.0)  # 180 degrees for directional light
        glLightf(self.light_id, GL_SPOT_EXPONENT, 0.0)  # Uniform light distribution

    # def set_direction(self, direction):
    #     """Set the direction of the directional light"""
    #     self.direction = direction
    #     if self.enabled:
    #         glLightfv(self.light_id, GL_SPOT_DIRECTION, self.direction)