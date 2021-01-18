import pygame
from screen import screen
from settings import settings


"""A class to manage the ship"""
class Ship:
    """Initialize the ship and set its starting position."""
    def __init__(self, ai_game):

        # Load the ship image and then set correct position.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = screen.rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_left = False
        self.moving_right = False

    """ Update the ship's position based on the movement flag."""
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= settings.ship_speed
        if self.moving_right and self.rect.right < screen.rect.right:
            self.x += settings.ship_speed
        # Update the rect object from self.x.
        self.rect.x = self.x

    """Draw the ship at its current location."""
    def blitme(self):
        screen.full.blit(self.image, self.rect)
