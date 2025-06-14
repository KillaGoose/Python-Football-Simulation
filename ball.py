import math
import numpy as np

class Ball:
    def __init__(self, start_x: float, start_y: float, target_x: float, target_y: float,
                 velocity: float, angle_deg: float, release_height: float = 0.0):
        """
        :param start_x: Starting x-position (yards downfield)
        :param start_y: Starting y-position (yards across field width)
        :param target_x, target_y: Target position to aim for (to determine horizontal direction)
        :param velocity: Initial speed of the ball in yards/second
        :param angle_deg: Launch angle in degrees (0° = flat, 90° = vertical)
        :param release_height: Height at which the ball is released (yards)
        """
        self.x = start_x
        self.y = start_y
        self.z = release_height  # vertical starting position
        self.v = velocity
        self.release_height = release_height
        self.angle = math.radians(angle_deg)
        self.t = 0
        self.g = 9.81 * 1.09361  # ~10.73 yards/sec²
        self.active = True

        # Compute horizontal direction
        dx = target_x - start_x
        dy = target_y - start_y
        horizontal_distance = math.hypot(dx, dy)

        if horizontal_distance == 0:
            self.dir_x = 0
            self.dir_y = 0
        else:
            self.dir_x = dx / horizontal_distance
            self.dir_y = dy / horizontal_distance

        # Velocity components
        self.vh = self.v * math.cos(self.angle)  # horizontal velocity magnitude
        self.vz = self.v * math.sin(self.angle)  # vertical velocity (Z)
        self.vx = self.vh * self.dir_x           # horizontal X component
        self.vy = self.vh * self.dir_y           # horizontal Y component

    def update(self, dt: float):
        if not self.active:
            return

        self.t += dt

        # Move in horizontal plane
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Vertical position using kinematics
        self.z = self.release_height + self.vz * self.t - 0.5 * self.g * self.t ** 2

        # Check if it hits the ground
        if self.z <= 0:
            self.z = 0
            self.active = False

    def get_position(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return f"Ball at x={self.x:.2f}, y={self.y:.2f}, height={self.z:.2f} yards"
