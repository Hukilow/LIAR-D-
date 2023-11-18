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
