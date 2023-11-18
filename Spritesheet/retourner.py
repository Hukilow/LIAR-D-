import os
from PIL import Image

# Chemin du dossier contenant les images
folder_path = 'Sprite'

# Liste des fichiers d'images dans le dossier (seuls les fichiers PNG et JPG sont inclus)
image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg'))]

# Ouvrir les images individuelles
images = [Image.open(image_path) for image_path in image_paths]

# Créer une nouvelle liste pour les images reflétées horizontalement
reflected_images = []

# Effectuer une réflexion horizontale sur chaque image
for image in images:
    reflected_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    reflected_images.append(reflected_image)

# Calculer la taille de la spritesheet
total_width = sum([image.width for image in reflected_images])
max_height = max([image.height for image in reflected_images])

# Créer une nouvelle image pour la spritesheet
spritesheet = Image.new('RGBA', (total_width, max_height))

# Coller les images individuelles côte à côte sur la spritesheet
x_offset = 0
for image in reflected_images:
    spritesheet.paste(image, (x_offset, 0))
    x_offset += image.width

# Enregistrez la spritesheet
spritesheet.save('spritesheet.png')
