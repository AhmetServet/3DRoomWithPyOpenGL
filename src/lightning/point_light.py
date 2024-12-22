from lightning.light import Light
from OpenGL.GL import *

class PointLight(Light):
    def __init__(self, light_id, ambient=(0.2, 0.2, 0.2, 1.0), diffuse=(0.8, 0.8, 0.8, 1.0), specular=(1.0, 1.0, 1.0, 1.0), position=(0.0, 0.0, 1.0, 1.0), attenuation=(1.0, 0.0, 0.0)):
        super().__init__(light_id, ambient, diffuse, specular, position)
        self.attenuation = attenuation

    def enable(self):
        super().enable()
        glLightf(self.light_id, GL_CONSTANT_ATTENUATION, self.attenuation[0])
        glLightf(self.light_id, GL_LINEAR_ATTENUATION, self.attenuation[1])
        glLightf(self.light_id, GL_QUADRATIC_ATTENUATION, self.attenuation[2])

    def set_attenuation(self, constant, linear, quadratic):
        self.attenuation = (constant, linear, quadratic)
        glLightf(self.light_id, GL_CONSTANT_ATTENUATION, constant)
        glLightf(self.light_id, GL_LINEAR_ATTENUATION, linear)
        glLightf(self.light_id, GL_QUADRATIC_ATTENUATION, quadratic)