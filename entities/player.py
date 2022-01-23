import pygame

class Player():
    def __init__(self, x, y, w, h, speed, life):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.life = life

        self.max_life = life
    
    def tick(self, screen):
        self.back(screen.get_width(), screen.get_height())

        if self.getLife() > self.max_life:
            self.setLife(self.max_life)
    
    def render(self, screen):
        pygame.draw.rect(screen, (255, 215, 0), (self.getX(), self.getY(), self.getWidth(), self.getHeight())) #Player

        pygame.draw.rect(screen, (128, 128, 128), (5, 5, self.max_life * 3, 10)) #Back life
        pygame.draw.rect(screen, (255, 0, 0), (5, 5, self.getLife() * 3, 10)) #Life

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
    
    def setSpeed(self, newSpeed):
        self.speed = newSpeed

    def setLife(self, newLife):
        self.life = newLife
    #
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
    def back(self, WIDTH, HEIGHT):
        if self.getX() >= WIDTH - self.getWidth():
            self.setX(0 + self.getWidth())
        elif self.getX() <= 0:
            self.setX(WIDTH - self.getWidth())
        
        if self.getY() >= HEIGHT - self.getHeight():
            self.setY(0 + self.getHeight())
        elif self.getY() <= 0:
            self.setY(HEIGHT - self.getHeight())
    #
    
def setup(x, y, w, h, speed, life):
    return Player(x, y, w, h, speed, life)