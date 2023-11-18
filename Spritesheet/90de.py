import os
from PIL import Image

# Chemin du dossier contenant les images
folder_path = 'Sprite'

# Liste des fichiers d'images dans le dossier (seuls les fichiers PNG et JPG sont inclus)
image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg'))]

# Ouvrir les images individuelles
images = [Image.open(image_path) for image_path in image_paths]

# Créer une nouvelle liste pour les images rotatées
rotated_images = []

# Effectuer une rotation de 90 degrés sur chaque image
for image in images:
    rotated_image = image.transpose(Image.ROTATE_270)
    rotated_images.append(rotated_image)

# Calculer la taille de la spritesheet
total_width = sum([image.width for image in rotated_images])
max_height = max([image.height for image in rotated_images])

# Créer une nouvelle image pour la spritesheet
spritesheet = Image.new('RGBA', (total_width, max_height))

# Coller les images individuelles côte à côte sur la spritesheet
x_offset = 0
for image in rotated_images:
    spritesheet.paste(image, (x_offset, 0))
    x_offset += image.width

# Enregistrez la spritesheet
spritesheet.save('spritesheet1.png')

# Liste pour stocker les coordonnées de chaque image
image_coordinates = []

# Coordonnées x et y initiales
x, y = 0, 0

# Parcourir chaque image
for rotated_image in rotated_images:
    width, height = rotated_image.size
    image_coordinates.append((x, y, width, height))
    x += width  # Incrémentez la coordonnée x pour la prochaine image

# Enregistrez les coordonnées dans un fichier texte
with open('image_coordinates.txt2', 'w') as file:
    for i, (x, y, width, height) in enumerate(image_coordinates):
        file.write(f"self.image_{i} = [self.game.attackscythe_spritesheet.get_sprite({x}, {y}, {width}, {height}),]\n")