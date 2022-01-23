import pygame
from pygame.locals import *


from sys import exit


running = True
class Pause():
    def __init__(self, screen):
        pygame.init()

        self.screen = screen
    
    def tick(self):
        self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self):
        self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = self.MY_FONT.render('Paused', False, (255, 255, 255))
        self.screen.blit(textsurface, (10, 20))

    def key_listener(self):
        if pygame.key.get_pressed()[K_w]:
            print()
        if pygame.key.get_pressed()[K_s]:
            print()
        if pygame.key.get_pressed()[K_d]:
            print()
        if pygame.key.get_pressed()[K_a]:
            print()
        
        if pygame.key.get_pressed()[K_ESCAPE]:
            print('esc')
    
    def quit(self):
        pygame.quit()
        exit()


def setup(screen):
    return Pause(screen)