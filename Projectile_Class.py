import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Projectile(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.ellipse(self.image, color, [0, 0, width, height], 0)
        pygame.draw.ellipse(self.image, BLACK,[10, 10, width-40, height-40], 0)
        pygame.draw.ellipse(self.image, BLACK,[30, 10, width-40, height-40], 0)
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
