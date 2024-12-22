from lightning.light import Light
from OpenGL.GL import *

class AreaLight(Light):
    def __init__(self, light_id, ambient=(0.2, 0.2, 0.2, 1.0), diffuse=(0.8, 0.8, 0.8, 1.0), specular=(1.0, 1.0, 1.0, 1.0), position=(0.0, 0.0, 1.0, 1.0), direction=(0.0, -1.0, 0.0)):
        super().__init__(light_id, ambient, diffuse, specular, position)
        self.direction = direction

    def enable(self):
        super().enable()
        glLightfv(self.light_id, GL_SPOT_DIRECTION, self.direction)
        glLightf(self.light_id, GL_SPOT_CUTOFF, 45.0)  # Set the cutoff angle for the spotlight
        