# from typing import Any
import pygame


def initialize():
    (numsucces,numfails) = pygame.init()
    if (numfails>0):
        print(f"there are {numfails} that didn't get loaded")



class Bird(pygame.sprite.Sprite):


    def __init__(self, x , y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.gameOver = False
        self.vel = 0
        self.images = []
        self.index = 0
        self.counter = 0

        for i in range(3):
           self.images.append(pygame.image.load(f"./assets/bird{i+1}.png"))

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        if (self.rect.top < 0):
            self.gameOver = True
        self.animation()
        self.handle_graphity()


    def handle_graphity(self):
        # in case you lose the game
        if (self.rect.y > 718):
            self.gameOver = True
        else:
            #  graphity
            self.vel += 0.5
            self.rect.y += self.vel


    def animation(self):
        # animation
        self.counter += 1

        if (self.counter > 20):
            self.counter = 0
            self.index+=1
            if (self.index >= len(self.images)):
                self.index = 0

        # rotate the bird
        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -3)


    def jump(self):
        self.vel = -10
        




class Pipe(pygame.sprite.Sprite):

    def __init__(self,x,y,rotate,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.image.load("./assets/pipe.png")
        self.rect = self.image.get_rect()
        if rotate:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y]
        else:
            self.rect.topleft = [x,y]

    def update(self):
        self.rect.x -= self.speed
        if (self.rect.right < 0):
            self.kill()
         


class Button():
    def __init__(self,x,y) -> None:
        self.image = pygame.image.load("./assets/restart.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def draw(self,screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action = True

        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action