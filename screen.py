import pygame

"""A class to store all settings for the screen."""
class Screen:
    """Initialize the game's screen."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230, 230)
        self.full = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.fill = self.full.fill(self.bg_color)
        self.rect = self.full.get_rect()

screen = Screen()
