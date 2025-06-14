from ball import Ball
from Physics import ball_physics as bp
import math

qb_pos = (20, 26, 2) # z coordinate is release height. May modify.
wr_pos = (40, 26, 2.97)
wr_vel = (3, 0)  # running straight downfield
ball_speed = 23  # ~48 MPH
release_height = 0  # ~9 feet in yards

print(ball_speed * 2.04546) # conversion from yards per second to mph. Yards per second trips me up.

solution = bp.find_leading_pass_3d(qb_pos, wr_pos, wr_vel, ball_speed, release_height)
angle_of_release = round(solution["angle_deg"], 2)
target_coordinates = solution["target"]
required_ball_velocity = bp.find_required_velocity_3d(qb_pos, wr_pos, angle_of_release)
print(angle_of_release)
print(target_coordinates)
print(required_ball_velocity)

TIME_STEP = 0.01  # seconds


""" ball = Ball(start_x=20, start_y=26.65, velocity=17.517, angle_deg=angle_of_release, release_height=2.97)  # QB has thrown the ball.
time_step = 0.01

while ball.active:
    ball.update(time_step)
    print(ball)
 """

if solution:
    print(f"Throw to: {solution['target']}")
    print(f"Time to arrive: {solution['time']:.2f}s")
    print(f"Required angle: {solution['angle_deg']:.2f}°")
    print(f"Velocity: Horizontal = {solution['vh']:.2f}, Vertical = {solution['vz']:.2f}")
else:
    print("No viable pass found.")

def wr_position(t):
        """Returns WR position (x, y, z) at time t (sec)"""
        if t < 1.0:  # running straight downfield for 1 sec at 10 yds/sec
            return (20 + 10 * t, 26, 0)
        else:  # cutting to the sideline at 8 yds/sec after x=30
            return (30, 26 + 8 * (t - 1), 0)

def wr_velocity(t):
        """Returns WR velocity (vx, vy) at time t"""
        if t < 1.0:
            return (10, 0)
        else:
            return (0, 8)

def simulate():
    t = 0
    ball = None
    ball_launched = False
    throw_time = 1.5  # QB is trained to throw after WR makes the cut

    while True:
        wr_pos_now = wr_position(t)
        wr_vel_now = wr_velocity(t)

        # QB throws exactly at the planned route breakpoint
        if not ball_launched and t >= throw_time:
            lead = bp.find_leading_pass_3d(qb_pos, wr_pos_now, wr_vel_now, ball_speed=23.0, release_height=release_height)
            if not lead:
                print("No valid throw found.")
                return

            print(f"Throwing to target at {lead['target']} in {lead['time']:.2f}s with angle {lead['angle_deg']:.2f}° at t={t:.2f}s")
            air_distance = math.sqrt((lead['target'][0] - qb_pos[0])**2 + (lead['target'][1] - qb_pos[1])**2) # total air distance the QB is throwing
            print(air_distance)

            ball = Ball(
                    qb_pos[0],
                    qb_pos[1],
                    lead["target"][0],
                    lead["target"][1],
                    velocity=23.0,
                    angle_deg=lead["angle_deg"],
                    release_height=release_height
                        )

            ball_launched = True

        if ball_launched:
            ball.update(TIME_STEP)
            ball_now = ball.get_position()

            distance = math.sqrt(
                (wr_pos_now[0] - ball_now[0])**2 +
                (wr_pos_now[1] - ball_now[1])**2 +
                (wr_pos_now[2] - ball_now[2])**2
            )

            if distance < 0.5:
                print(f"\n🏈 Caught at t={t:.2f}s")
                print(f"WR Position:    x={wr_pos_now[0]:.2f}, y={wr_pos_now[1]:.2f}, z={wr_pos_now[2]:.2f}")
                print(f"Ball Position:  x={ball_now[0]:.2f}, y={ball_now[1]:.2f}, z={ball_now[2]:.2f}")
                return

            if not ball.active:
                print("Ball hit ground before WR could catch.")
                print(ball.get_position())
                return

        t += TIME_STEP
        if t > 6:
            print("Simulation timed out.")
            return

simulate()


