from PIL import Image
import os

# Dossier contenant les images
input_folder = 'Input/'

# Dossier de sortie pour les images redimensionnées
output_folder = 'Sprite/'

# Dimensions souhaitées pour les images redimensionnées
new_width = 210
new_height = 64

# Liste des fichiers d'images dans le dossier
image_files = [file for file in os.listdir(input_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

# Créez le dossier de sortie s'il n'existe pas
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Parcourez chaque image et redimensionnez-la
for image_file in image_files:
    try:
        with Image.open(os.path.join(input_folder, image_file)) as img:
            # Redimensionnez l'image aux dimensions souhaitées
            resized_img = img.resize((new_width, new_height))
            
            # Enregistrez l'image redimensionnée dans le dossier de sortie
            output_path = os.path.join(output_folder, image_file)
            resized_img.save(output_path)
            print(f"Redimension de {image_file} terminée.")
    except Exception as e:
        print(f"Erreur lors de la redimension de {image_file}: {str(e)}")

print("Toutes les images ont été redimensionnées.")
