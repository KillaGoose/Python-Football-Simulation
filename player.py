# player.py

class Player:
    def __init__(self, name: str, position: str, team: str, x: float, y: float):
        """
        :param name: Player's name
        :param position: Position on the field (e.g., 'WR', 'QB', etc.)
        :param team: Team identifier (e.g., 'HOME', 'AWAY')
        :param x: Starting x-coordinate (yards downfield)
        :param y: Starting y-coordinate (yards across field width)
        """
        self.name = name
        self.position = position
        self.team = team
        self.x = x
        self.y = y

    def move_to(self, x: float, y: float):
        """Move player to an exact coordinate."""
        self.x = x
        self.y = y

    def move_by(self, dx: float, dy: float):
        """Move player by an offset (e.g., 5 yards forward and 2 yards right)."""
        self.x += dx
        self.y += dy

    def get_position(self) -> tuple:
        return (self.x, self.y)

    def __str__(self):
        return f"{self.name} ({self.position}, {self.team}) at ({self.x:.1f}, {self.y:.1f})"
