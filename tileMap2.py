import random
from mazegenerator import*
from allroom import*



def generate_labyrinth(width, height,):
    def transformer(width,height):
        py = Maze(width,height)
        dino = py.gen_maze_2D()
        tilemap = []
        for miniliste in dino:
            listeinf = []
            listeinfinf = []
            for case in miniliste:
                if case == 1:
                    listeinf.append('B')
                    listeinf.append('G')
                    listeinfinf.append('G')
                    listeinfinf.append('G')
                if case == 0:
                    listeinf.append('.')
                    listeinf.append('I')
                    listeinfinf.append('I')
                    listeinfinf.append('I')
            for i in range(len(listeinf)):
                if listeinf[i] == 'G':
                    listeinf[i] = 'B'
                if listeinf[i] == 'I':
                    listeinf[i] = '.'
            for i in range(len(listeinfinf)):
                if listeinfinf[i] == 'G':
                    listeinfinf[i] = 'B'
                if listeinfinf[i] == 'I':
                    listeinfinf[i] = '.'

            tilemap.append(listeinf)
            tilemap.append(listeinfinf)
        return tilemap
    
    def creer_salle(salle,tilemap,a):
        if a == 1:
            x = 1
            y = 1
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 2:
            x = len(tilemap)-12
            y = 1
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 3:
            x = 1
            y = len(tilemap)-12
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 4:
            x = len(tilemap)-12
            y = len(tilemap)-12
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        return tilemap
    
    # Crée un spawn au centre de la map
    def spawn(tilemap):
        Moitié = len(tilemap)//2
        for i in range(Moitié-2,Moitié+3):
            tilemap[Moitié-2][i] = "."
            tilemap[Moitié-1][i] = "."
            tilemap[Moitié+1][i] = "."
            tilemap[Moitié+2][i] = "."
        for i in range(Moitié-2,Moitié+3):
            tilemap[Moitié][i] = "."
        tilemap[Moitié][Moitié] = "P"
        return tilemap
    
    
    def spawnentites(tilemap):
        a = 1
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == '.':
                    b = random.randint(1,100)
                    if a == b:
                        tilemap[i][j] = "E"
                if column == '.':
                    b = random.randint(1,150)
                    if a == b:
                        tilemap[i][j] = "C"
        return tilemap
    tilemap = transformer(width,height)
    tilemap = spawnentites(tilemap)
    a = [1,2,3,4]
    c = random.choice(a)
    a.remove(c)
    tilemap = creer_salle(echelle_descendre, tilemap, c)
    b = liste_ps.copy()
    for i in range(0,3):
        d = random.choice(b)
        b.remove(d)
        c = random.choice(a)
        a.remove(c)
        tilemap = creer_salle(d, tilemap, c)
    tilemap = spawn(tilemap)
    return tilemap

def generate_labyrinth2(width, height, nombre_determinant_lettre):
    def transformer(width,height):
        py = Maze(width,height)
        dino = py.gen_maze_2D()
        tilemap = []
        for miniliste in dino:
            listeinf = []
            listeinfinf = []
            for case in miniliste:
                if case == 1:
                    listeinf.append('B')
                    listeinf.append('G')
                    listeinfinf.append('G')
                    listeinfinf.append('G')
                if case == 0:
                    listeinf.append('.')
                    listeinf.append('I')
                    listeinfinf.append('I')
                    listeinfinf.append('I')
            for i in range(len(listeinf)):
                if listeinf[i] == 'G':
                    listeinf[i] = 'B'
                if listeinf[i] == 'I':
                    listeinf[i] = '.'
            for i in range(len(listeinfinf)):
                if listeinfinf[i] == 'G':
                    listeinfinf[i] = 'B'
                if listeinfinf[i] == 'I':
                    listeinfinf[i] = '.'
            tilemap.append(listeinf)
            tilemap.append(listeinfinf)
        return tilemap
    
    def creer_salle(salle,tilemap,a):
        if a == 1:
            x = 1
            y = 1
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 2:
            x = len(tilemap)-12
            y = 1
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 3:
            x = 1
            y = len(tilemap)-12
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 4:
            x = len(tilemap)-12
            y = len(tilemap)-12
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        return tilemap
    
    def spawnentites(tilemap):
        a = random.randint(1,50)
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == '.':
                    b = random.randint(1,90)
                    if a == b:
                        tilemap[i][j] = "E"
                if column == '.':
                    b = random.randint(1,150)
                    if a == b:
                        tilemap[i][j] = "C"

        return tilemap
    
    def creer_salle_principale(salle,tilemap):
        x = round((len(tilemap)/2)-13)
        y = round((len(tilemap)/2)-13)
        for i in range(0,len(salle)):
            for k in range(0,len(salle[i])):
                tilemap[i+y][k+x] = salle[i][k]
    
    tilemap = transformer(width,height)
    tilemap = spawnentites(tilemap)
    a = [1,2,3,4]
    c = random.choice(a)
    a.remove(c)
    tilemap = creer_salle(echelle_descendre, tilemap, c)
    c = random.choice(a)
    a.remove(c)
    tilemap = creer_salle(echelle_monter, tilemap, c)
    g = liste_ps.copy()
    listy = liste_gs.copy()
    for i in range(0,2):
        f = random.choice(g)
        g.remove(f)
        c = random.choice(a)
        a.remove(c)
        tilemap = creer_salle(f, tilemap, c)
    if nombre_determinant_lettre == 100:
        d = liste_lettre[0]
        liste_lettre.remove(d)
    else:
        d = random.choice(listy)
        listy.remove(d)
    creer_salle_principale(d,tilemap)
    return tilemap

