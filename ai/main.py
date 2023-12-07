import pygame,random

rectangles = []

def createRect(x,y,size):
    rect = (pygame.Rect(x,y,size,size))
    rectangles.append(rect)

def updateRectangles():
    for rect in rectangles:
        pygame.draw.rect(screen,(0,255,0),rect)


(numsuccess,numfails) = pygame.init()
if(numfails>0):
    print(f"there is {numfails} modules that failed")
    exit("error : in loading pygame modules")

# settings of our game
width_sc = 800
height_sc =  800
score = 0
x_p = 0
y_p = 0
size = 100

screen = pygame.display.set_mode((width_sc,height_sc))
pygame.display.set_caption("our ai")


player = pygame.Rect(x_p,y_p,size,size)

for i in range(10):
    createRect(random.randint(0,500),random.randint(0,500),random.randint(30,50))

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Check arrow key presses to update player position
            if event.key == pygame.K_LEFT:
                player.x -= 10
            elif event.key == pygame.K_RIGHT:
                player.x += 10
            elif event.key == pygame.K_UP:
                player.y -= 10
            elif event.key == pygame.K_DOWN:
                player.y += 10   

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(0,0,255),player)
    updateRectangles()

    pygame.display.flip()        


pygame.quit()    