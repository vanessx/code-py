import pygame
import sys

from settings import Settings
from ship import Ship

class SidewaysShooter:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Sideways Shooter')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # start the main loop for the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            # redraw the scren during each pass through the loop
            self.screen.fill(self.settings.bg_color)        

            # make the most recently draw screen visible
            pygame.display.flip()


if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()
