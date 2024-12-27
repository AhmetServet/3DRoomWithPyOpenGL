from lightning.light import Light
from OpenGL.GL import *
import time, math

class AmbientLight(Light):
    def __init__(self, light_id, ambient=(0.5, 0.5, 0.5, 1.0), 
                 diffuse=(0.0, 0.0, 0.0, 1.0), 
                 specular=(0.0, 0.0, 0.0, 1.0), 
                 position=(0.0, 0.0, 0.0, 1.0)):
        super().__init__(light_id, ambient, diffuse, specular, position)
        self.start_time = time.time()
        self.rgb_mode = False

    def enable(self):
        glEnable(self.light_id)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient)
        self.enabled = True

    def disable(self):
        glDisable(self.light_id)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        self.enabled = False

    def update_color_rgb(self):
        """Update the ambient color to create a continuous RGB color change effect"""
        elapsed_time = time.time() - self.start_time
        r = (1 + math.sin(elapsed_time)) / 2
        g = (1 + math.sin(elapsed_time + 2 * math.pi / 3)) / 2
        b = (1 + math.sin(elapsed_time + 4 * math.pi / 3)) / 2
        self.ambient = (r, g, b, 0.3)
        if self.enabled:
            glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient)

    def toggle_rgb_mode(self):
        """Toggle between RGB mode and single color mode"""
        self.rgb_mode = not self.rgb_mode
        if not self.rgb_mode:
            self.ambient = (0.5, 0.5, 0.5, 1.0)
            if self.enabled:
                glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient)


    def set_rgb_mode(self, mode):
        self.rgb_mode = mode

    def get_rgb_mode(self):
        return self.rgb_mode