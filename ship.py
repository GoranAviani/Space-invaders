import pygame


class Ship():

    def __init__(self, screen):

        self.screen = screen
        #Load the ship image
        self.image = pygame.image.load('images/SpaceInvadersCannon.png')

        #Pygame treats game elements like rectangles (rects), even if not shaped as rectangle :)
        self.rect = self.image.get_rect()
        #position the ship at the bottom center of the screen:
        self.screen_rect = screen.get_rect()
        #start each new ship on the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement direction
        self.moving_right = False
        self.moving_left = False

    #Change ship position based on movement direction
    def update(self):
        if self.moving_right:
            # Move the ship to the right.
            self.rect.centerx += 1

        if self.moving_left:
            self.rect.centerx -= 1




    def blitme(self):
        #draw ship at its current location
        self.screen.blit(self.image, self.rect)