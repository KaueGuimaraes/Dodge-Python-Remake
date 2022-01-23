import pygame
from pygame.locals import *

from sys import exit


from random import randint


import entities.player as p
import entities.enemy as e


#Color
color = dict()

color = {
    'white' : (255, 255, 255),
    'red' : (255, 0, 0),
}
#

#Screen
WIDTH = 1280
HEIGHT = 720
SCALE = 1
#

enemys = []

running = True
class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Name')

        self.player = p.setup(300 * SCALE, 300 * SCALE, 25 * SCALE, 25 * SCALE, 10.6 * SCALE, 50) # x, y, width, height, speed, life

        print('Hello, World!')
    
    def main(self):
        self.clock.tick(30)
        self.screen.fill((0, 0, 0))

        self.tick()
        self.render()

        pygame.display.update()
    
    def tick(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()
        
        self.key_listener()

        if self.player.getLife() <= 0:
            self.quit()

        #Enemys
        if randint(0, 100) <= 30:
            enemys.append(e.setup(WIDTH * SCALE, HEIGHT * SCALE, 10 * SCALE, 60 * SCALE, 10 * SCALE, 60 * SCALE, 5 * SCALE, 10 * SCALE, 1, 2))
        
        cont = 0
        for c in enemys:
            #Collide
            self.rect1 = pygame.Rect(c.getX(), c.getY(), c.getWidth(), c.getHeight())
            self.rect2 = pygame.Rect(self.player.getX(), self.player.getY(), self.player.getWidth(), self.player.getHeight())
            if pygame.Rect.colliderect(self.rect1, self.rect2):
                self.player.setLife(self.player.getLife() - c.getDamage())
            #
            if c.getX() < 0 or c.getY() < 0 or c.getX() > WIDTH or c.getY() > HEIGHT:
                del(enemys[cont])
            c.tick(self.screen)
            
            cont += 1
        #

        self.player.tick(self.screen)

    def render(self):
        '''for c in range(0, self.player.getLife()):
            pygame.draw.rect(self.screen, color['red'], (10+(c*35) * SCALE, 10 * SCALE, 25 * SCALE, 25 * SCALE))'''

        for c in enemys:
            c.render(self.screen)
        
        self.player.render(self.screen)

    def key_listener(self):
        if pygame.key.get_pressed()[K_w]:
            self.player.up()
        if pygame.key.get_pressed()[K_s]:
            self.player.down()
        if pygame.key.get_pressed()[K_d]:
            self.player.right()
        if pygame.key.get_pressed()[K_a]:
            self.player.left()
    
    def quit():
        pygame.quit()
        exit()


game = Game()
while running:
    game.main()