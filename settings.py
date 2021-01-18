"""A class to store all settings for Alien Invasion."""
class Settings:
    """Initialize the game's settings."""
    def __init__(self):

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60, 60)
        self.bullets_allowed = 3

settings = Settings()
