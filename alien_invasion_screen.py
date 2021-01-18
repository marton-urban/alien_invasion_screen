import sys
import pygame


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


"""Overall class to manage game assets and behavior."""
class AlienInvasion:
    """Initialize the game, and create game resources."""
    def __init__(self):
        self.settings = Settings()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    """Start the main loop for the game."""
    def run_game(self):
        # Watch for keyboard and mouse event.
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
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

    """Update images on the screen, and flip to the new screen."""
    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        screen.full.fill(screen.bg_color)
        self.ship.blitme()
        # Draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    """Create a new bullet and add it to the bullets group."""
    def _fire_bullet(self):
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


"""A class to manage the ship"""
class Ship:
    """Initialize the ship and set its starting position."""
    def __init__(self, ai_game):
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = screen.rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_left = False
        self.moving_right = False

    """ Update the ship's position based on the movement flag."""
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < screen.rect.right:
            self.x += self.settings.ship_speed
        # Update the rect object from self.x.
        self.rect.x = self.x

    """Draw the ship at its current location."""
    def blitme(self):
        screen.full.blit(self.image, self.rect)


"""A class to manage bullets fired from the ship"""
class Bullet(pygame.sprite.Sprite):
    """Create a bullet object at the ship's current position."""
    def __init__(self, ai_game, ship):
        super().__init__()
        self.settings = ai_game.settings

        self.speed = self.settings.bullet_speed
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = ship.rect.midtop

        # Store te bullet's position as a decimal value.
        self.y = float(self.rect.y)

    """Move the bullet up the screen."""
    def update(self):
        # Update the decimal position of the bullet.
        self.y -= self.speed
        # Update the rect position.
        self.rect.y = self.y

    """Draw the bullet to the screen."""
    def draw_bullet(self):
        pygame.draw.rect(screen.full, self.color, self.rect)


if __name__ == '__main__':
    screen = Screen()
    ai = AlienInvasion()
    ai.run_game()
