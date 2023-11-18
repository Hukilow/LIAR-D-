import os
from PIL import Image

# Chemin du dossier contenant les images
folder_path = 'Sprite'

# Liste des fichiers d'images dans le dossier (seuls les fichiers PNG et JPG sont inclus)
image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg'))]

# Ouvrir les images individuelles
images = [Image.open(image_path) for image_path in image_paths]

# Créer une nouvelle liste pour les images rotatées de 270 degrés
rotated_images = []

# Effectuer une rotation de 270 degrés (ou -90 degrés) sur chaque image
for image in images:
    rotated_image = image.transpose(Image.ROTATE_90)
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
spritesheet.save('spritesheet4.png')
