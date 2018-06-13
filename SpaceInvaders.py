import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize pygame, settings and screen
    pygame.init()
    ai_settings = Settings()


    #Create a display window called "screen" , on which all of the games graphical elements will be drawn.
    #screen = pygame.display.set_mode((1200, 800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Space invaders by Goran Aviani")

    #make a ship
    ship = Ship(screen)


    #Start the main loop of the game
    while True:

        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)







if __name__ == "__main__":
    run_game()