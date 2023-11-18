import pygame
import sys
import math

DIMENSIONS = (1600, 900)
window = pygame.display.set_mode(DIMENSIONS, pygame.RESIZABLE)
window.fill((20, 20, 20))
pygame.display.set_caption("Pygame template")
clock = pygame.time.Clock()


looking_vector = pygame.Vector2(1,1)

while True:

    window.fill((20,20,20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    CENTER = (DIMENSIONS[0]/2, DIMENSIONS[1]/2)
    CENTER = pygame.Vector2(CENTER)

    # Relative position of mouse
    mouse_pos = pygame.mouse.get_pos()
    delta = mouse_pos - CENTER
    
    # Calculate the angle 
    angle_to_mouse = math.atan2(delta.y, delta.x)
    looking_vector.xy = (100*math.cos(angle_to_mouse), 100*math.sin(angle_to_mouse))
    
    # Line in direction to looking_vector
    pygame.draw.line(window, (50,255,50), CENTER, CENTER + looking_vector)

    print(looking_vector)

    pygame.display.update()
    clock.tick(60)

