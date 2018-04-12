import pygame
WHITE = (255, 255, 255)

class Projectile(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):
        siper().init()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.rect(self.image, color, [0, 0, width, height])
