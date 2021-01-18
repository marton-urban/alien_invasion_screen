import sys
import pygame
from screen import screen
from ship import Ship
from bullet import Bullet
from settings import settings

"""Overall class to manage game assets and behavior."""
class AlienInvasion:

    """Initialize the game, and create game resources."""
    def __init__(self):
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    """Start the main loop for the game."""
    def run_game(self):
        # Watch for keyboard and mouse event.
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    """Respond to keypresses and mouse events."""
    def _check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_bullets(self):
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    """Update images on the screen, and flip to the new screen."""
    def _update_screen(self):
        # Redraw the screen and ship during each pass through the loop.
        screen.full.fill(screen.bg_color)
        self.ship.blitme()
        # Draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    """Create a new bullet and add it to the bullets group."""
    def _fire_bullet(self):
        if len(self.bullets) < settings.bullets_allowed:
            new_bullet = Bullet(self, self.ship)
            self.bullets.add(new_bullet)

    """Respond to keypresses."""
    def _check_keydown_events(self, event):
        # Move the ship to the left
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Move the ship to the right
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Quit the game
        elif event.key == pygame.K_q:
            sys.exit()
        # Fire a bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    """Respond to key releases."""
    def _check_keyup_events(self, event):
        # Stop moving the ship to the left
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # Stop moving the ship to the right
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
