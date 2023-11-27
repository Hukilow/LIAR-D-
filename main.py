import pygame
from config import *
from sprites import *
import sys
import os
import pickle
from PIL import Image






class Game():
    def __init__(self):
        pygame.init()
        if os.stat("Saves/config.dat").st_size == 0:   
            self.WIN_WIDTH = 640
            self.WIN_HEIGHT = 480
            self.screen_size = (self.WIN_WIDTH,self.WIN_HEIGHT)
            self.screen = pygame.display.set_mode((self.screen_size[0],self.screen_size[1]),pygame.RESIZABLE)
            self.fullscreen = False
        else:
            with open('Saves/config.dat', 'rb') as fichier:
                self.load_data = pickle.load(fichier)
            self.WIN_WIDTH = self.load_data[0][0]
            self.WIN_HEIGHT = self.load_data[0][1]
            self.screen_size = (self.WIN_WIDTH,self.WIN_HEIGHT)
            if self.load_data[1]:
                self.fullscreen = True
                self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            else:
                self.fullscreen = False
                self.screen = pygame.display.set_mode((self.screen_size[0],self.screen_size[1]), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('mandalorelasertitle.ttf', 32)
        self.running = True
        self.win = False

        self.nombre_de_win = 0
        self.multiplicateur_difficulte_hp = 1
        self.multiplicateur_difficulte_hp_enemies = 1
        self.multiplicateur_difficulte_attack_enemies = 1
        
        self.text = f'{self.WIN_WIDTH}x{self.WIN_HEIGHT}' 
        self.screen_intro = True
        self.screen_option = False
        self.screen_save = False
        self.confirmation = False
        self.continueanimation = False
        self.writing = False
        
        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        
        self.character_spritesheet = Spritesheet('img/McLIGHT.png')
        self.terrain_spritesheet = Spritesheet('img/Blocks/terrain.png')
        self.trap_spritesheet = Spritesheet('img/Blocks/Trap.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.attack_spritesheet = Spritesheet('img/attack.png')
        self.attackscythe_spritesheet = Spritesheet('img/Attacks/scytheattacks.png')
        self.attackhellscythe_spritesheet = Spritesheet('img/Attacks/hellscytheattacks.png')
        self.attacksnakesword_spritesheet = Spritesheet('img/Attacks/snakeswordattacks.png')
        self.attackgreatsword_spritesheet = Spritesheet('img/Attacks/yellowslashesgroup.png')
        self.attackwintersballad_spritesheet = Spritesheet('img/Attacks/wintersballadattacks.png')
        self.attackmaid_spritesheet = Spritesheet('img/Attacks/whiteslashesgroup.png')
        self.intro_background = pygame.image.load('img/introbackground.jpg')
        self.game_overbackground = pygame.image.load('img/gameover.jpg')
        self.health_spritesheet = Spritesheet('img/Health/chaises.png')
        self.allchests_spritesheet = Spritesheet('img/coffres/allchests.png')
        self.etage_spritesheet = Spritesheet('img/Etage/Floor4.png')
        self.potion_spritesheet = Spritesheet('img/Health/Potion3Nombre.png')
        self.itempotion_spritesheet = Spritesheet('img/Health/ItemPotion.png')
        self.equipement_spritesheet = Spritesheetblanc('img/Equipement/Equipement.png')
        self.weapon_spritesheet = Spritesheet('img/Armes/Weapons1.png')
        self.weapon2_spritesheet = Spritesheet('img/Armes/Weapons2.png')
        self.weapon3_spritesheet = Spritesheet('img/Armes/Weapons3.png')
        self.weapon4_spritesheet = Spritesheet('img/Armes/Weapons4.png')
        self.sol_spritesheet = Spritesheet('img/Blocks/Sol.png')
        self.mur_spritesheet = Spritesheet('img/Blocks/mur48.jpg')
        self.armor_spritesheet = Spritesheet('img/Armures/armory.png')
        self.affiche_spritesheet = Spritesheet('img/Affiche/225145.png')
        self.knight_spritesheet = Spritesheet('img/Enemy/Knight/Knight3.png')
        self.knightidle_spritesheet = Spritesheet('img/Enemy/Knight/Knightidle3.png')
        self.maid_spritesheet = Spritesheet('img/Enemy/AngryMaid/Maid1.png')
        self.maididle_spritesheet = Spritesheet('img/Enemy/AngryMaid/Maid1idle.png')
        self.lavaequipement_spritesheet = Spritesheet('img/Equipement/LavaEquipement.png')
        self.knightattacks_spritesheet = Spritesheet('img/Attacks/knightattacks.png')
        self.slime_spritesheet = Spritesheet('img/Enemy/GreenSlime/BoogerBuddy.png')
        self.slimeattacks_spritesheet = Spritesheet('img/Attacks/slimeattacks.png')
        self.void_spritesheet = Spritesheet('img/Attacks/Void.png')
        self.beetle_spritesheet = Spritesheet('img/Enemy/Beetle/beetleresize.png')
        self.beetleidle_spritesheet = Spritesheet('img/Enemy/Beetle/beetleidle.png')
        self.beetleloadattacks_spritesheet = Spritesheet('img/Enemy/Beetle/beetleattacks.png')
        self.beetleattacks_spritesheet = Spritesheet('img/Attacks/beetleattacks.png')
        self.greencircle_spritesheet = Spritesheet('img/Attacks/greencircle.png')
        self.hematiteblade_spritesheet = Spritesheet('img/Attacks/hematitebladeattacks.png')
        self.earthshatter_spritesheet = Spritesheet('img/Attacks/earthshatterattacks.png')
        self.novascepter_spritesheet = Spritesheetblanc('img/Attacks/novascepterattacks.png')
        self.impactblue_spritesheet = Spritesheet('img/Attacks/ImpactBlue.png')
        self.impactwhite_spritesheet = Spritesheet('img/Attacks/ImpactWhite.png')
        self.impactpurple_spritesheet = Spritesheet('img/Attacks/ImpactPurple.png')
        self.boss_spritesheet = Spritesheet('img/Enemy/Mage/Mage-Sheet.png')
        self.bosscircle_spritesheet = Spritesheet('img/Attacks/bossbluecircle.png')
        self.bossprojectile_spritesheet = Spritesheet('img/Attacks/bossprojectile.png')
        self.bloodslash_spritesheet = Spritesheet('img/Attacks/crimsonattacks.png')

    def createTilemap(self,tilemap):
        self.player = Player(self, 0, 0)
        self.hitbox = PlayerHitbox(self,self.player.x,self.player.y)
        for i, row in enumerate(tilemap[1]):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    coordonnes = (j,i)
                if column == "E":
                    Slime(self, j, i,tilemap[0])
                if column == 'C':
                    Coffre9(self, j, i)
                if column == 'M':
                    EchelleHaut(self, j, i)
                if column == 'D':
                    EchelleBas(self, j, i)
                if column == 'L':
                    Trap(self, j, i)
                if column == 'Q':
                    Lave(self, j, i)
                if column == '1':
                    Coffre1(self,j,i)
                if column == '2':
                    Coffre2(self,j,i)
                if column == '3':
                    Coffre3(self,j,i)
                if column == '4':
                    Coffre4(self,j,i)
                if column == '5':
                    Coffre5(self,j,i)
                if column == '6':
                    Coffre6(self,j,i)
                if column == '7':
                    Coffre7(self,j,i)
                if column == '8':
                    Coffre8(self,j,i)
                if column == '9':
                    Coffre9(self,j,i)
        self.player.rect.x = coordonnes[0] * TILESIZE
        self.player.rect.y = coordonnes[1] * TILESIZE
        self.player.healthbar.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.healthbar.rect.y = (coordonnes[1] * TILESIZE) +(self.WIN_HEIGHT/2)-40
        self.player.etage.rect.x = (coordonnes[0] * TILESIZE) +(self.WIN_WIDTH/2)-180
        self.player.etage.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+20
        self.player.potion.rect.x = (coordonnes[0] * TILESIZE) +(self.WIN_WIDTH/2)-82
        self.player.potion.rect.y = (coordonnes[1] * TILESIZE) +(self.WIN_HEIGHT/2)-63
        self.player.epee.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+20
        self.player.epee.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+50
        self.player.helmet.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.helmet.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+30
        self.player.chest.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.chest.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+70
        self.player.pants.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.pants.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.player.boots.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.boots.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+150
        self.player.ranged.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+100
        self.player.ranged.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+50
        self.player.ring.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+20
        self.player.ring.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.player.necklace.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+100
        self.player.necklace.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.hitbox.rect.x = coordonnes[0] * TILESIZE
        self.hitbox.rect.y = coordonnes[1] * TILESIZE
        self.player.afficheequipped.rect.x = (coordonnes[1] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.afficheitem.rect.x = (coordonnes[1] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.afficheequipped.rect.y = (coordonnes[1] * TILESIZE)-(self.WIN_HEIGHT/2)+240
        self.player.afficheitem.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+395

    def createTilemap2(self,tilemap,endroit):         
        for i, row in enumerate(tilemap[1]):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i,tilemap[0])
                if column == 'C':
                    Coffre1(self, j, i)
                if column == 'M':
                    EchelleHaut(self, j, i)
                    if endroit == "monter":
                        coordonnes = (j,i)
                if column == 'D':
                    EchelleBas(self, j, i)
                    if endroit == "descendre":
                        coordonnes = (j,i)
                if column == 'P':
                    Ground(self,j,i)
                if column == 'L':
                    Trap(self, j, i)
                if column == 'Q':
                    Lave(self, j, i)
                if column == 'N':
                    Escalier(self, j, i)
                if column == '1':
                    Coffre1(self,j,i)
                if column == '2':
                    Coffre2(self,j,i)
                if column == '3':
                    Coffre3(self,j,i)
                if column == '4':
                    Coffre4(self,j,i)
                if column == '5':
                    Coffre6(self,j,i)
                if column == '6':
                    Coffre9(self,j,i)
                if column == '7':
                    Coffre7(self,j,i)
                if column == '8':
                    Coffre5(self,j,i)
                if column == '9':
                    Coffre8(self,j,i)
        self.player.rect.x = coordonnes[0] * TILESIZE
        self.player.rect.y = (coordonnes[1] * TILESIZE)
        self.player.healthbar.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.healthbar.rect.y = (coordonnes[1] * TILESIZE) +(self.WIN_HEIGHT/2)-40
        self.player.etage.rect.x = (coordonnes[0] * TILESIZE) +(self.WIN_WIDTH/2)-180
        self.player.etage.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+20
        self.player.potion.rect.x = (coordonnes[0] * TILESIZE) +(self.WIN_WIDTH/2)-82
        self.player.potion.rect.y = (coordonnes[1] * TILESIZE) +(self.WIN_HEIGHT/2)-63
        self.player.epee.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+20
        self.player.epee.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+50
        self.player.helmet.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.helmet.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+30
        self.player.chest.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.chest.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+70
        self.player.pants.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.pants.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.player.boots.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.boots.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+150
        self.player.ranged.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+100
        self.player.ranged.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+50
        self.player.ring.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+20
        self.player.ring.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.player.necklace.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+100
        self.player.necklace.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.hitbox.rect.x = (coordonnes[0] * TILESIZE) +9
        self.hitbox.rect.y = (coordonnes[1] * TILESIZE)+4
        self.player.afficheequipped.rect.x = (coordonnes[1] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.afficheitem.rect.x = (coordonnes[1] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.afficheequipped.rect.y = (coordonnes[1] * TILESIZE)-(self.WIN_HEIGHT/2)+240
        self.player.afficheitem.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+395
    

        for sprite in self.all_sprites:
            sprite.rect.x -= coordonnes[0]*TILESIZE
            sprite.rect.y -= coordonnes[1]*TILESIZE
            sprite.rect.x += self.WIN_WIDTH/2
            sprite.rect.y += self.WIN_HEIGHT/2


    def createTilemapboss(self,tilemap,change):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "W":
                    if change != True:
                        self.boss = Boss(self, j, i,tilemap[0])
                    else:
                        coordonnesboss = (j,i)
                if column == 'P':
                    coordonnes = (j,i)
                if column == 'L':
                    Trap(self, j, i)
                if column == 'J':
                    Escaliercasse(self, j, i)
                if column == 'Q':
                    Lave(self, j, i)
                if column == '1':
                    Lave1(self,j,i)
                if column == '2':
                    Lave2(self,j,i)
                if column == '3':
                    Lave3(self,j,i)
                if column == '4':
                    Lave4(self,j,i)
                if column == '5':
                    Lave5(self,j,i)
                if column == '6':
                    Lave6(self,j,i)
                if column == '7':
                    Lave7(self,j,i)
                if column == '8':
                    Lave8(self,j,i)
                if column == '9':
                    Lave9(self,j,i)
        self.player.rect.x = coordonnes[0] * TILESIZE
        self.player.rect.y = (coordonnes[1] * TILESIZE)
        if change == True:
            self.boss.rect.x = coordonnesboss[0] * TILESIZE
            self.boss.rect.y = (coordonnesboss[1] * TILESIZE)
        self.player.healthbar.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.healthbar.rect.y = (coordonnes[1] * TILESIZE) +(self.WIN_HEIGHT/2)-40
        self.player.etage.rect.x = (coordonnes[0] * TILESIZE) +(self.WIN_WIDTH/2)-180
        self.player.etage.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+20
        self.player.potion.rect.x = (coordonnes[0] * TILESIZE) +(self.WIN_WIDTH/2)-82
        self.player.potion.rect.y = (coordonnes[1] * TILESIZE) +(self.WIN_HEIGHT/2)-63
        self.player.epee.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+20
        self.player.epee.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+50
        self.player.helmet.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.helmet.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+30
        self.player.chest.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.chest.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+70
        self.player.pants.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.pants.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.player.boots.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+60
        self.player.boots.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+150
        self.player.ranged.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+100
        self.player.ranged.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+50
        self.player.ring.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+20
        self.player.ring.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.player.necklace.rect.x = (coordonnes[0] * TILESIZE) -(self.WIN_WIDTH/2)+100
        self.player.necklace.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+110
        self.hitbox.rect.x = (coordonnes[0] * TILESIZE) +9
        self.hitbox.rect.y = (coordonnes[1] * TILESIZE)+4
        self.player.afficheequipped.rect.x = (coordonnes[1] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.afficheitem.rect.x = (coordonnes[1] * TILESIZE) -(self.WIN_WIDTH/2)+10
        self.player.afficheequipped.rect.y = (coordonnes[1] * TILESIZE)-(self.WIN_HEIGHT/2)+240
        self.player.afficheitem.rect.y = (coordonnes[1] * TILESIZE) -(self.WIN_HEIGHT/2)+395
    

        for sprite in self.all_sprites:
            sprite.rect.x -= coordonnes[0]*TILESIZE
            sprite.rect.y -= coordonnes[1]*TILESIZE
            sprite.rect.x += self.WIN_WIDTH/2
            sprite.rect.y += self.WIN_HEIGHT/2

    def save(self):
        data = (self.player.etage.etageici, self.all_maps.tilemap1, self.all_maps.tilemap2, self.all_maps.tilemap3, self.all_maps.tilemap4, self.all_maps.tilemap5, self.all_maps.tilemap6,
                 self.player.healthbar.health, self.player.healthbar.maxhealth, self.player.helmet.ID, self.player.chest.ID, self.player.pants.ID, self.player.boots.ID, self.player.light.light_radius, self.player.light.couleur_rgb_et_intensite
                 ,self.player.vitesse,self.player.vitesse2,self.player.vitesse3,self.player.potion.nbrpotion,self.player.necklace.ID,self.player.ring.ID,self.player.puissance,
                 self.player.widthattack,self.player.heightattack,self.player.epee.ID,self.player.animation_number)

        with open("Saves/save1.dat", 'wb') as fichier:
            pickle.dump(data, fichier)

    def saveoption(self):
        if not self.fullscreen:
            WIDTH = ""
            HEIGHT = ""
            index = self.text.index("x")
            for size in range(len(self.text)):
                if size < index:
                    WIDTH += self.text[size]
                else:
                    if self.text[size] == "x" or  self.text[size] == "X":
                        continue
                    else:
                        HEIGHT += self.text[size]
            WIDTH,HEIGHT = int(WIDTH),int(HEIGHT)

            quotient,quotient2 = (WIDTH // 32),(HEIGHT // 32)
            closest_multiple,closest_multiple2 = (quotient * 32),(quotient2 * 32)
            if WIDTH - closest_multiple > 16:
                closest_multiple += 32
            if HEIGHT - closest_multiple2 > 16:
                closest_multiple2 += 32 
            WIDTH,HEIGHT = closest_multiple,closest_multiple2
            self.text = f'{self.WIN_WIDTH}x{self.WIN_HEIGHT}' 
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
            self.screen_size = (WIDTH,HEIGHT)
        
        data = (self.screen_size,self.fullscreen)

        with open("Saves/config.dat", 'wb') as fichier:
            pickle.dump(data, fichier)

    def loadsave(self):
        with open('Saves/save1.dat', 'rb') as fichier:
            load_data = pickle.load(fichier)

        EtageSave = load_data[0]
        tilemap = load_data[EtageSave]
        self.all_maps = All_mapsload()

        self.playing = True
        self.win = False
        self.all_sprites = pygame.sprite.LayeredUpdates() #toutes les apparences
        self.blocks = pygame.sprite.LayeredUpdates() #murs
        self.enemies = pygame.sprite.LayeredUpdates() #ennemis
        self.attacks = pygame.sprite.LayeredUpdates() #attacks
        self.attacksenemy = pygame.sprite.LayeredUpdates()
        self.interaction = pygame.sprite.LayeredUpdates()
        self.healthbar = pygame.sprite.LayeredUpdates()
        self.item = pygame.sprite.LayeredUpdates()
        self.coffre1 = pygame.sprite.LayeredUpdates()
        self.coffre2 = pygame.sprite.LayeredUpdates()
        self.coffre3 = pygame.sprite.LayeredUpdates()
        self.coffre4 = pygame.sprite.LayeredUpdates()
        self.coffre5 = pygame.sprite.LayeredUpdates()
        self.coffre6 = pygame.sprite.LayeredUpdates()
        self.coffre7 = pygame.sprite.LayeredUpdates()
        self.coffre8 = pygame.sprite.LayeredUpdates()
        self.coffre9 = pygame.sprite.LayeredUpdates()
        self.echellehaut = pygame.sprite.LayeredUpdates()
        self.echellebas = pygame.sprite.LayeredUpdates()
        self.coffrecasse = pygame.sprite.LayeredUpdates()
        self.trap = pygame.sprite.LayeredUpdates()
        self.escalier = pygame.sprite.LayeredUpdates()
        self.playerhitbox =  pygame.sprite.LayeredUpdates()
        self.light = pygame.sprite.LayeredUpdates()
        self.escaliercasse = pygame.sprite.LayeredUpdates()
        self.lave = pygame.sprite.LayeredUpdates()

        if EtageSave == 1:
            self.createTilemap(tilemap)
        elif EtageSave > 1 < 7:
            self.createTilemap2(tilemap,"monter")
        elif EtageSave == 7:
            self.createTilemapboss(tilemap_boss,False)

        self.player.healthbar.health = load_data[7]
        self.player.healthbar.maxhealth = load_data[8]
        if load_data[9] != None:
            self.player.helmet.ID = load_data[9]
            self.player.helmet.image = self.armor_spritesheet.get_sprite(load_data[9].IDimage[0],load_data[9].IDimage[1],load_data[9].IDimage[2],load_data[9].IDimage[3])
        if load_data[10] != None:    
            self.player.chest.ID = load_data[10]
            self.player.chest.image = self.armor_spritesheet.get_sprite(load_data[10].IDimage[0],load_data[10].IDimage[1],load_data[10].IDimage[2],load_data[10].IDimage[3])
        if load_data[11] != None: 
            self.player.pants.ID = load_data[11]
            self.player.pants.image = self.armor_spritesheet.get_sprite(load_data[11].IDimage[0],load_data[11].IDimage[1],load_data[11].IDimage[2],load_data[11].IDimage[3])
        if load_data[12] != None: 
            self.player.boots.ID = load_data[12]
            self.player.boots.image = self.armor_spritesheet.get_sprite(load_data[12].IDimage[0],load_data[12].IDimage[1],load_data[12].IDimage[2],load_data[12].IDimage[3])
        self.player.light.light_radius = load_data[13]
        self.player.light.couleur_rgb_et_intensite = load_data[14]
        self.player.vitesse = load_data[15]
        self.player.vitesse2 = load_data[16]
        self.player.vitesse3 = load_data[17]
        self.player.potion.nbrpotion = load_data[18]
        if load_data[19] != None: 
            self.player.necklace.ID = load_data[19]
            self.player.necklace.image = self.armor_spritesheet.get_sprite(load_data[19].IDimage[0],load_data[19].IDimage[1],load_data[19].IDimage[2],load_data[19].IDimage[3])
        if load_data[20] != None: 
            self.player.ring.ID = load_data[20]
            self.player.ring.image = self.armor_spritesheet.get_sprite(load_data[20].IDimage[0],load_data[20].IDimage[1],load_data[20].IDimage[2],load_data[20].IDimage[3])
        if load_data[24] != None:
            self.player.puissance = load_data[21]
            self.player.widthattack = load_data[22]
            self.player.heightattack = load_data[23]
            self.player.epee.ID = load_data[24] 
            self.player.epee.image = eval(load_data[24].IDimage)
            rightattack = []
            downattack = []
            leftattack = []
            upattack = []

            for i in range(len(load_data[24].IDattack)//4):
                rightattack.append(eval(load_data[24].IDattack[i]))

            for i in range(((len(load_data[24].IDattack))//4),((len(load_data[24].IDattack))//4)*2):
                downattack.append(eval(load_data[24].IDattack[i]))

            for i in range(((len(load_data[24].IDattack))//4)*2,((len(load_data[24].IDattack))//4)*3):
                leftattack.append(eval(load_data[24].IDattack[i]))
                
            for i in range(((len(load_data[24].IDattack))//4)*3,(len(load_data[24].IDattack))):
                upattack.append(eval(load_data[24].IDattack[i]))

            self.player.rightattack_animations = rightattack
            self.player.downattack_animations = downattack
            self.player.leftattack_animations = leftattack
            self.player.upattack_animations = upattack
            self.player.animation_number = load_data[25]


    def new(self):
        self.playing = True
        self.win = False
        self.all_sprites = pygame.sprite.LayeredUpdates() #toutes les apparences
        self.blocks = pygame.sprite.LayeredUpdates() #murs
        self.enemies = pygame.sprite.LayeredUpdates() #ennemis
        self.attacks = pygame.sprite.LayeredUpdates() #attacks
        self.attacksenemy = pygame.sprite.LayeredUpdates()
        self.interaction = pygame.sprite.LayeredUpdates()
        self.healthbar = pygame.sprite.LayeredUpdates()
        self.item = pygame.sprite.LayeredUpdates()
        self.coffre1 = pygame.sprite.LayeredUpdates()
        self.coffre2 = pygame.sprite.LayeredUpdates()
        self.coffre3 = pygame.sprite.LayeredUpdates()
        self.coffre4 = pygame.sprite.LayeredUpdates()
        self.coffre5 = pygame.sprite.LayeredUpdates()
        self.coffre6 = pygame.sprite.LayeredUpdates()
        self.coffre7 = pygame.sprite.LayeredUpdates()
        self.coffre8 = pygame.sprite.LayeredUpdates()
        self.coffre9 = pygame.sprite.LayeredUpdates()
        self.echellehaut = pygame.sprite.LayeredUpdates()
        self.echellebas = pygame.sprite.LayeredUpdates()
        self.coffrecasse = pygame.sprite.LayeredUpdates()
        self.trap = pygame.sprite.LayeredUpdates()
        self.escalier = pygame.sprite.LayeredUpdates()
        self.playerhitbox =  pygame.sprite.LayeredUpdates()
        self.light = pygame.sprite.LayeredUpdates()
        self.escaliercasse = pygame.sprite.LayeredUpdates()
        self.lave = pygame.sprite.LayeredUpdates()

        
        self.all_maps = All_maps()      
        self.createTilemap(self.all_maps.tilemap1)
        self.save()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save()
                self.playing = False
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Attack(self)

        
    def update(self):
        self.all_sprites.update()
        self.win_screen()
        self.WIN_WIDTH = pygame.display.get_surface().get_width()
        self.WIN_HEIGHT = pygame.display.get_surface().get_height()
        

    def draw(self): #afficher les sprites
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        if not self.fullscreen:
            self.screen = pygame.display.set_mode((self.WIN_WIDTH,self.WIN_HEIGHT))
        for sprite in self.all_sprites:
            sprite.rect.x -= (len(self.all_maps.tilemap1[1])*TILESIZE)/2
            sprite.rect.x += self.WIN_WIDTH/2
            sprite.rect.y -= (len(self.all_maps.tilemap1[1][0])*TILESIZE)/2
            sprite.rect.y += self.WIN_HEIGHT/2

        if self.continueanimation and (self.player.epee.ID != None):
            with open('Saves/save1.dat', 'rb') as fichier:
                load_data = pickle.load(fichier)
            self.player.arme_x_left = eval(load_data[24].IDpos[0])
            self.player.arme_y_left = eval(load_data[24].IDpos[1])
            self.player.arme_x_down = eval(load_data[24].IDpos[2])
            self.player.arme_y_down = eval(load_data[24].IDpos[3])
            self.player.arme_x_right = eval(load_data[24].IDpos[4])
            self.player.arme_y_right = eval(load_data[24].IDpos[5])
            self.player.arme_x_up = eval(load_data[24].IDpos[6])
            self.player.arme_y_up = eval(load_data[24].IDpos[7])

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(self.WIN_WIDTH/2, self.WIN_HEIGHT/2))

        restart_button = Button(self.WIN_WIDTH-200,self.WIN_HEIGHT-100, 120,50, WHITE, BLACK, 'Restart', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if restart_button.is_pressed(mouse_pos, mouse_pressed):
                    self.new()
                    self.main()

                self.screen.blit(self.game_overbackground, (0,0))
                self.screen.blit(text, text_rect)
                self.screen.blit(restart_button.image, restart_button.rect)
                self.clock.tick(FPS)
                pygame.display.update()

    def intro_screen(self):
        intro = True

        while intro:
            self.blackscreen = pygame.Surface((self.WIN_WIDTH,self.WIN_HEIGHT))
            self.WIN_WIDTH = pygame.display.get_surface().get_width()
            self.WIN_HEIGHT = pygame.display.get_surface().get_height()
            self.intro_background = Image.open('img/introbackground.jpg')
            self.intro_background = self.intro_background.resize((self.WIN_WIDTH, self.WIN_HEIGHT))
            self.intro_background.save('img/introbackground.jpg')
            self.intro_background = pygame.image.load('img/introbackground.jpg')
            title = self.font.render('Lost In A Random (dungeon)', True, BLACK)
            title_rect = title.get_rect(x = 100, y = 30)
            Screen_size = self.font.render('Screen size :', True, WHITE)
            Screen_size_rect = title.get_rect(x = self.WIN_WIDTH/2-225, y = self.WIN_HEIGHT/3+8)
            Confirmation1= self.font.render("Etes vous sur de vouloir", True, WHITE)
            Confirmation2 = self.font.render("effacer l'ancienne sauvegarde ?", True, WHITE)
            Confirmation1_rect = title.get_rect(x = self.WIN_WIDTH/2-215, y = self.WIN_HEIGHT/2-20 )
            Confirmation2_rect = title.get_rect(x = self.WIN_WIDTH/2-270, y = self.WIN_HEIGHT/2+10 )
            Warning1 = self.font.render("Warning !", True, RED)
            Warning2 = self.font.render("Fullscreen can causes a lack of performance", True, WHITE)
            Warning3 = self.font.render("Recommended window size : 1600x928", True, WHITE)
            Warning1_rect = title.get_rect(x = self.WIN_WIDTH/2-175, y = self.WIN_HEIGHT/2-50 )
            Warning2_rect = title.get_rect(x = self.WIN_WIDTH/2-350, y = self.WIN_HEIGHT/2)
            Warning3_rect = title.get_rect(x = self.WIN_WIDTH/2-350, y = self.WIN_HEIGHT/2+50)
            Fullscreen = self.font.render("Fullscreen :", True, WHITE)
            Fullscreen_rect = title.get_rect(x = self.WIN_WIDTH/2-225, y = self.WIN_HEIGHT/2-220 )
            save_button = Button(self.WIN_WIDTH-150, self.WIN_HEIGHT-75 ,100 ,50 ,WHITE ,BLACK ,'SAVE' ,32)
            reset_button = Button(self.WIN_WIDTH-300, self.WIN_HEIGHT-75 ,100 ,50 ,WHITE ,BLACK ,'RESET' ,32)
            new_button = Button(self.WIN_WIDTH/2-50, self.WIN_HEIGHT/2-100 ,100 ,50 ,WHITE ,BLACK ,'New' ,32)
            option_button = Button(50, self.WIN_HEIGHT-75 ,100 ,50 ,WHITE ,BLACK ,'Option' ,32)
            quit_button = Button(50, self.WIN_HEIGHT-75 ,100 ,50 ,WHITE ,BLACK ,'Quit' ,32)
            quitgame_button = Button(self.WIN_WIDTH-100, self.WIN_HEIGHT-75 ,100 ,50 ,WHITE ,BLACK ,'Quit' ,32)
            continue_button = Button(self.WIN_WIDTH/2-100, self.WIN_HEIGHT/2-150 ,200 ,50 ,WHITE ,BLACK ,'continue' ,32)
            yes_button = Button(self.WIN_WIDTH/2-125, self.WIN_HEIGHT/2+70 ,100 ,50 ,GREEN ,BLACK ,'Yes' ,32)
            no_button = Button(self.WIN_WIDTH/2+35, self.WIN_HEIGHT/2+70 ,100 ,50 ,RED ,BLACK ,'No' ,32)
            Square = pygame.Surface((50,50),pygame.SRCALPHA)
            pygame.draw.rect(Square, WHITE, pygame.Rect(0, 0, 50, 50))
            Square_rect = title.get_rect(x = self.WIN_WIDTH/2, y = self.WIN_HEIGHT/2-225)
            ConfirmationRectangle = pygame.Surface((110,60),pygame.SRCALPHA)
            pygame.draw.rect(ConfirmationRectangle, WHITE, pygame.Rect(0, 0, 110, 60))
            ConfirmationRectangleYes_rect = title.get_rect(x = self.WIN_WIDTH/2-130, y = self.WIN_HEIGHT/2+65)
            ConfirmationRectangleNo_rect = title.get_rect(x = self.WIN_WIDTH/2+30, y = self.WIN_HEIGHT/2+65)
            Rectangle = pygame.Surface((210,60),pygame.SRCALPHA)
            pygame.draw.rect(Rectangle, WHITE, pygame.Rect(0, 0, 210, 60))
            Screen_size_button = Button(self.WIN_WIDTH/2, self.WIN_HEIGHT/3-8 , 200,50 ,WHITE ,WHITE ,'' ,32)
            if self.fullscreen:
                Fullscreen_button = Button(self.WIN_WIDTH/2+5, self.WIN_HEIGHT/2-220 ,40 ,40 ,WHITE, WHITE,'' ,32)
            else:
                Fullscreen_button = Button(self.WIN_WIDTH/2+5, self.WIN_HEIGHT/2-220 ,40 ,40 ,WHITE, BLACK,'' ,32)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    print(event.w, event.h)
                    self.WIN_WIDTH, self.WIN_HEIGHT = event.w, event.h
                    quotient,quotient2 = (self.WIN_WIDTH // 32),(self.WIN_HEIGHT // 32)
                    closest_multiple,closest_multiple2 = (quotient * 32),(quotient2 * 32)
                    if self.WIN_WIDTH - closest_multiple > 16:
                        closest_multiple += 32
                    if self.WIN_HEIGHT - closest_multiple2 > 16:
                        closest_multiple2 += 32 
                    self.WIN_WIDTH,self.WIN_HEIGHT = closest_multiple,closest_multiple2
                    print(self.WIN_WIDTH, self.WIN_HEIGHT)
                    self.text = f'{self.WIN_WIDTH}x{self.WIN_HEIGHT}'
                    self.screen = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT),pygame.RESIZABLE)
                if self.writing:
                    if event.type == pygame.KEYDOWN:
                        Xkey = False
                        for key in self.text:
                            if key == "X" or key == "x":
                                Xkey = True
                                break
                        if event.key == pygame.K_BACKSPACE:
                            if not self.delete_time():
                                if len(self.text)>0:
                                    self.text = self.text[:-1]
                                    self.derniertemps1 = pygame.time.get_ticks()
                                    Xkey = False
                                    for key in self.text:
                                        if key == "X" or key == "x":
                                            Xkey = True
                                            break
                        if len(self.text) < 9:
                            if len(self.text) == 3 and self.text[-1] != "x" :
                                if  event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, 
                                    pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9,pygame.K_x, pygame.KSCAN_X):  
                                        self.text += event.unicode
                                        if event.key in (pygame.K_x, pygame.KSCAN_X):
                                            Xkey = True
                            elif len(self.text) == 4 and self.text[-1] != "x" :
                                if event.key in (pygame.K_x, pygame.KSCAN_X):
                                    self.text += event.unicode
                                    Xkey = True
                            elif len(self.text) < 3:
                                    if  event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, 
                                    pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9):  
                                        self.text += event.unicode
                            if Xkey:
                                if self.text[3] == "x" or self.text[3] == "X":
                                    if len(self.text) < 8:
                                        if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, 
                                                pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9):
                                                self.text += event.unicode
                                else:
                                    if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, 
                                        pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9):
                                        self.text += event.unicode
                        img = self.font.render(self.text, True, RED)
                        rect.size=img.get_size()
                        cursor.topleft = rect.topright
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
    
            if self.screen_intro:
                self.screen.blit(self.blackscreen,(0,0))
                self.screen.blit(self.intro_background, (0,0))
                self.screen.blit(title, title_rect)
                self.screen.blit(new_button.image, new_button.rect)
                self.screen.blit(option_button.image, option_button.rect)
                self.screen.blit(quitgame_button.image, quitgame_button.rect)
                if self.confirmation:
                    self.screen.blit(Confirmation1,Confirmation1_rect)
                    self.screen.blit(Confirmation2,Confirmation2_rect)
                    self.screen.blit(ConfirmationRectangle, ConfirmationRectangleYes_rect)
                    self.screen.blit(yes_button.image, yes_button.rect)
                    self.screen.blit(ConfirmationRectangle, ConfirmationRectangleNo_rect)
                    self.screen.blit(no_button.image, no_button.rect)
                    if yes_button.is_pressed(mouse_pos, mouse_pressed):
                        intro = False
                        self.new()
                        self.confirmation = False
                    elif no_button.is_pressed(mouse_pos, mouse_pressed):
                        self.confirmation = False

                if os.stat("Saves/save1.dat").st_size != 0:
                    self.screen.blit(continue_button.image, continue_button.rect) 

                if os.stat("Saves/save1.dat").st_size != 0:
                    if continue_button.is_pressed(mouse_pos, mouse_pressed):
                        intro = False
                        
                        self.loadsave()
                        self.continueanimation = True

                if new_button.is_pressed(mouse_pos, mouse_pressed):
                    if os.stat("Saves/save1.dat").st_size != 0:      
                        self.confirmation = True
                    else:
                        intro = False
                        self.new()

                if option_button.is_pressed(mouse_pos, mouse_pressed):
                    if self.clicktime() == False:
                        self.screen_intro = False
                        self.screen_option = True
                        self.derniertemps = pygame.time.get_ticks()
                if quitgame_button.is_pressed(mouse_pos, mouse_pressed):
                    self.running = False
                    intro = False
                self.clock.tick(FPS)
                pygame.display.update()
            if self.screen_option:
                if Fullscreen_button.is_pressed(mouse_pos, mouse_pressed):
                    if self.clicktime() == False:
                        if self.fullscreen:
                            self.fullscreen = False
                            self.screen = pygame.display.set_mode((self.WIN_WIDTH,self.WIN_HEIGHT),pygame.RESIZABLE)
                        else:
                            self.fullscreen = True
                            self.screen_size = (640,480)
                            self.WIN_WIDTH = 640
                            self.WIN_HEIGHT = 480
                            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)    
                        self.derniertemps = pygame.time.get_ticks()       
                if quit_button.is_pressed(mouse_pos, mouse_pressed):
                    if self.clicktime() == False:
                        self.screen_intro = True
                        self.screen_option = False
                        self.derniertemps = pygame.time.get_ticks()
                if save_button.is_pressed(mouse_pos, mouse_pressed):
                    self.saveoption()
                if reset_button.is_pressed(mouse_pos, mouse_pressed):
                    self.WIN_WIDTH,self.WIN_HEIGHT = 1280,800
                    self.text = f'{self.WIN_WIDTH}x{self.WIN_HEIGHT}' 
                    self.screen = pygame.display.set_mode((self.WIN_WIDTH,self.WIN_HEIGHT),pygame.RESIZABLE)
                self.screen.blit(self.blackscreen,(0,0))
                self.screen.blit(reset_button.image, reset_button.rect)
                self.screen.blit(save_button.image, save_button.rect)
                self.screen.blit(Square, Square_rect)
                self.screen.blit(Fullscreen, Fullscreen_rect)
                self.screen.blit(Fullscreen_button.image, Fullscreen_button.rect)
                self.screen.blit(quit_button.image, quit_button.rect)

            if not self.fullscreen and self.screen_option:
                if Screen_size_button.is_pressed(mouse_pos, mouse_pressed):
                    if not self.clicktime():
                        self.derniertemps = pygame.time.get_ticks()
                        if self.writing:
                            self.writing = False
                        else:
                            self.writing = True
                img = self.font.render(self.text, True, WHITE)

                rect = img.get_rect()
                rect.topleft = (self.WIN_WIDTH/2, self.WIN_HEIGHT/3+8)
                cursor = pygame.Rect(rect.topright, (3, rect.height)) 

                
                self.screen.blit(img, rect)
                if time.time() % 1 > 0.5:
                    if self.writing:
                        pygame.draw.rect(self.screen, WHITE, cursor)

                self.screen.blit(Screen_size, Screen_size_rect)

            if self.fullscreen and self.screen_option:
                self.screen.blit(Warning1, Warning1_rect)
                self.screen.blit(Warning2, Warning2_rect)
                self.screen.blit(Warning3, Warning3_rect)



            self.clock.tick(FPS)
            pygame.display.update()

            if self.screen_save:
                if quit_button.is_pressed(mouse_pos, mouse_pressed):
                    if self.clicktime() == False:
                        self.screen_intro = True
                        self.screen_save = False
                        self.derniertemps = pygame.time.get_ticks()
                self.screen.blit(quit_button.image, quit_button.rect)
                self.screen.blit(new_button.image, new_button.rect)
                self.clock.tick(FPS)
                pygame.display.update()

    def delete_time(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 150
        


    def win_screen(self):
        if self.win == True:
            text = self.font.render('You won loleee', True, WHITE)
            text_rect = text.get_rect(center=(self.WIN_WIDTH/2, 100))

            hp_multiplicateur_button = Button(50,self.WIN_HEIGHT/2, 300,50, WHITE, BLUE, 'HP decrease for Player', 16)
            hpenemy_multiplicateur_button = Button(self.WIN_WIDTH/2-150,self.WIN_HEIGHT/2, 300,50, WHITE, RED, 'HP increase for Enemies', 16)
            attackenemy_multiplicateur_button = Button((self.WIN_WIDTH-350),self.WIN_HEIGHT/2, 300,50, WHITE, GREEN, 'Attack increase for Enemies', 16)

            for sprite in self.all_sprites:
                sprite.kill()

            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()

                    if hp_multiplicateur_button.is_pressed(mouse_pos, mouse_pressed):
                        self.multiplicateur_difficulte_hp -= 0.3
                        self.difficulty_upgrade = True
                        self.nombre_de_win += 1
                        self.new()
                        self.main()

                    if hpenemy_multiplicateur_button.is_pressed(mouse_pos, mouse_pressed):
                        self.multiplicateur_difficulte_hp_enemies += 0.3
                        self.difficulty_upgrade = True
                        self.nombre_de_win += 1
                        self.new()
                        self.main()

                    if attackenemy_multiplicateur_button.is_pressed(mouse_pos, mouse_pressed):
                        self.multiplicateur_difficulte_attack_enemies += 1
                        self.difficulty_upgrade = True
                        self.nombre_de_win += 1
                        self.new()
                        self.main()
                        
                    self.screen.blit(self.game_overbackground, (0,0))
                    self.screen.blit(text, text_rect)
                    self.screen.blit(hp_multiplicateur_button.image, hp_multiplicateur_button.rect)
                    self.screen.blit(hpenemy_multiplicateur_button.image, hpenemy_multiplicateur_button.rect)
                    self.screen.blit(attackenemy_multiplicateur_button.image, attackenemy_multiplicateur_button.rect)
                    self.clock.tick(FPS)
                    pygame.display.update()
                    self.win = False

    def clicktime(self):
        return self.derniertemps > pygame.time.get_ticks() - 250




g = Game()
g.intro_screen()

while g.running:
    g.main()
    g.game_over()
    

pygame.quit()
sys.exit()

