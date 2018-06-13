import sys
import pygame

def check_events():
    # Listen for keyboard and mouse envents
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()