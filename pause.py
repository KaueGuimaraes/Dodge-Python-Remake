import pygame
from pygame.locals import *


from sys import exit


menu = ['Resume', 'Restart', 'Quit']
color = {'orange' : (255, 215, 0),
        'white' : (255, 255, 255)}

choice_symbol = '>'

running = True
class Pause():
    def __init__(self, screen):
        self.choice_cont = 5
        self.last_choice_cont = 0
        self.choice = 0

        self.screen = screen
    
    def tick(self):
        self.key_listener()

    def render(self):
        self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 30)
        
        textsurface = self.MY_FONT.render('Paused', False, color['white'])
        self.screen.blit(textsurface, (10, 20))

        textsurface = self.MY_FONT.render('github.com/KaueGuimaraes', False, color['white'])
        self.screen.blit(textsurface, (10, self.screen.get_height() - 50))

        #Menu
        textsurface = self.MY_FONT.render('Dodge Python REMAKE', False, color['orange'])
        self.screen.blit(textsurface, ((self.screen.get_width() / 2) - 200, ((self.screen.get_height() / 2) - 150)))

        for c in range(0, len(menu)):
            if c == self.choice:
                self.screen.blit(self.MY_FONT.render(choice_symbol, False, color['orange']), (((self.screen.get_width() / 2) - 100) - 20, ((self.screen.get_height() / 2) - 100) + 30 * c))
            textsurface = self.MY_FONT.render(menu[c], False, color['orange'])
            self.screen.blit(textsurface, ((self.screen.get_width() / 2) - 100, ((self.screen.get_height() / 2) - 100) + 30 * c))
        #
    
    #Get
    def get_menu(self):
        return menu

    def get_choiche(self):
        return self.choice
    #
    
    def key_listener(self):
        self.choice_cont += 1
        if self.choice_cont > self.last_choice_cont:
            if pygame.key.get_pressed()[K_w]:
                self.choice -= 1

                if self.choice < 0:
                    self.choice = len(menu) - 1

                self.last_choice_cont = self.choice_cont + 5
            if pygame.key.get_pressed()[K_s]:
                self.choice += 1

                if self.choice >= len(menu):
                    self.choice = 0
                
                self.last_choice_cont = self.choice_cont + 5
            if pygame.key.get_pressed()[K_d]:
                print()
            if pygame.key.get_pressed()[K_a]:
                print()


def setup(screen):
    return Pause(screen)