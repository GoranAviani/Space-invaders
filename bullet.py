import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        # this below call in python 3 is super().__init__
        super(Bullet, self).__init__()
        self.screen = screen
