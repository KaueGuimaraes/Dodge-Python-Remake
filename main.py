import pygame
from pygame.locals import *

from sys import exit


from random import randint


import entities.player as p
import entities.text as t
import entities.health as h


import entities.enemys.enemy1 as e
import entities.enemys.enemy2 as e2
import entities.enemys.enemy3 as e3


import pause as ps
import game_over as go


#Color
color = dict()

color = {
    'white' : (255, 255, 255),
    'red' : (255, 0, 0),
    'violet' : (221,160,221),
}
#

#Screen
WIDTH = 1280
HEIGHT = 720
SCALE = 1
#

enemys = []
texts = []
healths = []

fps = 30

levels = ['easy', 'normal', 'hard', 'very hard', 'impossible']

running = True
class Game():
    def __init__(self):
        self.is_paused = False
        self.pause_cont = 5
        self.last_pause_cont = 0

        self.is_game_over = False

        self.is_status = False
        self.status_cont = 5
        self.last_status_cont = 0
        self.show_status = []

        self.time_cont = 0
        self.time = 0
        
        
        self.max_healths = 10
        
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Name')

        self.pauser = ps.setup(self.screen)
        self.game_over = go.setup(self.screen, fps)

        self.player = p.setup(300 * SCALE, 300 * SCALE, 15 * SCALE, 15 * SCALE, 10.6 * SCALE, 50) # x, y, width, height, speed, life

        self.new_game = False

        print('Hello, World!')
    
    def main(self):
        self.clock.tick(fps)
        self.screen.fill((0, 0, 0))

        #Restart game
        if self.new_game:
            game = Game()

            self.clear()

            while True:
                game.main()
        #

        self.tick()
        self.render()

        pygame.display.update()
    
    def tick(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
        
        self.key_listener()

        if self.is_paused:
            self.pauser.tick()
        elif self.is_game_over:
            self.game_over.tick()
        else:
            #Timer
            self.time_cont += 1
            if self.time_cont >= fps:
                self.time += 1
                self.time_cont = 0
            #
            
            if self.player.getLife() <= 0:
                self.player.setLife(self.player.max_life)
                #self.is_game_over = True
                #self.quit()

            #Enemys
            if randint(0, 100) <= 30:
                enemys.append(e.setup(WIDTH * SCALE, HEIGHT * SCALE, 10 * SCALE, 60 * SCALE, 10 * SCALE, 60 * SCALE, 5 * SCALE, 10 * SCALE, 1, 2))
            
            if randint(0, 100) <= 10:
                enemys.append(e2.setup(WIDTH * SCALE, HEIGHT * SCALE, 10 * SCALE, 60 * SCALE, 10 * SCALE, 60 * SCALE, 5 * SCALE, 10 * SCALE, 1, 2, 2))
            
            if randint(0, 100) <= 50:
                enemys.append(e3.setup(WIDTH * SCALE, HEIGHT * SCALE, 30 * SCALE, 60 * SCALE, 10 * SCALE, 60 * SCALE, 5 * SCALE, 10 * SCALE, 1, 2, 2))
            #
            cont = 0
            for c in enemys:
                #Enemy collide
                self.rect1 = pygame.Rect(c.getX(), c.getY(), c.getWidth(), c.getHeight())
                self.rect2 = pygame.Rect(self.player.getX(), self.player.getY(), self.player.getWidth(), self.player.getHeight())
                if pygame.Rect.colliderect(self.rect1, self.rect2):
                    self.player.setLife(self.player.getLife() - c.getDamage())
                    texts.append(t.setup(c.getX(), c.getY(), 10, 10, 10, 'Hit', c.getType()))
                #
                if c.kill(self.screen):
                    del(enemys[cont])
                c.tick(self.screen)
                
                cont += 1
            #
            #Healths
            if len(healths) < self.max_healths:
                if randint(0, 100) <= 3:
                    healths.append(h.setup(25 * SCALE, 25 * SCALE, 3, 10, self.screen))
            
            cont = 0
            for c in healths:
                self.rect1 = pygame.Rect(c.getX(), c.getY(), c.getWidth(), c.getHeight())
                self.rect2 = pygame.Rect(self.player.getX(), self.player.getY(), self.player.getWidth(), self.player.getHeight())
                #Health collide
                if pygame.Rect.colliderect(self.rect1, self.rect2):
                    self.player.setLife(self.player.getLife() + c.getLife())
                    del(healths[cont])
                #
                c.tick(self.screen)
                cont += 1
            #
            #Texts
            cont = 0
            for c in texts:
                c.tick(self.screen)
                if c.leaveMap(self.screen):
                    del(texts[cont])
                cont += 1
            #

            self.player.tick(self.screen)

    def render(self):
        '''for c in range(0, self.player.getLife()):
            pygame.draw.rect(self.screen, color['red'], (10+(c*35) * SCALE, 10 * SCALE, 25 * SCALE, 25 * SCALE))'''
        
        if self.is_game_over:
            self.game_over.render()
        else:
            for c in enemys:
                c.render(self.screen)
            for c in healths:
                c.render(self.screen)
            self.player.render(self.screen)
            for c in texts:
                c.render(self.screen)
            
            if self.is_paused:
                self.pauser.render()
            else:
                #Timer
                self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 20)
                self.screen.blit(self.MY_FONT.render('Timer : ' + str(self.time), False, color['red']), (10, 20))
                #

            
            if self.is_status:
                self.status()

    def key_listener(self):
        #Game over
        if self.is_game_over:
            if pygame.key.get_pressed()[K_SPACE]:
                #Restart game
                game = Game()
                self.clear()
                
                while True:
                    game.main()
                #
        #
        #To pause
        else:
            self.pause_cont += 1
            if pygame.key.get_pressed()[K_ESCAPE]:
                if self.pause_cont > self.last_pause_cont:
                    print('esc')
                    
                    if self.is_paused:
                        self.is_paused = False
                    else:
                        self.is_paused = True
                    self.last_pause_cont = self.pause_cont + 5
            #
            #To Status
            self.status_cont += 1
            if pygame.key.get_pressed()[K_F5]:
                if self.status_cont > self.last_status_cont:
                    print('status')
                    
                    if self.is_status:
                        self.is_status = False
                    else:
                        self.is_status = True
                    self.last_status_cont = self.status_cont + 5
            #
            if self.is_paused == False:
                if pygame.key.get_pressed()[K_w]:
                    self.player.up()
                if pygame.key.get_pressed()[K_s]:
                    self.player.down()
                if pygame.key.get_pressed()[K_d]:
                    self.player.right()
                if pygame.key.get_pressed()[K_a]:
                    self.player.left()
            else:
                #is_paused = True
                if pygame.key.get_pressed()[K_RETURN]:
                    if self.pauser.get_menu()[self.pauser.get_choiche()].lower() == 'resume':
                        self.is_paused = False
                        print('resume')
                    elif self.pauser.get_menu()[self.pauser.get_choiche()].lower() == 'restart':
                        self.new_game = True
                        print('restart')
                    elif self.pauser.get_menu()[self.pauser.get_choiche()].lower() == 'quit':
                        print('quit')
                        self.quit()
                #

    def get_player(self):
        return self.player

    def status(self):
        self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 30) #Font
        self.screen.blit(self.MY_FONT.render('STATS FOR NERDS', False, color['violet']), (10, 70))

        self.show_status = []
        self.show_status.append(['Enemys', len(enemys)]) #Enemys
        self.show_status.append(['Healths', len(healths)]) #Healths
        self.show_status.append(['Texts', len(texts)])

        self.show_status.append(['', ''])

        self.show_status.append(['Max Life', self.player.max_life])
        self.show_status.append(['Life', self.player.getLife()])

        self.show_status.append(['', ''])

        self.show_status.append(['X', self.player.getX()])
        self.show_status.append(['Y', self.player.getY()])

        self.show_status.append(['', ''])

        self.show_status.append(['Width', self.player.getWidth()])
        self.show_status.append(['Height', self.player.getHeight()])

        print(self.show_status)

        self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 20)
        self.cont = 1
        for c in self.show_status:
            if c[0] == '':
                self.screen.blit(self.MY_FONT.render('', False, color['violet']), (10, (30) + (30 * self.cont)))
            else:
                self.screen.blit(self.MY_FONT.render(c[0] + ' : ' + str(c[1]), False, color['violet']), (10, (100) + (25 * self.cont)))
            self.cont += 1

    def clear(self):
        enemys.clear()
        healths.clear()
        texts.clear()

    def quit(self):
        pygame.quit()
        exit()


game = Game()
while running:
    game.main()