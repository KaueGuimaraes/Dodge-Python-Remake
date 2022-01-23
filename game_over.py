import pygame
from pygame.locals import *


from sys import exit


color = {'orange' : (255, 215, 0),
        'white' : (255, 255, 255),
        'red' : (255, 0, 0),}

running = True
class Game_over():
    def __init__(self, screen, fps):
        self.screen = screen

        self.fps = fps

        self.show = True

        self.cont = 0
    
    def tick(self):
        self.cont += 1

        if self.cont >= self.fps / 2:
            if self.show:
                self.show = False
            else:
                self.show = True
            self.cont = 0

    def render(self):
        self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = self.MY_FONT.render('Game Over', False, color['red'])

        self.screen.blit(textsurface, (self.screen.get_width() / 2 - (60 * len('Game Over')), 50))
        if self.show:
            self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 30)
            self.screen.blit(self.MY_FONT.render('> Press SPACE to restart', False, color['red']), (self.screen.get_width() / 2 - (60 * len('Game Over') + 30), 200))


def setup(screen, fps):
    return Game_over(screen, fps)