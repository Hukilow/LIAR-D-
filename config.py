from tileMap2 import *
import pickle

TILESIZE = 32
FPS = 60

BEETLE_HEALTH = 15
BOSS_HEALTH = 250
SLIME_HEALTH = 3
ANGRY_MAID_HEALTH = 10
KNIGHT_HEALTH = 30
MULTICOLOR_MAN_HEALTH = 25
ADVENTURER_HEALTH = 15
ZOMBIE_HEALTH = 10
GARDENER_HEALTH = 1

HEALTH_LAYER = 7
PLAYER_LAYER = 6
LIGHT_LAYER = 5
ENEMY_LAYER = 4
ITEM_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1
HITBOX_LAYER = 0

PLAYER_SPEED = 3
ENEMY_SPEED = 1.5
KNIGHT_SPEED = 1
MAID_SPEED = 1.5
SLIME_SPEED = 1.5
BETTLE_SPEED = 2
BOSS_SPEED = 2
KNOCKBACK_SPEED = 10
MULTICOLOR_MAN_SPEED = 2.5
ADVENTURER_SPEED = 2.8
ZOMBIE_SPEED = 0.5
GARDENER_SPEED = 5

RED = (255, 0, 0)
LIGHTRED = (211,58,48)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
GREY = (85,79,79)
SIENNA = (160,82,45)
MARON = (139,69,19)
GREEN = (0,255,0)
LIMEGREEN = (50,205,50)

GAUCHE = ((-80,-60),(-80,60))
DROITE = ((80,-60),(80,60))
HAUT = ((-80,-60),(80,-60))
BAS = ((-80,60),(80,60))


testmap = [
'BBBBBBBBBBBBBBBBBBBB',
'BBB..BBBBBB..BBBBBBB',
'BBB..BBBBBB..BBBBBBB',
'BBB.......E.....BBBB',
'BBB.............BBBB',
'BBB..BBBBBBBBB..BBBB',
'B..P...BB.....B....B',
'B......BB....B.....B',
'B..BB..BBBB..B..BBBB',
'B..BB....B......BBBB',
'BBBBB.....BBBB..BBBB',
'BBBBBBBB..BBBB..B..B',
'BB.EBB......BBBBB..B',
'BB..BB......BB.....B',
'B.......BB...E..B..B',
'BBBBBBBBBBBBBBBBB..B',
]

"""tilemap1 = [
'.......................',
'.......................',
'.......................',
'.......................',
'............P..........',
'.......................',
'...........E...........',
'.......................',
'.......................',
'.......................',
'.......................',
'.......................',
'.......................',
'.......................',
'.......................',
]

tilemap1 = ["tilemap1",tilemap1]"""




class All_maps:
    def __init__(self):
        #self.dinop = random.randint(1,100)
        self.dinop = 100
        self.tilemap1 = generate_labyrinth(15,15)
        self.tilemap1 = ["tilemap1",self.tilemap1]
        self.tilemap1 = spawncoffres(self.tilemap1)
        self.tilemap1 = spawnennemis(self.tilemap1)

        self.tilemap2 = generate_labyrinth2(15,15,self.dinop)
        self.tilemap2 = ["tilemap2",self.tilemap2]
        self.tilemap2 = spawncoffres(self.tilemap2)
        self.tilemap2 = spawnennemis(self.tilemap2)

        self.tilemap3 = generate_labyrinth2(15,15,self.dinop)
        self.tilemap3 = ["tilemap3",self.tilemap3]
        self.tilemap3 = spawncoffres(self.tilemap3)
        self.tilemap3 = spawnennemis(self.tilemap3)

        self.tilemap4 = generate_labyrinth2(15,15,self.dinop)
        self.tilemap4 = ["tilemap4",self.tilemap4]
        self.tilemap4 = spawncoffres(self.tilemap4)
        self.tilemap4 = spawnennemis(self.tilemap4)

        self.tilemap5 = generate_labyrinth2(15,15,self.dinop)
        self.tilemap5 = ["tilemap5",self.tilemap5]
        self.tilemap5 = spawncoffres(self.tilemap5)
        self.tilemap5 = spawnennemis(self.tilemap5)

        self.tilemap6 = generate_labyrinth5(15,15,self.dinop)
        self.tilemap6 = ["tilemap6",self.tilemap6]
        self.tilemap6 = spawncoffres(self.tilemap6)
        self.tilemap6 = spawnennemis(self.tilemap6)

