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
spritesheet.save('spritesheet1.png')





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
spritesheet.save('spritesheet2.png')

# Liste pour stocker les coordonnées de chaque image
image_coordinates = []


# Créer une nouvelle liste pour les images rotatées de 180 degrés
rotated_images = []

# Effectuer une rotation de 180 degrés sur chaque image
for image in images:
    rotated_image = image.rotate(180)
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
spritesheet.save('spritesheet3.png')

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

# Chargez vos 4 spritesheets différentes (remplacez les chemins par les vôtres)
spritesheet1 = Image.open('spritesheet1.png')
spritesheet2 = Image.open('spritesheet2.png')
spritesheet3 = Image.open('spritesheet3.png')
spritesheet4 = Image.open('spritesheet4.png')

# Obtenez les dimensions de chaque spritesheet
width1, height1 = spritesheet1.size
width2, height2 = spritesheet2.size
width3, height3 = spritesheet3.size
width4, height4 = spritesheet4.size

# Calculez la largeur et la hauteur totales de la spritesheet finale
total_width = max(width1, width2, width3, width4)
total_height = height1 + height2 + height3 + height4

# Créez une nouvelle spritesheet vide
final_spritesheet = Image.new('RGBA', (total_width, total_height), (0, 0, 0, 0))

# Collez chaque spritesheet individuelle dans la spritesheet finale
final_spritesheet.paste(spritesheet1, (0, 0))
final_spritesheet.paste(spritesheet2, (0, height1))
final_spritesheet.paste(spritesheet3, (0, height1 + height2))
final_spritesheet.paste(spritesheet4, (0, height1 + height2 + height3))

# Enregistrez la spritesheet finale
final_spritesheet.save('spritesheet_final.png')


nombreimage = int(input("Combien d'images ? : "))
width = int(input("Largeur de l'image : "))
height = int(input("Hauteur de l'image : "))
nomspritesheet = input("Nom de la spritesheet : ")


with open('coordinates.txt', 'w') as file:
    for i in range(nombreimage):
        if i == 0 : 
            file.write(f'self.right_attacksanimation = [')
        if i == nombreimage-1:
            file.write(f'self.game.{nomspritesheet}_spritesheet.get_sprite({width*i}, {0}, {width}, {height}),]\n\n')
            break
        file.write(f'self.game.{nomspritesheet}_spritesheet.get_sprite({width*i}, {0}, {width}, {height}),\n')

        
    for i in range(nombreimage):
        if i == 0:
            file.write(f'self.down_attacksanimation = [')
        if i == nombreimage-1:
            file.write(f'self.game.{nomspritesheet}_spritesheet.get_sprite({height*i}, {height}, {height}, {width}),]\n\n')    
            break
        file.write(f'self.game.{nomspritesheet}_spritesheet.get_sprite({height*i}, {height}, {height}, {width}),\n')


    for i in range(nombreimage):
        if i == 0:
            file.write(f'self.left_attacksanimation = [')
        if i == nombreimage-1:
            file.write(f'self.game.{nomspritesheet}_spritesheet.get_sprite({width*i}, {width+height}, {width}, {height}),]\n\n')
            break
        file.write(f'self.game.{nomspritesheet}_spritesheet.get_sprite({width*i}, {width+height}, {width}, {height}),\n')


    for i in range(nombreimage):
        if i == 0:
            file.write(f'self.up_attacksanimation = [')
        if i == nombreimage-1:
            file.write(f'self.game.{nomspritesheet}_spritesheet.get_sprite({height*i}, {width+height+height}, {height}, {width}),]\n\n')
            break
        file.write(f'self.game.{nomspritesheet}_spritesheet.get_sprite({height*i}, {width+height+height}, {height}, {width}),\n')


