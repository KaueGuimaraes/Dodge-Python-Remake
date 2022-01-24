import pygame


from random import randint


gros = 2


class Enemy():
    def __init__(self, WIDTH, HEIGHT, min_w, max_w, min_h, max_h, min_speed, max_speed, min_damage, max_damage, volt):
        self.w = randint(min_w, max_w)
        self.h = randint(min_h, max_h)
        self.speed = randint(min_speed, max_speed)
        
        
        self.volt_cont = 0
        self.volt = volt


        self.damage = randint(min_damage, max_damage)

        self.type = 2

        self.color = (255, 215, 0)

        self.text =(str(randint(0, 1)) + str(randint(0, 1)))


        if randint(0, 100) <= 50:
            if randint(0, 1) == 0:
                self.x = 0
            else:
                self.x = randint(WIDTH - 50 - self.w, WIDTH - self.w)
        else:
            self.x = randint(0, WIDTH - self.w)
        
        if randint(0, 100) <= 50:
            if randint(0, 1) == 0:
                self.y = 0
            else:
                self.y = randint(HEIGHT - 50 - self.h, HEIGHT - self.h)
        else:
            self.y = randint(0, HEIGHT - self.h)
        

        self.MY_FONT = pygame.font.SysFont('Comic Sans MS', self.getHeight())


        self.dire = []
        if randint(0, 100) <= 15:
            rand = randint(0, 4)
            if rand == 0:
                self.dire.append('right')
                self.dire.append('right')
            if rand == 1:
                self.dire.append('left')
                self.dire.append('left')
            if rand == 2:
                self.dire.append('up')
                self.dire.append('up')
            if rand >= 3:
                self.dire.append('down')
                self.dire.append('down')
        else:
            if randint(0, 1) == 0:
                self.dire.append('right')
            else:
                self.dire.append('left')
            if randint(0, 1) == 0:
                self.dire.append('up')
            else:
                self.dire.append('down')
    
    def tick(self, screen):
        self.goDire()
        self.back(screen.get_width(), screen.get_height())
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.getX(), self.getY(), self.getWidth(), self.getHeight()))
        pygame.draw.rect(screen, (0, 0, 0), (self.getX() + (gros / 2), self.getY() + (gros / 2), self.getWidth() - gros, self.getHeight() - gros))

        textsurface = self.MY_FONT.render(self.text, False, (255, 255, 255))
        
        screen.blit(textsurface, (self.getX() + (self.getWidth() / 3), self.getY()))

    #Get
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getWidth(self):
        return self.w
    
    def getHeight(self):
        return self.h
    
    def getSpeed(self):
        return self.speed
    
    def getDamage(self):
        return self.damage
    
    def getType(self):
        return self.type
    #
    #Set
    def setX(self, newX):
        self.x = newX
    
    def setY(self, newY):
        self.y = newY
    
    def setWidth(self, newWidth):
        self.w = newWidth
    
    def setHeight(self, newHeight):
        self.h = newHeight
    
    def setSpeed(self, newSpeed):
        self.speed = newSpeed
    #

    def kill(self, screen):
        if self.volt_cont >= self.volt:
            print('agora deleta')
            return True
        else:
            return False

    #Move
    def goDire(self):
        if self.dire[0] == 'right':
            self.right()
        if self.dire[0] == 'left':
            self.left()
        if self.dire[0] == 'up':
            self.up()
        if self.dire[0] == 'down':
            self.down()
        
        if self.dire[1] == 'right':
            self.right()
        if self.dire[1] == 'left':
            self.left()
        if self.dire[1] == 'up':
            self.up()
        if self.dire[1] == 'down':
            self.down()


    def right(self):
        self.setX(self.getX() + self.getSpeed())
    
    def left(self):
        self.setX(self.getX() - self.getSpeed())
    
    def down(self):
        self.setY(self.getY() + self.getSpeed())
    
    def up(self):
        self.setY(self.getY() - self.getSpeed())
    #
    #Back
    def back(self, WIDTH, HEIGHT):
        if self.getX() >= WIDTH - self.getWidth():
            self.setX(0 + self.getWidth())
            self.volt_cont += 1
        elif self.getX() <= 0:
            self.setX(WIDTH - self.getWidth())
            self.volt_cont += 1
        
        if self.getY() >= HEIGHT - self.getHeight():
            self.setY(0 + self.getHeight())
            self.volt_cont += 1
        elif self.getY() <= 0:
            self.setY(HEIGHT - self.getHeight())
            self.volt_cont += 1
    #
    
def setup(WIDTH, HEIGHT, min_w, max_w, min_h, max_h, min_speed, max_speed, min_damage, max_damage, volt):
    return Enemy(WIDTH, HEIGHT, min_w, max_w, min_h, max_h, min_speed, max_speed, min_damage, max_damage, volt)