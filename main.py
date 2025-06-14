from ball import Ball

qb_pos = (20, 26, 2.97) # z coordinate is release height. May modify.
wr_pos = (40, 26, 2.97)
wr_vel = (3, 0)  # running straight downfield
ball_speed = 17.08  # ~48 MPH
release_height = 2.97  # ~9 feet in yards

solution = Ball.find_leading_pass_3d(qb_pos, wr_pos, wr_vel, ball_speed, release_height)
angle_of_release = round(solution["angle_deg"], 2)
target_coordinates = solution["target"]
required_ball_velocity = Ball.find_required_velocity_3d(qb_pos, wr_pos, angle_of_release)
print(angle_of_release)
print(target_coordinates)
print(required_ball_velocity)


ball = Ball(start_x=20, start_y=26.65, velocity=17.517, angle_deg=angle_of_release, release_height=2.97)  # QB has thrown the ball.
time_step = 0.01

while ball.active:
    ball.update(time_step)
    print(ball)


if solution:
    print(f"Throw to: {solution['target']}")
    print(f"Time to arrive: {solution['time']:.2f}s")
    print(f"Required angle: {solution['angle_deg']:.2f}°")
    print(f"Velocity: Horizontal = {solution['vh']:.2f}, Vertical = {solution['vz']:.2f}")
else:
    print("No viable pass found.")


