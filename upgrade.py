import pygame
from settings import *

class Upgrade:
    def __init__(self, player):
        
        self.display_surface = pygame.display.get_surface()
        self.player = player

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            pass
    def display(self):
        self.display_surface.fill('black')