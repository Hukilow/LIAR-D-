def multiple_of_32(num):
    reste = num % 32
    num = num-reste

    return num

# Exemple d'utilisation
nombre_donne = 1435
resultat = multiple_of_32(nombre_donne)
print(resultat)