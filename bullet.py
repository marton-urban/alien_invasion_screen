import pygame
from screen import screen
from settings import settings

"""A class to manage bullets fired from the ship"""
class Bullet(pygame.sprite.Sprite):
    """Create a bullet object at the ship's current position."""
    def __init__(self, ai_game, ship):
        super().__init__()

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.midtop = ship.rect.midtop

        # Store te bullet's position as a decimal value.
        self.y = float(self.rect.y)

    """Move the bullet up the screen."""
    def update(self):
        # Update the decimal position of the bullet.
        self.y -= settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    """Draw the bullet to the screen."""
    def draw_bullet(self):
        pygame.draw.rect(screen.full, settings.bullet_color, self.rect)
