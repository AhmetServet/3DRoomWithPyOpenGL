import math

class Camera:
    def __init__(self, pos=None, horizontal_angle=-1.50, vertical_angle=0.0, radius=8.0, speed=0.2, zoom_speed=1.0):
        self.pos = pos if pos is not None else [0.0, 0.0, -radius]
        self.horizontal_angle = horizontal_angle
        self.vertical_angle = vertical_angle
        self.radius = radius
        self.speed = speed
        self.zoom_speed = zoom_speed

    def move(self, direction):
        if direction == "left":
            self.horizontal_angle += self.speed
        elif direction == "right":
            self.horizontal_angle -= self.speed
        elif direction == "up":
            self.vertical_angle += self.speed
        elif direction == "down":
            self.vertical_angle -= self.speed
        elif direction == "in":
            self.radius -= self.zoom_speed
        elif direction == "out":
            self.radius += self.zoom_speed

        # Clamp the vertical angle to prevent flipping
        self.vertical_angle = max(-math.pi / 2, min(math.pi / 2, self.vertical_angle))

        # Clamp the radius to prevent going through the origin
        self.radius = max(0.1, self.radius)

        # Calculate new camera position
        self.pos[0] = self.radius * math.cos(self.horizontal_angle) * math.cos(self.vertical_angle)
        self.pos[1] = self.radius * math.sin(self.vertical_angle)
        self.pos[2] = self.radius * math.sin(self.horizontal_angle) * math.cos(self.vertical_angle)

    def get_position(self):
        return self.pos