def generate_labyrinth5(width, height, nombre_determinant_lettre):
    def transformer(width,height):
        py = Maze(width,height)
        dino = py.gen_maze_2D()
        tilemap = []
        for miniliste in dino:
            listeinf = []
            listeinfinf = []
            for case in miniliste:
                if case == 1:
                    listeinf.append('B')
                    listeinf.append('G')
                    listeinfinf.append('G')
                    listeinfinf.append('G')
                if case == 0:
                    listeinf.append('.')
                    listeinf.append('I')
                    listeinfinf.append('I')
                    listeinfinf.append('I')
            for i in range(len(listeinf)):
                if listeinf[i] == 'G':
                    listeinf[i] = 'B'
                if listeinf[i] == 'I':
                    listeinf[i] = '.'
            for i in range(len(listeinfinf)):
                if listeinfinf[i] == 'G':
                    listeinfinf[i] = 'B'
                if listeinfinf[i] == 'I':
                    listeinfinf[i] = '.'
            tilemap.append(listeinf)
            tilemap.append(listeinfinf)
        return tilemap
    
    def creer_salle(salle,tilemap,a):
        if a == 1:
            x = 1
            y = 1
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 2:
            x = len(tilemap)-12
            y = 1
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 3:
            x = 1
            y = len(tilemap)-12
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        if a == 4:
            x = len(tilemap)-12
            y = len(tilemap)-12
            for i in range(0,len(salle)):
                for k in range(0,len(salle[i])):
                    tilemap[i+y][k+x] = salle[i][k]
        return tilemap
    
    def spawnentites(tilemap):
        a = random.randint(1,50)
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == '.':
                    b = random.randint(1,75)
                    if a == b:
                        tilemap[i][j] = "E"
                if column == '.':
                    b = random.randint(1,150)
                    if a == b:
                        tilemap[i][j] = "C"
        return tilemap
    
    def creer_salle_principale(salle,tilemap):
        x = round((len(tilemap)/2)-13)
        y = round((len(tilemap)/2)-13)
        for i in range(0,len(salle)):
            for k in range(0,len(salle[i])):
                tilemap[i+y][k+x] = salle[i][k]
    
    tilemap = transformer(width,height)
    tilemap = spawnentites(tilemap)
    a = [1,2,3,4]
    c = random.choice(a)
    a.remove(c)
    tilemap = creer_salle(echelle_monter, tilemap, c)
    g = liste_ps.copy()
    for i in range(0,3):
        f = random.choice(g)
        g.remove(f)
        c = random.choice(a)
        a.remove(c)
        tilemap = creer_salle(f, tilemap, c)
    if nombre_determinant_lettre == 100:
        d = gs_D
    else:
        d = salle_entrée_boss
    creer_salle_principale(d,tilemap)
    return tilemap

"""def createTilemap(self,tilemap):
        a = random.randint(1,50)
        m = random.randint(1,50)
        p = random.randint(1,50)
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == '.':
                    b = random.randint(1,50)
                    if a == b:
                        Enemy(self, j, i)
                if column == '.':
                    b = random.randint(1,75)
                    if a == b:
                        Coffre(self, j, i)
                if column == '.':
                    l = random.randint(1,100)
                    if m == l:
                        EchelleHaut(self, j, i)
                        m = 900
                if column == '.':
                    e = random.randint(1,100)
                    if p == e:
                        EchelleBas(self, j, i)
                        p = 900"""

