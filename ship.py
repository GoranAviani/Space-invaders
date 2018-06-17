import pygame


class Ship():

    def __init__(self,ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image
        self.image = pygame.image.load('images/SpaceInvadersCannon.png')

        #Pygame treats game elements like rectangles (rects), even if not shaped as rectangle :)
        self.rect = self.image.get_rect()
        #position the ship at the bottom center of the screen:
        self.screen_rect = screen.get_rect()
        #Start each new ship on the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a deciaml value for the ships center: centerx can onyl store int and there is 1.5px change per moving ship
        self.center = float(self.rect.centerx)


        #Movement direction
        self.moving_right = False
        self.moving_left = False

    #Change ship position based on movement direction
    def update(self):
        # Update the ships center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Move the ship to the right by 1px.
            #self.rect.centerx += 1

            self.center += self.ai_settings.ship_speed_factor


        if self.moving_left and self.rect.left > 0:
            # Move the ship to the left by 1px.
            #self.rect.centerx -= 1

            self.center -= self.ai_settings.ship_speed_factor

        #Update the rect object from self.center to move by 1.5px
        self.rect.centerx = self.center

    def blitme(self):
        #draw ship at its current location
        self.screen.blit(self.image, self.rect)