from PIL import Image

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

# Créez un fichier texte pour enregistrer les coordonnées
with open('coordinates.txt', 'w') as file:
    # Écrivez les coordonnées pour la première spritesheet
    file.write(f'spritesheet1: x=0, y=0, width={width1}, height={height1}\n')

    # Écrivez les coordonnées pour la deuxième spritesheet
    y2 = height1
    file.write(f'spritesheet2: x=0, y={y2}, width={width2}, height={height2}\n')

    # Écrivez les coordonnées pour la troisième spritesheet
    y3 = height1 + height2
    file.write(f'spritesheet3: x=0, y={y3}, width={width3}, height={height3}\n')

    # Écrivez les coordonnées pour la quatrième spritesheet
    y4 = height1 + height2 + height3
    file.write(f'spritesheet4: x=0, y={y4}, width={width4}, height={height4}\n')

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