class All_mapsload:
    def __init__(self):
        with open('Saves/save1.dat', 'rb') as fichier:
            load_data = pickle.load(fichier)
        self.tilemap1 = load_data[1]
        self.tilemap2 = load_data[2]
        self.tilemap3 = load_data[3]
        self.tilemap4 = load_data[4]
        self.tilemap5 = load_data[5]
        self.tilemap6 = load_data[6]   

tilemap_boss_phase1 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B............................B',
    'B............................B',
    'B............................B',
    'B.....Q.................Q....B',
    'B...............Q............B',
    'B..........Q.................B',
    'B....................Q.......B',
    'B.....123....................B',
    'B.....456...............Q....B',
    'B.....789....................B',
    'BQQ..........................B',
    'BJP.Q....................W...B',
    'BQQ..........Q......123......B',
    'B.....Q.............456......B',
    'B...................789......B',
    'B............................B',
    'B......Q.........Q...........B',
    'B........................Q...B',
    'B............................B',
    'B...........Q.......Q........B',
    'B............................B',
    'B.....Q......................B',
    'B............................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',]


tilemap_boss_phase2_1 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B....L.......................B',
    'B......................L.....B',
    'B............................B',
    'B.........1223...............B',
    'B....L....4556..Q............B',
    'B.........4556...............B',
    'B.........7889...............B',
    'B....................B.......B',
    'B...................L........B',
    'B...................L.......1B',
    'BQL................L........7B',
    'BJP.L.......G......L.....W..cB',
    'BQL................L........1B',
    'B............L......L.......7B',
    'B...Q...............L........B',
    'B....................B.......B',
    'B222223......................B',
    'B555556......................B',
    'B55555522223........L........B',
    'B88885555556.................B',
    'B..x.7888889.........Q.......B',
    'B..Q.........................B',
    'B............................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',]
tilemap_boss_phase2_2 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..........LLLLLLL...........B',
    'B..........L.....Q...........B',
    'B..........L.LLL.L......Q....B',
    'B......Q...L.LCL.L...........B',
    'B..........L.L.L.L...........B',
    'B..........L.L...L....Q......B',
    'B..........L.LLLLL...........B',
    'B.......LLLL.................B',
    'B.......L....................B',
    'B.......L......Q.......L.B...B',
    'BQL...................L.....2B',
    'BJP.L.......Q........L...W..4B',
    'BQL...................L.....7B',
    'B.......L..............L.B...B',
    'B.......L....................B',
    'B...Q...LLLL.LLLLL...........B',
    'B..........L.L...L...........B',
    'B..........Q.L.L.L.......Q...B',
    'B..........L.L.L.L...........B',
    'B..Q.......L.LXL.L...........B',
    'B..........L.LLL.L...........B',
    'B..........L.....L.....Q.....B',
    'B..........LLLLLLL...........B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',]
tilemap_boss_phase3_1 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B......46.X.46...............B',
    'B......46...46.....13........B',
    'B...Q..6522256.....79........B',
    'B......7888889...........Q...B',
    'B............................B',
    'B...........BEBEB............B',
    'B...Q.....B.......B..........B',
    'B.......B.....Q.....B........B',
    'B.....B...............B......B',
    'B...........LLLLL............B',
    'BQQ.........L...L............B',
    'BJP.Q.......L.C.L......Q.W...B',
    'BQQ.........L...L............B',
    'B...........LLLLL............B',
    'B.....B...............B......B',
    'B.......B.....Q.....B........B',
    'B.........B.......B..........B',
    'B...Q.......BEBEB.......Q....B',
    'B............................B',
    'B............................B',
    'B.......Q....................B',
    'B...............Q......Q.....B',
    'B............................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',]
tilemap_boss_phase3_2 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B.........122222223..........B',
    'B.Q......15855555853....Q....B',
    'B........46B45556B46.........B',
    'B........75255555259....Q....B',
    'B..Q......788888887..........B',
    'B............................B',
    'B............................B',
    'B.....BLBLBLBLBLBEBLBLB......B',
    'B............................B',
    'B............................B',
    'BQQ..........Q...........E...B',
    'BJP.L............Q.......W.C.B',
    'BQQ......................E...B',
    'B............................B',
    'B............................B',
    'B.....BLBLBLBLBLBEBLBLB......B',
    'B.............Q..............B',
    'B............................B',
    'B.........122222223......Q...B',
    'B.....Q..15855555853.........B',
    'B........46B45556B46.........B',
    'B........75255555259.........B',
    'B.........788888887X.........B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',]

MapsBossPhase2 = [tilemap_boss_phase2_1,tilemap_boss_phase2_2]
MapsBossPhase3 = [tilemap_boss_phase3_1,tilemap_boss_phase3_2]