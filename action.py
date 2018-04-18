# ICS3U
# Assignment 2: Action
# <Farhan Mahamud>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from Projectile_Class import Projectile
pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (243, 247, 0)
LIGHTBLUE = (166, 249, 252)
YELLOW = (249, 255, 91)
PURPLE = (50, 0, 153)

speed = 1
colorList = (WHITE, RED, BLUE, GREEN, LIGHTBLUE, YELLOW, PURPLE)
background = pygame.image.load('grass.png')

# Set the screen size
SCREENWIDTH = 561
SCREENHEIGHT = 378

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

all_sprites_lists = pygame.sprite.Group()

projectile1 = Projectile(LIGHTBLUE, 50, 50, random.randint(50,100))
projectile1.rect.x = 0
projectile1.rect.y = 40

projectile2 = Projectile(YELLOW, 50, 50,random.randint(50,100))
projectile2.rect.x = 0
projectile2.rect.y = 80

projectile3 = Projectile(PURPLE, 50, 50,random.randint(50,100))
projectile3.rect.x = 0
projectile3.rect.y = 120

projectile4 = Projectile(GREEN, 50, 50,random.randint(50,100))
projectile4.rect.x = 0
projectile4.rect.y = 160

projectile5 = Projectile(RED, 50, 50,random.randint(50,100))
projectile5.rect.x = 0
projectile5.rect.y = 200

projectile6 = Projectile(BLUE, 50, 50,random.randint(50,100))
projectile6.rect.x = 0
projectile6.rect.y = 240

all_sprites_lists.add(projectile1)
all_sprites_lists.add(projectile2)
all_sprites_lists.add(projectile3)
all_sprites_lists.add(projectile4)
all_sprites_lists.add(projectile5)
all_sprites_lists.add(projectile6)

all_moving_projectile = pygame.sprite.Group()
all_moving_projectile.add(projectile1)
all_moving_projectile.add(projectile2)
all_moving_projectile.add(projectile3)
all_moving_projectile.add(projectile4)
all_moving_projectile.add(projectile5)
all_moving_projectile.add(projectile6)

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
            
    projectile1.moveRight(speed)
    projectile1.rect.x += 1
    if projectile1.rect.x > SCREENWIDTH:
        projectile1.changeSpeed(random.randint(0, 0))
        #projectile1.repaint(random.choice(colorList))
        projectile1.rect.x = 0

    projectile2.moveRight(speed)
    projectile2.rect.x += 2
    if projectile2.rect.x > SCREENWIDTH:
        projectile2.changeSpeed(random.randint(0, 0))
        #projectile2.repaint(random.choice(colorList))
        projectile2.rect.x = 0

    projectile3.moveRight(speed)
    projectile3.rect.x += 3
    if projectile3.rect.x > SCREENWIDTH:
        projectile3.changeSpeed(random.randint(0, 0))
        #projectile3.repaint(random.choice(colorList))
        projectile3.rect.x = 0

    projectile4.moveRight(speed)
    projectile4.rect.x += 4
    if projectile4.rect.x > SCREENWIDTH:
        projectile4.changeSpeed(random.randint(0, 0))
        #projectile4.repaint(random.choice(colorList))
        projectile4.rect.x = 0

    projectile5.moveRight(speed)
    projectile5.rect.x += 5
    if projectile5.rect.x > SCREENWIDTH:
        projectile5.changeSpeed(random.randint(0, 0))
        #projectile5.repaint(random.choice(colorList))
        projectile5.rect.x = 0

    projectile6.moveRight(speed)
    projectile6.rect.x += 6
    if projectile6.rect.x > SCREENWIDTH:
        projectile6.changeSpeed(random.randint(0, 0))
        #projectile6.repaint(random.choice(colorList))
        projectile6.rect.x = 0
        
    # --- Game logic goes here
    # There should be none for a static image

    # --- Draw code goes here
    
    # Clear the screen to white
    screen.fill(BLACK)
    screen.blit(background, (0, 0))

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    all_sprites_lists.draw(screen)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
