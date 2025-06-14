import math
import numpy as np

def find_required_velocity_3d(qb_pos: tuple, target_pos: tuple, angle_deg: float) -> float | None:
        """
        Solves for the required minimum initial velocity to throw a football from QB to a target
        in 3D space, given a fixed launch angle.

        :param qb_pos: (x, y, z) position of quarterback (z = release height)
        :param target_pos: (x, y, z) position of target (e.g., WR hands)
        :param angle_deg: Launch angle in degrees
        :return: required velocity in yards/second, or None if impossible
        """
        gravity = 9.81 * 1.09361  # gravity in yards/sec²
        angle_rad = math.radians(angle_deg)

        dx = target_pos[0] - qb_pos[0]
        dy = target_pos[1] - qb_pos[1]
        dz = target_pos[2] - qb_pos[2]

        horizontal_dist = math.sqrt(dx**2 + dy**2)  # actual 2D distance on field
        cos_theta = math.cos(angle_rad)
        #sin_theta = math.sin(angle_rad)

        if cos_theta == 0:
            return None  

        # Use projectile motion formula adapted to 3D vertical displacement:
        # dz = horizontal_dist * tan(angle) - (g * horizontal_dist^2) / (2 * v^2 * cos^2(angle))
        numerator = gravity * horizontal_dist**2
        denominator = 2 * (horizontal_dist * math.tan(angle_rad) - dz) * cos_theta**2

        if denominator <= 0:
            return None

        v_squared = numerator / denominator

        if v_squared < 0:
            return None

        return math.sqrt(v_squared)


def find_leading_pass_3d(qb_pos, wr_pos, wr_vel, ball_speed, release_height):
        x_q, y_q, z_q = qb_pos          # QB position including height
        x_r, y_r, z_r = wr_pos          # WR position including height
        vx_r, vy_r = wr_vel             # WR velocity in x, y direction

        z_launch = release_height       # Use release height (not z_q) as vertical launch point
        gravity_yards_coefficient = 10.73  # gravity in yards/sec²

        best_solution = None

        for t in np.linspace(0.1, 5, 500):
            # Predict WR position at time t
            x_target = x_r + vx_r * t
            y_target = y_r + vy_r * t
            z_target = z_r  # WR catch height is their current z-position

            # Horizontal distance (ignoring height)
            dx = x_target - x_q
            dy = y_target - y_q
            horizontal_distance = np.hypot(dx, dy)

            # Required horizontal velocity
            v_horizontal = horizontal_distance / t
            if v_horizontal > ball_speed:
                continue  # can't reach the target in t seconds

            # Vertical velocity component needed
            vz = (z_target - z_launch + 0.5 * gravity_yards_coefficient * t**2) / t

            # Total velocity (magnitude of horizontal and vertical components)
            v_total = np.sqrt(v_horizontal ** 2 + vz ** 2)

            # Check if this total velocity is close enough to the QB's throw velocity
            if abs(v_total - ball_speed) < 0.5:
                angle_rad = np.arctan2(vz, v_horizontal)
                angle_deg = np.degrees(angle_rad)
                best_solution = {
                    "target": (x_target, y_target, z_target),
                    "time": t,
                    "angle_deg": angle_deg,
                    "vz": vz,
                    "vh": v_horizontal,
                    "v_total": v_total
                }
                break

        return best_solution