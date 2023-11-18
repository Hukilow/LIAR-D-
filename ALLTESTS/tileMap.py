"""import random

# Fonction pour générer une carte de labyrinthe
def generate_labyrinth(width, height):
    # Créer une carte remplie de murs
    tilemap = [['B' for _ in range(width)] for _ in range(height)]

    # Coordonnées de départ du joueur
    start_x, start_y = random.randint(1, width - 2), random.randint(1, height - 2)
    tilemap[start_y][start_x] = 'P'

    # Liste de directions possibles (haut, bas, gauche, droite)
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

    # Fonction pour vérifier si une cellule est valide
    def is_valid(x, y):
        return x >= 0 and y >= 0 and x < width and y < height

    # Fonction pour creuser un couloir
    def dig(x, y):
        tilemap[y][x] = '.'

    # Fonction pour effectuer une marche aléatoire
    def random_walk(x, y):
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and tilemap[ny][nx] == 'B':
                dig(nx, ny)
                dig(x + dx // 2, y + dy // 2)
                random_walk(nx, ny)

    # Commencer la marche aléatoire à partir de la position du joueur
    random_walk(start_x, start_y)

    # Créer des murs tout autour de la carte
    for x in range(width):
        tilemap[0][x] = 'B'
        tilemap[height - 1][x] = 'B'
    for y in range(height):
        tilemap[y][0] = 'B'
        tilemap[y][width - 1] = 'B'

    # Créer une sortie aléatoire (par exemple, en haut)
    exit_x = random.randint(1, width - 2)
    tilemap[0][exit_x] = '.'

    # Retourner la carte générée
    return [''.join(row) for row in tilemap]

# Exemple d'utilisation :
width = 20
height = 15
labyrinth = generate_labyrinth(width, height)
for row in labyrinth:
    print(row)"""

import random

def generate_labyrinth(width, height):
    # Crée une carte remplie de 'B' pour les murs
    tilemap = [['B' for _ in range(width)] for _ in range(height)]

    # Fonction pour vérifier si une cellule est valide
    def is_valid(x, y):
        return 1 < x < width - 1 and 1 < y < height - 1

    # Fonction pour creuser un passage de 2 de largeur
    def dig(x, y, direction):
        if direction == 'horizontal':
            tilemap[y][x - 1] = '.'
            tilemap[y][x] = '.'
            tilemap[y][x + 1] = '.'
        elif direction == 'vertical':
            tilemap[y - 1][x] = '.'
            tilemap[y][x] = '.'
            tilemap[y + 1][x] = '.'

    # Choisit un point de départ aléatoire près du bord de la carte
    start_x = random.randint(1, max(width, height) // 2) * 2
    start_y = random.randint(1, max(width, height) // 2) * 2

    # Creuse un passage depuis le point de départ
    dig(start_x, start_y, 'horizontal')

    # Liste de directions possibles (haut, bas, gauche, droite)
    directions = [(0, -2, 'vertical'), (0, 2, 'vertical'), (-2, 0, 'horizontal'), (2, 0, 'horizontal')]

    # Fonction pour effectuer une marche aléatoire
    def random_walk(x, y):
        random.shuffle(directions)
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and tilemap[ny][nx] == 'B':
                dig(nx, ny, direction)
                random_walk(nx, ny)

    # Commence la marche aléatoire à partir du point de départ
    random_walk(start_x, start_y)

    # Trouve une position pour le joueur 'P' loin de la sortie
    player_x, player_y = start_x, start_y
    while tilemap[player_y][player_x] != '.':
        player_x = random.randint(1, width - 2) * 2
        player_y = random.randint(1, height - 2) * 2

    tilemap[player_y][player_x] = 'P'

    # Retourne la carte générée
    return [''.join(row) for row in tilemap]

# Exemple d'utilisation :
width = 25
height = 25
labyrinth = generate_labyrinth(width, height)
for row in labyrinth:
    print(row)


"""import random

def generate_labyrinth(width, height):
    # Crée une carte remplie de 'B' pour les murs
    tilemap = [['B' for _ in range(width)] for _ in range(height)]

    # Fonction pour vérifier si une cellule est valide
    def is_valid(x, y):
        return x >= 0 and y >= 0 and x < width and y < height

    # Fonction pour creuser un passage de 2 de largeur
    def dig(x, y, direction):
        if direction == 'horizontal':
            for i in range(-1, 2):
                if is_valid(x + i, y):
                    tilemap[y][x + i] = '.'
        elif direction == 'vertical':
            for i in range(-1, 2):
                if is_valid(x, y + i):
                    tilemap[y + i][x] = '.'

    # Choisit un point de départ aléatoire près du bord de la carte
    start_x = random.randint(2, width // 2) * 2
    start_y = random.randint(2, height // 2) * 2

    # Creuse un passage depuis le point de départ
    dig(start_x, start_y, 'horizontal')

    # Liste de directions possibles (haut, bas, gauche, droite)
    directions = [(0, -2, 'vertical'), (0, 2, 'vertical'), (-2, 0, 'horizontal'), (2, 0, 'horizontal')]

    # Fonction pour effectuer une marche aléatoire
    def random_walk(x, y):
        random.shuffle(directions)
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and tilemap[ny][nx] == 'B':
                dig(nx, ny, direction)
                random_walk(nx, ny)

    # Commence la marche aléatoire à partir du point de départ
    random_walk(start_x, start_y)

    # Place la sortie
    exit_x, exit_y = random.randint(2, width // 2) * 2, random.randint(2, height // 2) * 2
    tilemap[exit_y][exit_x] = '.'

    # Trouve une position pour le joueur 'P' loin de la sortie
    player_x, player_y = start_x, start_y
    while tilemap[player_y][player_x] != '.':
        player_x = random.randint(2, width // 2) * 2
        player_y = random.randint(2, height // 2) * 2

    tilemap[player_y][player_x] = 'P'

    # Retourne la carte générée
    return [''.join(row) for row in tilemap]

# Exemple d'utilisation :
width = 40
height = 40
labyrinth = generate_labyrinth(width, height)
for row in labyrinth:
    print(row)"""