# ICS3U
# Assignment 2: Action
# <your name>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from Projectile_Class import Projectile
pygame.init()

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

colorList = (BLACK, WHITE, GREEN, RED, BLUE, LIGHTBLUE, YELLOW, PURPLE)

# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

all_sprites_lists = pygame.sprite.Group()

projectile1 = Projectile(LIGHTBLUE, 50, 50,random.randint(50,100))
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
projectile6.rect.y = 200

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

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
