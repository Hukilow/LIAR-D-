import os

# Dossier 1 : Spécifiez le chemin du premier dossier que vous souhaitez vider
dossier_1 = 'Input/'

# Dossier 2 : Spécifiez le chemin du deuxième dossier que vous souhaitez vider
dossier_2 = 'Sprite/'

# Supprimer tous les fichiers dans le dossier 1
for fichier in os.listdir(dossier_1):
    chemin_fichier = os.path.join(dossier_1, fichier)
    if os.path.isfile(chemin_fichier):
        os.remove(chemin_fichier)

# Supprimer tous les fichiers dans le dossier 2
for fichier in os.listdir(dossier_2):
    chemin_fichier = os.path.join(dossier_2, fichier)
    if os.path.isfile(chemin_fichier):
        os.remove(chemin_fichier)

# Supprimer 3 fichiers .txt dans le dossier courant
for fichier in os.listdir('.'):
    if fichier.endswith('.txt'):
        os.remove(fichier)

# Supprimer 5 fichiers .png dans le dossier courant
for fichier in os.listdir('.'):
    if fichier.endswith('.png'):
        os.remove(fichier)

print("Opérations de suppression terminées.")
