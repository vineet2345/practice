import pygame
import math

pygame.init()

''' Variables '''
run = True
fps = 40
ani = 4


''' Setup '''

clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode((800, 500))
backdrop = pygame.image.load("bg.png")
pygame.display.set_caption("Simple Game")


class Player(object):
    def __init__(self,x,y,width,height,color='red'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.isJump = False
        self.jumpCount = -10

player = Player(700,400,30,50,"red")

def draw(player):
    rect = ((player.x, player.y), (player.width, player.height))
    pygame.draw.rect(world, player.color, rect )

    pygame.display.update()

def controls(player):
    velocity = 3

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False


    key = pygame.key.get_pressed()
    
    if (key[pygame.K_w] or key[pygame.K_SPACE]) and not player.isJump:
        player.isJump = True
        player.y -= player.jumpCount * velocity
        player.jumpCount += 1
        

        

    if key[pygame.K_a] and player.x > 15:
        player.x -= velocity
    if key[pygame.K_d] and player.x < 755:
        player.x += velocity

while run:
    draw(player)
    controls(player)
    
    pygame.display.update()
    world.fill((0, 0, 0))
