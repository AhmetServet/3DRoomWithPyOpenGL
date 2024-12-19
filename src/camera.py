import math

class Camera:
    def __init__(self, pos=None, horizontal_angle=0.0, vertical_angle=0.0, radius=5.0, speed=0.2):
        self.pos = pos if pos is not None else [0.0, 0.0, -5]
        self.horizontal_angle = horizontal_angle
        self.vertical_angle = vertical_angle
        self.radius = radius
        self.speed = speed

    def move(self, direction):
        if direction == "left":
            self.horizontal_angle -= self.speed
        elif direction == "right":
            self.horizontal_angle += self.speed
        elif direction == "up":
            self.vertical_angle += self.speed
        elif direction == "down":
            self.vertical_angle -= self.speed

        # Clamp the vertical angle to prevent flipping
        self.vertical_angle = max(-math.pi / 2, min(math.pi / 2, self.vertical_angle))

        # Calculate new camera position
        self.pos[0] = self.radius * math.cos(self.horizontal_angle) * math.cos(self.vertical_angle)
        self.pos[1] = self.radius * math.sin(self.vertical_angle)
        self.pos[2] = self.radius * math.sin(self.horizontal_angle) * math.cos(self.vertical_angle)

    def get_position(self):
        return self.pos
