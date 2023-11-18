import pygame

# Initialisation de Pygame
pygame.init()

# Constantes
WIN_WIDTH, WIN_HEIGHT = 800, 600
LIGHT_LAYER = 2

# Créez la fenêtre du jeu
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Effet de Lumière")

# Classe DarkScreen pour l'écran noir
class DarkScreen:
    def __init__(self):
        self.dark_mask = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.dark_mask.fill((0, 0, 0))

    def draw(self, screen):
        screen.blit(self.dark_mask, (0, 0))

# Classe Light pour la source de lumière
class Light(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, intensity):
        super().__init__(light_group)
        self._layer = LIGHT_LAYER
        self.x = x
        self.y = y
        self.light_radius = radius
        self.light_intensity = intensity
        self.light_mask = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        self.light_mask.fill((0, 0, 0, 0))
        self.image = self.light_mask
        self.rect = self.light_mask.get_rect(center=(self.x, self.y))

    def update(self):
        # Efface la lumière précédente
        self.light_mask.fill((0, 0, 0, 0))
        # Dessine un nouveau cercle de lumière
        pygame.draw.circle(self.light_mask, (255, 255, 150, self.light_intensity), (self.light_radius, self.light_radius), self.light_radius)
        self.rect = self.light_mask.get_rect(center=(self.x, self.y))

# Groupe de lumière
light_group = pygame.sprite.LayeredUpdates()

# Créez l'écran noir
dark_screen = DarkScreen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Récupérez la position du curseur de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Mettez à jour la position de la source de lumière pour suivre le curseur de la souris
    light_group.empty()  # Efface le groupe de lumière précédent
    light1 = Light(mouse_x, mouse_y, 100, 200)  # Créez la nouvelle source de lumière

    # Dessinez l'écran noir
    dark_screen.draw(screen)

    # Mettez à jour et affichez les sources de lumière
    light_group.update()
    light_group.draw(screen)

    pygame.display.flip()

pygame.quit()
