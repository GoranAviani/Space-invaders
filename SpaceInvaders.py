import sys
import pygame


def run_game():
    #Initialize game and create screen
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space invaders by Goran Aviani")

    #Start the main loop of the game
    while True:

        #Listen for keyboard and mouse envents
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    #Make the most recently drawn screen visible
    pygame.display.flip()





if __name__ == "__main__":
    run_game()