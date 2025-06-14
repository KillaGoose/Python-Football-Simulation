# field.py
import os
class Field:
    def __init__(self):
        self.total_length_yards = 120  
        self.playable_length_yards = 100
        self.width_yards = 53.3

       
        self.hash_mark_left = 23.375
        self.hash_mark_right = self.width_yards - 23.375

        self.endzone_depth = 10

        self.ball_position = (25, self.width_yards / 2)

    def is_in_bounds(self, x: float, y: float) -> bool:
        return (
            0 <= x <= self.total_length_yards and
            0 <= y <= self.width_yards
        )

    def is_in_endzone(self, x: float) -> bool:
        return x < self.endzone_depth or x > (self.total_length_yards - self.endzone_depth)

    def get_hash_marks(self) -> tuple:
        return (self.hash_mark_left, self.hash_mark_right)

    def set_ball_position(self, x: float, y: float):
        if not self.is_in_bounds(x, y):
            raise ValueError(f"Position ({x}, {y}) is out of bounds.")
        self.ball_position = (x, y)

    def __str__(self):
        return (
            f"NFL Field: {self.total_length_yards} yards x {self.width_yards} yards\n"
            f"Endzones: {self.endzone_depth} yards deep\n"
            f"Hash marks at y={self.hash_mark_left:.2f} and y={self.hash_mark_right:.2f}\n"
            f"Ball position: {self.ball_position}"
        )
    
    def draw(self, players):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal

        display_length = 50
        display_width = 50

        scale_x = self.total_length_yards / display_length
        scale_y = self.width_yards / display_width

        for y in range(display_width):
            row = ""
            for x in range(display_length):
                field_x = x * scale_x
                field_y = y * scale_y

                player_here = next(
                    (p for p in players if int(p.x // scale_x) == x and int(p.y // scale_y) == y),
                    None
                )

                if player_here:
                    # Use first letter of position as symbol (e.g., 'W' for WR)
                    row += player_here.position[0]
                elif x == 0 or x == display_length - 1:
                    row += "="
                elif x % 10 == 0:
                    row += "|"
                else:
                    row += "."
            print(row)





