import pygame
from settings import Settings
from ship import Ship
import game_functions as Gf

def run_game():
    #Initialize pygame, settings and screen
    pygame.init()
    ai_settings = Settings()


    #Create a display window called "screen" , on which all of the games graphical elements will be drawn.
    #screen = pygame.display.set_mode((1200, 800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Space invaders by Goran Aviani")

    #make a ship
    space_ship = Ship(ai_settings, screen)


    #Start the main loop of the game
    while True:

        Gf.check_events(space_ship)
        space_ship.update()
        Gf.update_screen(ai_settings, screen, space_ship)







if __name__ == "__main__":
    run_game()