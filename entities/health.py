import pygame


from random import randint


gros = 4
long = 8

class Health():
    def __init__(self, w, h, min_life, max_life, screen):
        self.x = randint(0 + w, screen.get_width() - w)
        self.y = randint(0 + h, screen.get_height() - h)
        self.w = w
        self.h = h
        self.life = randint(min_life, max_life)
    
    def tick(self, screen):
        self.cont = 0
    
    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.getX(), self.getY(), self.getWidth(), self.getHeight()))

        pygame.draw.rect(screen, (255, 0, 0), (self.getX() + (long / 2), self.getY() + ((self.getHeight() / 2 - (gros / 2))), self.getWidth() - long, gros)) #Horizontal
        pygame.draw.rect(screen, (255, 0, 0), (self.getX() + ((self.getWidth() / 2 - (gros / 2))), self.getY() + (long / 2), gros, self.getHeight() - long)) #Vertical
        

    #Get
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getWidth(self):
        return self.w
    
    def getHeight(self):
        return self.h
    
    def getLife(self):
        return self.life
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

    def setLife(self, newLife):
        self.life = newLife
    #
    
def setup(w, h, min_life, max_life, screen):
    return Health(w, h, min_life, max_life, screen)