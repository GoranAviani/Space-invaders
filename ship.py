import pygame


class Ship():

    def __init__(self, screen):

        self.screen = screen

        #Load the ship image
        self.image = pygame.image.load('images/ship.bmp')

        #Pygame treats game elements like rectangles (rects), even if not shaped as rectangle :)
        self.rect = self.image.get_rect()
        #position the ship at the bottom center of the screen:
        self.screen_rect = screen.get_rect()
        #start each new ship on the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #draw ship at its current location
        self.screen.blit(self.image, self.rect)