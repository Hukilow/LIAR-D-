import pygame
pygame.init()
HEALTH = [32,40]
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
LAYER = pygame.Surface((HEALTH[1]*10,25))
pygame.display.set_caption('grid')
running = True
def drawgrid():
    pygame.draw.rect(LAYER,"black", pygame.Rect(0,0,HEALTH[1]*10,25))
    pygame.draw.rect(LAYER,"red" ,pygame.Rect(0,0,HEALTH[0]*9,23))
while running:
    screen.fill((255,255,120))
    drawgrid()
    screen.blit(LAYER, (10,10))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()