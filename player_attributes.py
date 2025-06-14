# player_attributes.py

class PlayerAttributes:
    def __init__(self, speed: int, strength: int, height: float, weight: int, route: int, agility: int = 0, acceleration: int = 0):

        """
        Holds physical and athletic traits for a player.

        :param speed: Top speed in yards per second
        :param strength: Arbitrary strength value (e.g., 0–100 scale)
        :param height: Height in inches
        :param weight: Weight in pounds
        :param agility: Change of direction quickness (optional)
        :param acceleration: Rate of speeding up (optional)
        """
        self.speed = speed
        self.strength = strength
        self.height = height
        self.weight = weight
        self.agility = agility
        self.acceleration = acceleration
        self.route = route

    def __str__(self):
        return (
            f"Speed: {self.speed} yds/s, Strength: {self.strength}, "
            f"Height: {self.height} in, Weight: {self.weight} lbs, "
            f"Agility: {self.agility}, Acceleration: {self.acceleration}"
        )
