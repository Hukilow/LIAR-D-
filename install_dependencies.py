import subprocess
from pkg_resources import parse_version

def verify_requirements():
    try:
        with open('requirements.txt', 'r') as file:
            required_libraries = [line.strip() for line in file.readlines()]

        installed_libraries = subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')
        installed_libraries = [lib.split('==')[0].lower() for lib in installed_libraries if lib]

        missing_libraries = []
        for lib in required_libraries:
            lib_parts = lib.split('==')
            lib_name = lib_parts[0].lower()
            lib_version = lib_parts[1] if len(lib_parts) == 2 else None


            if lib_name not in installed_libraries:
                missing_libraries.append(lib)

        if missing_libraries:
            print("Bibliothèques manquantes détectées. Installation en cours...")
            for library in missing_libraries:
                subprocess.run(['pip', 'install', library])
            print("Installation terminée.")
        else:
            print("Toutes les bibliothèques nécessaires sont déjà installées.")

    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
