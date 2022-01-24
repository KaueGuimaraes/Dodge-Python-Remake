import pygame

class Text():
    def __init__(self, x, y, w, h, speed, text, type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.text = text
        self.type = type

        self.cont = 0

        self.MY_FONT = pygame.font.SysFont('Comic Sans MS', 30)
    
    def tick(self, screen):
        self.cont += 1

        if self.cont >= 1:
            self.up()
            self.cont = 0
    
    def render(self, screen):
        if self.type == 0:
            textsurface = self.MY_FONT.render(self.text, False, (255, 0, 0))
        elif self.type == 1:
            textsurface = self.MY_FONT.render(self.text, False, (0, 128, 0))
        elif self.type == 2:
            textsurface = self.MY_FONT.render(self.text, False, (255, 215, 0))
        
        screen.blit(textsurface, (self.getX(), self.getY()))

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
    #Move
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
    def leaveMap(self, screen):
        if self.getX() > screen.get_width():
            return True
        elif self.getX() < 0:
            return True
        elif self.getY() > screen.get_height():
            return True
        elif self.getY() < 0:
            return True
        else:
            return False
    #
    
def setup(x, y, w, h, speed, text, type):
    return Text(x, y, w, h, speed, text, type)