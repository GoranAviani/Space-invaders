import sys
import pygame

def check_events():
    # Listen for keyboard and mouse envents
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):

    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()


    # Make the most recently drawn screen visible
    pygame.display.flip()