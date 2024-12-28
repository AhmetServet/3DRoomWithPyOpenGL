from OpenGL.GL import *

class Light:
    def __init__(self, light_id, ambient=(0.2, 0.2, 0.2, 1.0), diffuse=(0.8, 0.8, 0.8, 1.0), specular=(1.0, 1.0, 1.0, 1.0), position=(0.0, 0.0, 1.0, 0.0)):
        self.light_id = light_id
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.position = position
        self.enabled = False

    def enable(self):
        glEnable(self.light_id)
        glLightfv(self.light_id, GL_AMBIENT, self.ambient)
        glLightfv(self.light_id, GL_DIFFUSE, self.diffuse)
        glLightfv(self.light_id, GL_SPECULAR, self.specular)
        glLightfv(self.light_id, GL_POSITION, self.position)
        self.enabled = True

    def disable(self):
        glDisable(self.light_id)
        self.enabled = False

    def set_ambient(self, ambient):
        self.ambient = ambient
        glLightfv(self.light_id, GL_AMBIENT, self.ambient)

    def set_diffuse(self, diffuse):
        self.diffuse = diffuse
        glLightfv(self.light_id, GL_DIFFUSE, self.diffuse)

    def set_specular(self, specular):
        self.specular = specular
        glLightfv(self.light_id, GL_SPECULAR, self.specular)

    def set_position(self, position):
        self.position = position
        glLightfv(self.light_id, GL_POSITION, self.position)