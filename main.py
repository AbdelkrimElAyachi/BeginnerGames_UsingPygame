from Bird import *
import random


def resetGame():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_h/2)
    flappy.gameOver = False
    flappy.vel = 0
    note = 0

# loading pygame modules
initialize()
# declaring the principale variables in our game  
pipe_speed = 4
fps = 60
screen_wd = 864 #864
screen_h = 936
last_pipe = pygame.time.get_ticks()
note = 0
hole = 100


# setting up frames
clock = pygame.time.Clock()

# loading images for background and the ground
bg = pygame.image.load("assets/bg.png")
ground = pygame.image.load("assets/ground.png")


# setting up the window 
surface = pygame.display.set_mode((screen_wd,screen_h),pygame.RESIZABLE)
pygame.display.set_caption("flappy bird")
Icon = pygame.image.load("assets/logo2.png")
pygame.display.set_icon(Icon)



# creating rect
ground_scroll = 0
scroll_speed = 4



# initializing sprites for the bird and the pipes  
pipe_group , bird_group= pygame.sprite.Group(),pygame.sprite.Group() 
flappy = Bird(100,int(936/2))
bird_group.add(flappy)
pipe_group.add(Pipe(random.randint(300,600),random.randint(220,550),True,pipe_speed))

# create my restart button
btn  = Button(screen_wd//2,screen_h//2)

running = True
while running:


    # frames pe defautl fps = 60 
    clock.tick(fps)
 
    #  adding background
    surface.blit(bg,(0,0)) 

    # check for collision
    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False):
        flappy.gameOver = True 
    # drawing pipes 
    pipe_group.draw(surface)

    if not flappy.gameOver:
        
        # update pipes and the bird
        pipe_group.update()

        # creating pipes
        if (pygame.time.get_ticks() - last_pipe ) > 1500 :
            num = random.randint(100,500)
            pipe_group.add(Pipe(900,num-hole ,True,pipe_speed))
            pipe_group.add(Pipe(900,num+hole ,False,pipe_speed))
            last_pipe = pygame.time.get_ticks() 
            note += 1
            hole -= 0.5
            print(note)

        # animation ground
        surface.blit(ground,(ground_scroll,768))
        ground_scroll -= scroll_speed

    # plyaer
    bird_group.draw(surface)
    bird_group.update()

    if (ground_scroll<-35):
        ground_scroll = 0

    if flappy.gameOver :
        if btn.draw(surface):
            resetGame()
            print("clicked")


    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE and not flappy.gameOver:
                flappy.jump()
       
    pygame.display.flip()



