import pygame


class Ship:

    def __init__(self, ss_game):
        # start the ship and set its starting position
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # loading the ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the left center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # store a decimal value for the ship's vertical position
        self.y = float(self.rect.y)