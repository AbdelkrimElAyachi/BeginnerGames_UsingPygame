import pygame
import random

# setting up colors
bBLUE = (0,255,255)

(nbrSuccess,nbrFails)=pygame.init()
if(nbrFails > 0):
    print(f"failed to load {nbrFails} modules")
    exit(1)

# setting up pygame objects and variables
(window_width,window_height) = pygame.display.get_desktop_sizes()[0]
clock = pygame.time.Clock()
# setting up variables


# setting up the window
window_surface = pygame.display.set_mode((window_width,window_height-63))
pygame.display.set_caption("snake")
logo = pygame.image.load("assets/logo.jpg")
pygame.display.set_icon(logo)


pygame.draw.rect(window_surface,bBLUE,[0,0,50,50])

print(pygame.display.get_desktop_sizes()[0])

running = True
while running:

    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
            running = False

    pygame.display.flip()