def spawncoffres(tilemap):
    c = ['1','2','3','4','5','6','7','8','9']
    for i, row in enumerate(tilemap[1]):
        for j, column in enumerate(row):
            if column == 'C':
                if tilemap[0] == 'tilemap1':
                    a = random.randint(1,1000)
                    if 1 <= a < 600:
                        tilemap[1][i][j] = '1'
                    if 600 <= a < 805:
                        tilemap[1][i][j] = '2'
                    if 805 <= a < 929:
                        tilemap[1][i][j] = '3'
                    if 929 <= a < 979:
                        tilemap[1][i][j] = '4'
                    if 979 <= a < 999:
                        tilemap[1][i][j] = '5'
                    if a == 1000:
                        tilemap[1][i][j] = '6'
                    
                if tilemap[0] == 'tilemap2':
                    a = random.randint(1,1000)
                    if 1 <= a < 500:
                        tilemap[1][i][j] = '1'
                    if 500 <= a < 755:
                        tilemap[1][i][j] = '2'
                    if 755 <= a < 909:
                        tilemap[1][i][j] = '3'
                    if 909 <= a < 969:
                        tilemap[1][i][j] = '4'
                    if 969 <= a < 999:
                        tilemap[1][i][j] = '5'
                    if a == 1000:
                        tilemap[1][i][j] = '6'
                        
                if tilemap[0] == 'tilemap3':
                    a = random.randint(1,1000)
                    if 1 <= a < 400:
                        tilemap[1][i][j] = '1'
                    if 400 <= a < 685:
                        tilemap[1][i][j] = '2'
                    if 685 <= a < 889:
                        tilemap[1][i][j] = '3'
                    if 889 <= a < 959:
                        tilemap[1][i][j] = '4'
                    if 959 <= a < 999:
                        tilemap[1][i][j] = '5'
                    if a == 1000:
                        tilemap[1][i][j] = '6'

                if tilemap[0] == 'tilemap4':
                    a = random.randint(1,1000)
                    if 1 <= a < 300:
                        tilemap[1][i][j] = '1'
                    if 300 <= a < 565:
                        tilemap[1][i][j] = '2'
                    if 565 <= a < 869:
                        tilemap[1][i][j] = '3'
                    if 869 <= a < 949:
                        tilemap[1][i][j] = '4'
                    if 949 <= a < 999:
                        tilemap[1][i][j] = '5'
                    if a == 1000:
                        tilemap[1][i][j] = '6'
                        
                if tilemap[0] == 'tilemap5':
                    a = random.randint(1,1000)
                    if 1 <= a < 200:
                        tilemap[1][i][j] = '1'
                    if 200 <= a < 405:
                        tilemap[1][i][j] = '2'
                    if 405 <= a < 759:
                        tilemap[1][i][j] = '3'
                    if 759 <= a < 909:
                        tilemap[1][i][j] = '4'
                    if 909 <= a < 999:
                        tilemap[1][i][j] = '5'
                    if a == 1000:
                        tilemap[1][i][j] = '6'

                if tilemap[0] == 'tilemap6':
                    a = random.randint(1,1000)
                    if 1 <= a < 100:
                        tilemap[1][i][j] = '1'
                    if 100 <= a < 300:
                        tilemap[1][i][j] = '2'
                    if 300 <= a < 620:
                        tilemap[1][i][j] = '3'
                    if 620 <= a < 840:
                        tilemap[1][i][j] = '4'
                    if 840 <= a < 990:
                        tilemap[1][i][j] = '5'
                    if 990 <= a <= 1000:
                        tilemap[1][i][j] = '6'
                        
            if column == 'H':
                a = random.randint(1,100)
                if 1 <= a < 70:
                    tilemap[1][i][j] = '7'
                if 70 <= a < 90:
                    tilemap[1][i][j] = '8'
                if 90 <= a <= 100:
                    tilemap[1][i][j] = '9'
    return tilemap

