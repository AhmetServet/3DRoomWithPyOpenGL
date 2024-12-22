from lightning.light import Light
from OpenGL.GL import *

class AmbientLight(Light):
    def __init__(self, light_id, ambient=(1.0,1.0,1.0, 1.0)):
        super().__init__(light_id, ambient, (0.0, 0.0, 0.0, 1.0), (0.0, 0.0, 0.0, 1.0), (0.0, 0.0, 0.0, 1.0))

    def enable(self):
        glEnable(self.light_id)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient)
        self.enabled = True