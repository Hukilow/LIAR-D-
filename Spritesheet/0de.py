import os
from PIL import Image

# Chemin du dossier contenant les images
folder_path = 'Sprite'

# Liste des fichiers d'images dans le dossier
image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

# Ouvrir les images individuelles
images = [Image.open(image_path) for image_path in image_paths]

# Créer une nouvelle image pour la spritesheet
total_width = sum([image.width for image in images])
max_height = max([image.height for image in images])
spritesheet = Image.new('RGBA', (total_width, max_height))

# Liste pour stocker les coordonnées de chaque image
image_coordinates = []

# Coordonnées x et y initiales
x, y = 0, 0

# Parcourez chaque image
for image in images:
    width, height = image.size
    spritesheet.paste(image, (x, y))
    image_coordinates.append((x, y, width, height))
    x += width  # Incrémentez la coordonnée x pour la prochaine image

# Enregistrez la spritesheet
spritesheet.save('spritesheet.png')

# Enregistrez les coordonnées dans un fichier texte
with open('image_coordinates.txt', 'w') as file:
    for i, (x, y, width, height) in enumerate(image_coordinates):
        file.write(f"self.image_{i} = [self.game.attackscythe_spritesheet.get_sprite({x}, {y}, {width}, {height}),]\n")

