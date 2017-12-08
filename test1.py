import pygame

pygame.init()

height = 600
width = 800
score = 0

#Display information
white = (255,255,255)
screen = pygame.display.set_mode((width, height))

catSprite = pygame.image.load('cat11.png')
mouseSprite = pygame.image.load('mouse11.png')
deadMouse = pygame.image.load('dead.png')
#font = pygame.font.Font(None, 40)
#scoretext = font.render("Score = "+ str(score), 1, (0,0,0))

#catSprite Information
catx = 0
caty = 0

xChange = 0
yChange = 0

catHeight = 36
catWidth = 128

#mouseSprite Information
mousex = 200
mousey = 200

mouseWidth = 40
mouseHeight = 24


clock = pygame.time.Clock()

def mouse(mousex, mousey):
    screen.blit(mouseSprite,(mousex, mousey))
    

def cat(catx,caty):
    screen.blit(catSprite, (catx,caty))

def detect(x1, y1, w1, h1, x2, y2, w2, h2):
    if(x2+w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):
        print("collide 1")
        return True
    elif(x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):
        print("collide 2")
        return True
    elif(x2+w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
        print("collide 3")
        return True
    elif(x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
        print("collide 4")
        return True
    else:
        return False
    

#Main Game Loop
keepGoing = True
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                catSprite = pygame.image.load('catLeft.png')
                xChange = -5
            elif event.key == pygame.K_RIGHT:
                catSprite = pygame.image.load('cat11.png')
                xChange = 5
            elif event.key == pygame.K_UP:
                catSprite = pygame.image.load('catUp.png')
                yChange = -5
            elif event.key == pygame.K_DOWN:
                catSprite = pygame.image.load('catDown.png')
                yChange = 5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                xChange = 0
                yChange = 0
    catx += xChange
    caty += yChange
    
    screen.fill(white)
    cat(catx,caty)
    mouse(mousex, mousey)

    #Setting Boundaries
    if catx > width - catWidth or catx < 0:
        xChange = 0
    if caty > height - catHeight or caty < 0:
        yChange = 0

    #Collision Dectection
    collision = detect(catx, caty, catWidth, catHeight, mousex, mousey, mouseWidth, mouseHeight)

    if collision == True:
        score = score + 1
        screen.blit(deadMouse,(mousex, mousey))
        
    font = pygame.font.Font(None, 40)
    scoretext = font.render("Score = "+ str(score), 1, (0,0,0))
    screen.blit(scoretext, (5, 10))
    
    

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
quit()

        