def spawnennemis(tilemap):
    e = ['V','S','F','W','Z','A','U','K','R']
    b = random.randint(1,1000)
    for i, row in enumerate(tilemap[1]):
        for j, column in enumerate(row):
            if column == 'E':

                if tilemap[0] == 'tilemap1':
                    a = random.randint(1,1000)
                    if 1 <= a < 50:
                        tilemap[1][i][j] = 'V'
                    if 51 <= a < 250:
                        tilemap[1][i][j] = 'S'
                    if 251 <= a < 450:
                        tilemap[1][i][j] = 'Z'
                    if 451 <= a < 650:
                        tilemap[1][i][j] = 'W'
                    if 651 <= a < 800:
                        tilemap[1][i][j] = 'K'
                    if 801 <= a < 900:
                        tilemap[1][i][j] = 'U'
                    if 901 <= a < 955:
                        tilemap[1][i][j] = 'R'
                    if 956 <= a < 980:
                        tilemap[1][i][j] = 'A'
                    if 981 <= a <= 1000:
                        tilemap[1][i][j] = 'F'
                    
                if tilemap[0] == 'tilemap2':
                    a = random.randint(1,1000)
                    if 1 <= a < 50:
                        tilemap[1][i][j] = 'V'
                    if 51 <= a < 250:
                        tilemap[1][i][j] = 'S'
                    if 251 <= a < 450:
                        tilemap[1][i][j] = 'Z'
                    if 451 <= a < 650:
                        tilemap[1][i][j] = 'W'
                    if 651 <= a < 800:
                        tilemap[1][i][j] = 'K'
                    if 801 <= a < 900:
                        tilemap[1][i][j] = 'U'
                    if 901 <= a < 950:
                        tilemap[1][i][j] = 'R'
                    if 951 <= a < 976:
                        tilemap[1][i][j] = 'A'
                    if 976 <= a <= 1000:
                        tilemap[1][i][j] = 'F'
                        
                if tilemap[0] == 'tilemap3':
                    a = random.randint(1,1000)
                    if 1 <= a < 35:
                        tilemap[1][i][j] = 'V'
                    if 35 <= a < 200:
                        tilemap[1][i][j] = 'S'
                    if 200 <= a < 325:
                        tilemap[1][i][j] = 'Z'
                    if 325 <= a < 525:
                        tilemap[1][i][j] = 'W'
                    if 525 <= a < 725:
                        tilemap[1][i][j] = 'K'
                    if 725 <= a < 850:
                        tilemap[1][i][j] = 'U'
                    if 850 <= a < 935:
                        tilemap[1][i][j] = 'R'
                    if 935 <= a < 965:
                        tilemap[1][i][j] = 'A'
                    if 965 <= a <= 1000:
                        tilemap[1][i][j] = 'F'

                if tilemap[0] == 'tilemap4':
                    a = random.randint(1,1000)
                    if 1 <= a < 35:
                        tilemap[1][i][j] = 'V'
                    if 35 <= a < 200:
                        tilemap[1][i][j] = 'S'
                    if 200 <= a < 325:
                        tilemap[1][i][j] = 'Z'
                    if 325 <= a < 525:
                        tilemap[1][i][j] = 'W'
                    if 525 <= a < 725:
                        tilemap[1][i][j] = 'K'
                    if 725 <= a < 850:
                        tilemap[1][i][j] = 'U'
                    if 850 <= a < 935:
                        tilemap[1][i][j] = 'R'
                    if 935 <= a < 965:
                        tilemap[1][i][j] = 'A'
                    if 965 <= a <= 1000:
                        tilemap[1][i][j] = 'F'
                        
                if tilemap[0] == 'tilemap5':
                    a = random.randint(1,1000)
                    if 1 <= a < 25:
                        tilemap[1][i][j] = 'V'
                    if 25 <= a < 150:
                        tilemap[1][i][j] = 'S'
                    if 150 <= a < 250:
                        tilemap[1][i][j] = 'Z'
                    if 250 <= a < 400:
                        tilemap[1][i][j] = 'W'
                    if 400 <= a < 620:
                        tilemap[1][i][j] = 'K'
                    if 620 <= a < 825:
                        tilemap[1][i][j] = 'U'
                    if 825 <= a < 930:
                        tilemap[1][i][j] = 'R'
                    if 930 <= a < 955:
                        tilemap[1][i][j] = 'A'
                    if 955 <= a <= 1000:
                        tilemap[1][i][j] = 'F'

                if tilemap[0] == 'tilemap6':
                    b = random.randint(1,1000)

                    if 1 < b < 100:
                        a = random.randint(1,1000)
                        if 1 <= a < 25:
                            tilemap[1][i][j] = 'V'
                        if 25 <= a < 150:
                            tilemap[1][i][j] = 'S'
                        if 150 <= a < 250:
                            tilemap[1][i][j] = 'Z'
                        if 250 <= a < 400:
                            tilemap[1][i][j] = 'W'
                        if 400 <= a < 610:
                            tilemap[1][i][j] = 'K'
                        if 610 <= a < 815:
                            tilemap[1][i][j] = 'U'
                        if 815 <= a < 915:
                            tilemap[1][i][j] = 'R'
                        if 915 <= a < 945:
                            tilemap[1][i][j] = 'A'
                        if 945 <= a <= 1000:
                            tilemap[1][i][j] = 'F'

                    elif b == 1:
                        tilemap[1][i][j] = 'V'
                        
                    elif b == 2:
                        tilemap[1][i][j] = 'S'

                    elif b == 3:
                        tilemap[1][i][j] = 'Z'
                        

                    elif b == 3:
                        tilemap[1][i][j] = 'W'
                    
                    elif b == 3:
                        tilemap[1][i][j] = 'K'

                    elif b == 3:
                        tilemap[1][i][j] = 'U'

                    elif b == 3:
                        tilemap[1][i][j] = 'R'

                    elif b == 3:
                        tilemap[1][i][j] = 'A'

                    elif b == 3:
                        tilemap[1][i][j] = 'F'
    return tilemap