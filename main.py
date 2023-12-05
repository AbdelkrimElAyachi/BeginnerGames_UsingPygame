from typing import Any
import pygame


def initialize():
    (numsucces,numfails) = pygame.init()
    if(numfails>0):
        print(f"there are {numfails} that didn't get loaded")


class Bird(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, x , y):
       
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self) 

       self.images = []
       self.index = 0
       self.counter = 0
       for i in range(3):
           self.images.append(pygame.image.load(f"assets/bird{i+1}.png"))


       self.image = self.images[self.index]
       self.rect = self.image.get_rect()
       self.rect.center = [x,y]

    def update(self):

        self.counter += 1

        if(self.counter > 20):
            self.counter = 0
            self.index+=1
        
            if(self.index >= len(self.images)):
                self.index = 0
        
        self.image = self.images[self.index]
        


initialize()


clock = pygame.time.Clock()
fps = 60

# images
bg = pygame.image.load("assets/bg.png")
ground = pygame.image.load("assets/ground.png")



surface = pygame.display.set_mode((864,936),pygame.RESIZABLE)
pygame.display.set_caption("flappy bird")
Icon = pygame.image.load("logo2.png")
pygame.display.set_icon(Icon)



# creating rect
ground_scroll = 0
scroll_speed = 4



# 
b_group = pygame.sprite.Group()
flappy = Bird(100,int(936/2))
b_group.add(flappy)

running = True
while running:

    # frames pe defautl fps = 60
    clock.tick(fps)



    #  adding background
    surface.blit(bg,(0,0)) 
    surface.blit(ground,(ground_scroll,768))
    ground_scroll -= scroll_speed

    # plyaer
    b_group.draw(surface)
    b_group.update()

    if (ground_scroll<-35):
        ground_scroll = 0

    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
            running = False
       


    pygame.display.flip()