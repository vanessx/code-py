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



if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()
