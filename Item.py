import pygame
from config import *
from HUD import Light


class Potion(pygame.sprite.Sprite):
    nom = 'Health Potion'
    attribut = 'Health : +5'
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = self.game.itempotion_spritesheet.get_sprite(0,0,32,32)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if hits and keys[pygame.K_e]:
                self.game.player.potion.item_pris()
                self.game.player.afficheitem.trueorfalse = False
                self.kill()

class Scythe(pygame.sprite.Sprite):
    nom = "Scythe"
    attribut = "Puissance : +2"
    IDimage = "self.weapon_spritesheet.get_sprite(81,68,28,42)"
    IDattack = ("self.attackscythe_spritesheet.get_sprite(0, 0, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(50, 0 ,50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(100, 0, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(150, 0, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(200, 0, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(250, 0, 50, 60)","self.attackscythe_spritesheet.get_sprite(0, 60, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(60, 60, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(120, 60, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(180, 60, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(240, 60, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(300, 60, 60, 50)","self.attackscythe_spritesheet.get_sprite(0, 110, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(50, 110, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(100, 110, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(150, 110, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(200, 110, 50, 60)",
                           "self.attackscythe_spritesheet.get_sprite(250, 110, 50, 60)","self.attackscythe_spritesheet.get_sprite(0, 170, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(60, 170, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(120, 170, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(180, 170, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(240, 170, 60, 50)",
                           "self.attackscythe_spritesheet.get_sprite(300, 170, 60, 50)",)
    IDpos = ("self.player.rect.x - (TILESIZE+20)",
        "self.player.rect.y - (TILESIZE/2)",
        "self.player.rect.x - (TILESIZE/2)",
        "self.player.rect.y + TILESIZE",
        "self.player.rect.x + TILESIZE",
        "self.player.rect.y - (TILESIZE/2)",
        "self.player.rect.x - (TILESIZE/2)",
        "self.player.rect.y - (TILESIZE+20)",)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Scythe
        self.image = self.game.weapon_spritesheet.get_sprite(81,68,28,42)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 2

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.rightattack_scythe = [self.game.attackscythe_spritesheet.get_sprite(0, 0, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(50, 0 ,50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(100, 0, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(150, 0, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(200, 0, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(250, 0, 50, 60),]

        self.downattack_scythe = [self.game.attackscythe_spritesheet.get_sprite(0, 60, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(60, 60, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(120, 60, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(180, 60, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(240, 60, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(300, 60, 60, 50),]

        self.leftattack_scythe = [self.game.attackscythe_spritesheet.get_sprite(0, 110, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(50, 110, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(100, 110, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(150, 110, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(200, 110, 50, 60),
                           self.game.attackscythe_spritesheet.get_sprite(250, 110, 50, 60),]

        self.upattack_scythe = [self.game.attackscythe_spritesheet.get_sprite(0, 170, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(60, 170, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(120, 170, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(180, 170, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(240, 170, 60, 50),
                           self.game.attackscythe_spritesheet.get_sprite(300, 170, 60, 50),]
        self.scythe_x_left = self.game.player.rect.x - (TILESIZE+20)
        self.scythe_y_left = self.game.player.rect.y - (TILESIZE/2)
        self.scythe_x_down = self.game.player.rect.x - (TILESIZE/2)
        self.scythe_y_down = self.game.player.rect.y + TILESIZE
        self.scythe_x_right = self.game.player.rect.x + TILESIZE
        self.scythe_y_right = self.game.player.rect.y - (TILESIZE/2)
        self.scythe_x_up = self.game.player.rect.x - (TILESIZE/2)
        self.scythe_y_up = self.game.player.rect.y - (TILESIZE+20)
        self.animation_number = 6


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.epee.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Scythe
                    self.game.player.widthattack = 60
                    self.game.player.heightattack = 50
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.rightattack_scythe
                    self.game.player.downattack_animations = self.downattack_scythe 
                    self.game.player.leftattack_animations = self.leftattack_scythe
                    self.game.player.upattack_animations = self.upattack_scythe
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Hematite_Blade(pygame.sprite.Sprite):
    nom = "Hematite Blade"
    attribut = "Puissance : +9"
    IDimage = "self.weapon3_spritesheet.get_sprite(156,89,17,45)"
    IDattack = ("self.hematiteblade_spritesheet.get_sprite(0, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(64, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(128, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(192, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(256, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(320, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(384, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(448, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(512, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(576, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(640, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(704, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(768, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(832, 0, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(896, 0, 64, 49)","self.hematiteblade_spritesheet.get_sprite(0, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(49, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(98, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(147, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(196, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(245, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(294, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(343, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(392, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(441, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(490, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(539, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(588, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(637, 49, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(686, 49, 49, 64)","self.hematiteblade_spritesheet.get_sprite(0, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(64, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(128, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(192, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(256, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(320, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(384, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(448, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(512, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(576, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(640, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(704, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(768, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(832, 113, 64, 49)",
        "self.hematiteblade_spritesheet.get_sprite(896, 113, 64, 49)","self.hematiteblade_spritesheet.get_sprite(0, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(49, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(98, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(147, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(196, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(245, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(294, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(343, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(392, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(441, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(490, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(539, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(588, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(637, 162, 49, 64)",
        "self.hematiteblade_spritesheet.get_sprite(686, 162, 49, 64)",)
    IDpos = ("self.player.rect.x - (TILESIZE+30)",
        "self.player.rect.y - (TILESIZE/2)+10",
        "self.player.rect.x - (TILESIZE/2)+10",
        "self.player.rect.y + TILESIZE",
        "self.player.rect.x + TILESIZE",
        "self.player.rect.y - (TILESIZE/2)",
        "self.player.rect.x - (TILESIZE/2)+10",
        "self.player.rect.y - (TILESIZE+30)",)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Hematite_Blade
        self.image = self.game.weapon3_spritesheet.get_sprite(156,89,17,45)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 9

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.right_attacksanimation = [self.game.hematiteblade_spritesheet.get_sprite(0, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(64, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(128, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(192, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(256, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(320, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(384, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(448, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(512, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(576, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(640, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(704, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(768, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(832, 0, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(896, 0, 64, 49),]

        self.down_attacksanimation = [self.game.hematiteblade_spritesheet.get_sprite(0, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(49, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(98, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(147, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(196, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(245, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(294, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(343, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(392, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(441, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(490, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(539, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(588, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(637, 49, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(686, 49, 49, 64),]

        self.left_attacksanimation = [self.game.hematiteblade_spritesheet.get_sprite(0, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(64, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(128, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(192, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(256, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(320, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(384, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(448, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(512, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(576, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(640, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(704, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(768, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(832, 113, 64, 49),
        self.game.hematiteblade_spritesheet.get_sprite(896, 113, 64, 49),]

        self.up_attacksanimation = [self.game.hematiteblade_spritesheet.get_sprite(0, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(49, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(98, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(147, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(196, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(245, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(294, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(343, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(392, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(441, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(490, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(539, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(588, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(637, 162, 49, 64),
        self.game.hematiteblade_spritesheet.get_sprite(686, 162, 49, 64),]


        self.scythe_x_left = self.game.player.rect.x - (TILESIZE+30)
        self.scythe_y_left = self.game.player.rect.y - (TILESIZE/2)+10
        self.scythe_x_down = self.game.player.rect.x - (TILESIZE/2)+10
        self.scythe_y_down = self.game.player.rect.y + TILESIZE
        self.scythe_x_right = self.game.player.rect.x + TILESIZE
        self.scythe_y_right = self.game.player.rect.y - (TILESIZE/2)
        self.scythe_x_up = self.game.player.rect.x - (TILESIZE/2)+10
        self.scythe_y_up = self.game.player.rect.y - (TILESIZE+30)
        self.animation_number = 15


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.epee.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Hematite_Blade
                    self.game.player.widthattack = 65
                    self.game.player.heightattack = 50
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.right_attacksanimation
                    self.game.player.downattack_animations = self.down_attacksanimation
                    self.game.player.leftattack_animations = self.left_attacksanimation
                    self.game.player.upattack_animations = self.up_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class HellScythe(pygame.sprite.Sprite):
    nom = "Hell Scythe"
    attribut = "Puissance : +8"
    IDimage = "self.weapon2_spritesheet.get_sprite(100,80,26,33)"
    IDattack = ("self.attackhellscythe_spritesheet.get_sprite(0, 0, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(60, 0 ,60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(120, 0, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(180, 0, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(240, 0, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(300, 0, 60, 80)","self.attackhellscythe_spritesheet.get_sprite(0, 80, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(80, 80, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(160, 80, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(240, 80, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(320, 80, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(400, 80, 80, 60)","self.attackhellscythe_spritesheet.get_sprite(0, 140, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(60, 140, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(120, 140, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(180, 140, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(240, 140, 60, 80)",
                           "self.attackhellscythe_spritesheet.get_sprite(300, 140, 60, 80)","self.attackhellscythe_spritesheet.get_sprite(0, 220, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(80, 220, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(160, 220, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(240, 220, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(320, 220, 80, 60)",
                           "self.attackhellscythe_spritesheet.get_sprite(400, 220, 80, 60)",)
    IDpos = ("self.player.rect.x - (TILESIZE+20)",
        "self.player.rect.y - (TILESIZE/2)",
        "self.player.rect.x - (TILESIZE/2)",
        "self.player.rect.y + TILESIZE",
        "self.player.rect.x + TILESIZE",
        "self.player.rect.y - (TILESIZE/2)",
        "self.player.rect.x - (TILESIZE/2)-10",
        "self.player.rect.y - (TILESIZE+20)",)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = HellScythe
        self.image = self.game.weapon2_spritesheet.get_sprite(100,80,26,33)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 8

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.rightattack_scythe = [self.game.attackhellscythe_spritesheet.get_sprite(0, 0, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(60, 0 ,60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(120, 0, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(180, 0, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(240, 0, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(300, 0, 60, 80),]

        self.downattack_scythe = [self.game.attackhellscythe_spritesheet.get_sprite(0, 80, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(80, 80, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(160, 80, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(240, 80, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(320, 80, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(400, 80, 80, 60),]

        self.leftattack_scythe = [self.game.attackhellscythe_spritesheet.get_sprite(0, 140, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(60, 140, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(120, 140, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(180, 140, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(240, 140, 60, 80),
                           self.game.attackhellscythe_spritesheet.get_sprite(300, 140, 60, 80),]

        self.upattack_scythe = [self.game.attackhellscythe_spritesheet.get_sprite(0, 220, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(80, 220, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(160, 220, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(240, 220, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(320, 220, 80, 60),
                           self.game.attackhellscythe_spritesheet.get_sprite(400, 220, 80, 60),]
        self.scythe_x_left = self.game.player.rect.x - (TILESIZE+20)
        self.scythe_y_left = self.game.player.rect.y - (TILESIZE/2)
        self.scythe_x_down = self.game.player.rect.x - (TILESIZE/2)
        self.scythe_y_down = self.game.player.rect.y + TILESIZE
        self.scythe_x_right = self.game.player.rect.x + TILESIZE
        self.scythe_y_right = self.game.player.rect.y - (TILESIZE/2)
        self.scythe_x_up = self.game.player.rect.x - (TILESIZE/2)-10
        self.scythe_y_up = self.game.player.rect.y - (TILESIZE+20)
        self.animation_number = 6


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.epee.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = HellScythe
                    self.game.player.widthattack = 60
                    self.game.player.heightattack = 80
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.rightattack_scythe
                    self.game.player.downattack_animations = self.downattack_scythe 
                    self.game.player.leftattack_animations = self.leftattack_scythe
                    self.game.player.upattack_animations = self.upattack_scythe
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()
                    
class WintersBallad(pygame.sprite.Sprite):
    nom = "Winter's Ballad"
    attribut = "Puissance : +6"
    IDimage = "self.weapon4_spritesheet.get_sprite(4,4,16,43)"
    IDattack = ("self.attackwintersballad_spritesheet.get_sprite(0, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(45, 0 ,45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(90, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(135, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(180, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(225, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(0, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(45, 0 ,45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(90, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(135, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(180, 0, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(225, 0, 45, 32)","self.attackwintersballad_spritesheet.get_sprite(0, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(32, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(64, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(96, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(128, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(160, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(0, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(32, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(64, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(96, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(128, 32, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(160, 32, 32, 45)","self.attackwintersballad_spritesheet.get_sprite(0, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(45, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(90, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(135, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(180, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(225, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(0, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(45, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(90, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(135, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(180, 77, 45, 32)",
                           "self.attackwintersballad_spritesheet.get_sprite(225, 77, 45, 32)","self.attackwintersballad_spritesheet.get_sprite(0, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(32, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(64, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(96, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(128, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(160, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(0, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(32, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(64, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(96, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(128, 109, 32, 45)",
                           "self.attackwintersballad_spritesheet.get_sprite(160, 109, 32, 45)",)
    IDpos = ("self.player.rect.x - (TILESIZE+20)",
        "self.player.rect.y",
        "self.player.rect.x",
        "self.player.rect.y + TILESIZE + 20",
        "self.player.rect.x + TILESIZE +20",
        "self.player.rect.y",
        "self.player.rect.x",
        "self..player.rect.y - (TILESIZE+20)",)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = WintersBallad
        self.image = self.game.weapon4_spritesheet.get_sprite(4,4,16,43)
        self.image.set_colorkey(BLACK)
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 6

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.rightattack_scythe = [self.game.attackwintersballad_spritesheet.get_sprite(0, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(45, 0 ,45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(90, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(135, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(180, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(225, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(0, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(45, 0 ,45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(90, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(135, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(180, 0, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(225, 0, 45, 32),]

        self.downattack_scythe = [self.game.attackwintersballad_spritesheet.get_sprite(0, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(32, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(64, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(96, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(128, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(160, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(0, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(32, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(64, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(96, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(128, 32, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(160, 32, 32, 45),]

        self.leftattack_scythe = [self.game.attackwintersballad_spritesheet.get_sprite(0, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(45, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(90, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(135, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(180, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(225, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(0, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(45, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(90, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(135, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(180, 77, 45, 32),
                           self.game.attackwintersballad_spritesheet.get_sprite(225, 77, 45, 32),]

        self.upattack_scythe = [self.game.attackwintersballad_spritesheet.get_sprite(0, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(32, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(64, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(96, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(128, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(160, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(0, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(32, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(64, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(96, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(128, 109, 32, 45),
                           self.game.attackwintersballad_spritesheet.get_sprite(160, 109, 32, 45),]
        self.scythe_x_left = self.game.player.rect.x - (TILESIZE+20)
        self.scythe_y_left = self.game.player.rect.y 
        self.scythe_x_down = self.game.player.rect.x 
        self.scythe_y_down = self.game.player.rect.y + TILESIZE + 20
        self.scythe_x_right = self.game.player.rect.x + TILESIZE +20
        self.scythe_y_right = self.game.player.rect.y 
        self.scythe_x_up = self.game.player.rect.x
        self.scythe_y_up = self.game.player.rect.y - (TILESIZE+20)
        self.animation_number = 12


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.epee.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = WintersBallad
                    self.game.player.widthattack = 45
                    self.game.player.heightattack = 32
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.rightattack_scythe
                    self.game.player.downattack_animations = self.downattack_scythe 
                    self.game.player.leftattack_animations = self.leftattack_scythe
                    self.game.player.upattack_animations = self.upattack_scythe
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()     
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class SnakeSword(pygame.sprite.Sprite):
    nom = "SnakeSword"
    attribut = "Puissance : +15"
    IDimage = "self.weapon3_spritesheet.get_sprite(129,38,13,45)"
    IDattack = ("self.attacksnakesword_spritesheet.get_sprite(0, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(110, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(220, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(330, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(440, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(550, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(660, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(770, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(880, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(990, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1100, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1210, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1320, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1430, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1540, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1650, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1760, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1870, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1980, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(2090, 0, 110, 110)","self.attacksnakesword_spritesheet.get_sprite(0, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(110, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(220, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(330, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(440, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(550, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(660, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(770, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(880, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(990, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1100, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1210, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1320, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1430, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1540, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1650, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1760, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1870, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1980, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(2090, 0, 110, 110)","self.attacksnakesword_spritesheet.get_sprite(0, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(110, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(220, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(330, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(440, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(550, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(660, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(770, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(880, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(990, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1100, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1210, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1320, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1430, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1540, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1650, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1760, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1870, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1980, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(2090, 0, 110, 110)","self.attacksnakesword_spritesheet.get_sprite(0, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(110, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(220, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(330, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(440, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(550, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(660, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(770, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(880, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(990, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1100, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1210, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1320, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1430, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1540, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1650, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1760, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1870, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(1980, 0, 110, 110)",
                                            "self.attacksnakesword_spritesheet.get_sprite(2090, 0, 110, 110)",)
    IDpos = ("self.player.rect.x - ((TILESIZE*2)+16)",
        "self.player.rect.y - TILESIZE",
        "self.player.rect.x - TILESIZE",
        "self.player.rect.y + (TILESIZE-10)",
        "self.player.rect.x + TILESIZE/2",
        "self.player.rect.y - TILESIZE",
        "self.player.rect.x - TILESIZE",
        "self.player.rect.y - ((TILESIZE*2)+20)",)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = SnakeSword
        self.image = self.game.weapon3_spritesheet.get_sprite(129,38,13,45)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 15

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)
        self.snakeswordspriteanimation = [self.game.attacksnakesword_spritesheet.get_sprite(0, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(110, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(220, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(330, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(440, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(550, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(660, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(770, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(880, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(990, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1100, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1210, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1320, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1430, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1540, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1650, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1760, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1870, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(1980, 0, 110, 110),
                                            self.game.attacksnakesword_spritesheet.get_sprite(2090, 0, 110, 110),]
        self.rightattack_snakesword = self.snakeswordspriteanimation
        self.downattack_snakesword = self.snakeswordspriteanimation
        self.leftattack_snakesword = self.snakeswordspriteanimation
        self.upattack_snakesword = self.snakeswordspriteanimation

        self.snakesword_x_left = self.game.player.rect.x - ((TILESIZE*2)+16)
        self.snakesword_y_left = self.game.player.rect.y - TILESIZE
        self.snakesword_x_down = self.game.player.rect.x - TILESIZE
        self.snakesword_y_down = self.game.player.rect.y + (TILESIZE-10)
        self.snakesword_x_right = self.game.player.rect.x + TILESIZE/2
        self.snakesword_y_right = self.game.player.rect.y - TILESIZE
        self.snakesword_x_up = self.game.player.rect.x - TILESIZE
        self.snakesword_y_up = self.game.player.rect.y - ((TILESIZE*2)+20)

        self.animation_number = 20

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.epee.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut

            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = SnakeSword
                    self.game.player.widthattack = 110
                    self.game.player.heightattack = 110
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.rightattack_snakesword
                    self.game.player.downattack_animations = self.downattack_snakesword 
                    self.game.player.leftattack_animations = self.leftattack_snakesword
                    self.game.player.upattack_animations = self.upattack_snakesword
                    self.game.player.arme_x_up = self.snakesword_x_up
                    self.game.player.arme_y_up = self.snakesword_y_up
                    self.game.player.arme_x_down = self.snakesword_x_down
                    self.game.player.arme_y_down = self.snakesword_y_down
                    self.game.player.arme_x_left = self.snakesword_x_left
                    self.game.player.arme_y_left = self.snakesword_y_left
                    self.game.player.arme_x_right = self.snakesword_x_right
                    self.game.player.arme_y_right = self.snakesword_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class GreatSword(pygame.sprite.Sprite):
    nom = "GreatSword"
    attribut = "Puissance : +12"
    IDimage = "self.weapon3_spritesheet.get_sprite(46,85,22,49)"
    IDattack = ("self.attackgreatsword_spritesheet.get_sprite(0, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(110, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(220, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(330, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(440, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(550, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(660, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(770, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(880, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(990, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1100, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1210, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1320, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1430, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1540, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1650, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1760, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1870, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1980, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(2090, 0, 110, 110)","self.attackgreatsword_spritesheet.get_sprite(0, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(110, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(220, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(330, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(440, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(550, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(660, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(770, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(880, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(990, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1100, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1210, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1320, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1430, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1540, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1650, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1760, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1870, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1980, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(2090, 0, 110, 110)","self.attackgreatsword_spritesheet.get_sprite(0, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(110, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(220, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(330, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(440, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(550, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(660, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(770, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(880, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(990, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1100, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1210, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1320, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1430, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1540, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1650, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1760, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1870, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1980, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(2090, 0, 110, 110)","self.attackgreatsword_spritesheet.get_sprite(0, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(110, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(220, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(330, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(440, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(550, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(660, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(770, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(880, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(990, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1100, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1210, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1320, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1430, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1540, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1650, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1760, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1870, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(1980, 0, 110, 110)",
                                    "self.attackgreatsword_spritesheet.get_sprite(2090, 0, 110, 110)",)
    
    IDpos = ("self.player.rect.x - ((TILESIZE*2)+16)",
                "self.player.rect.y - TILESIZE",
                "self.player.rect.x - TILESIZE",
                "self.player.rect.y + (TILESIZE-10)",
                "self.player.rect.x + TILESIZE/2",
                "self.player.rect.y - TILESIZE",
                "self.player.rect.x - TILESIZE",
                "self.player.rect.y - ((TILESIZE*2)+20)",)
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = SnakeSword
        self.image = self.game.weapon3_spritesheet.get_sprite(46,85,22,49)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 12

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)
        self.greatswordspriteanimation = [self.game.attackgreatsword_spritesheet.get_sprite(0, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(110, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(220, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(330, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(440, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(550, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(660, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(770, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(880, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(990, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1100, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1210, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1320, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1430, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1540, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1650, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1760, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1870, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(1980, 0, 110, 110),
                                    self.game.attackgreatsword_spritesheet.get_sprite(2090, 0, 110, 110),]
        self.rightattack_snakesword = self.greatswordspriteanimation
        self.downattack_snakesword = self.greatswordspriteanimation
        self.leftattack_snakesword = self.greatswordspriteanimation
        self.upattack_snakesword = self.greatswordspriteanimation

        self.snakesword_x_left = self.game.player.rect.x - ((TILESIZE*2)+16)
        self.snakesword_y_left = self.game.player.rect.y - TILESIZE
        self.snakesword_x_down = self.game.player.rect.x - TILESIZE
        self.snakesword_y_down = self.game.player.rect.y + (TILESIZE-10)
        self.snakesword_x_right = self.game.player.rect.x + TILESIZE/2
        self.snakesword_y_right = self.game.player.rect.y - TILESIZE
        self.snakesword_x_up = self.game.player.rect.x - TILESIZE
        self.snakesword_y_up = self.game.player.rect.y - ((TILESIZE*2)+20)

        self.animation_number = 20

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.epee.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut

            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = GreatSword
                    self.game.player.widthattack = 110
                    self.game.player.heightattack = 110
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.rightattack_snakesword
                    self.game.player.downattack_animations = self.downattack_snakesword 
                    self.game.player.leftattack_animations = self.leftattack_snakesword
                    self.game.player.upattack_animations = self.upattack_snakesword
                    self.game.player.arme_x_up = self.snakesword_x_up
                    self.game.player.arme_y_up = self.snakesword_y_up
                    self.game.player.arme_x_down = self.snakesword_x_down
                    self.game.player.arme_y_down = self.snakesword_y_down
                    self.game.player.arme_x_left = self.snakesword_x_left
                    self.game.player.arme_y_left = self.snakesword_y_left
                    self.game.player.arme_x_right = self.snakesword_x_right
                    self.game.player.arme_y_right = self.snakesword_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Helmet_leather(pygame.sprite.Sprite):
    nom = "Leather Helmet"
    attribut = "Max health : +1 / Vision : +75"
    IDimage = (37,35,24,26)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Helmet_leather
        self.image = self.game.armor_spritesheet.get_sprite(37,35,24,26)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.addhealth = 1
        self.vision = 200
        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.helmet.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.helmet.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.helmet.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 

            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.helmet.ID != None:
                        helmet_instance = self.game.player.helmet.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.light.kill()
                    self.game.player.light = None
                    self.game.player.light = Light(self.game,self.game.player.x,self.game.player.y,self.vision,(255,167,38,40))
                    self.game.player.helmet.ID = Helmet_leather
                    self.game.player.helmet.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Helmet_chainmail(pygame.sprite.Sprite):
    nom = "Chainmail Helmet"
    attribut = "Max health : +2 / Vision : +25"
    IDimage = (35,96,27,32)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Helmet_chainmail
        self.image = self.game.armor_spritesheet.get_sprite(35,96,27,32)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.addhealth = 2
        self.vision = 150

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.helmet.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.helmet.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.helmet.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 

            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.helmet.ID != None:
                        helmet_instance = self.game.player.helmet.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.light.kill()
                    self.game.player.light = None
                    self.game.player.light = Light(self.game,self.game.player.x,self.game.player.y,self.vision,(255,167,38,25))
                    self.game.player.helmet.ID = Helmet_chainmail
                    self.game.player.helmet.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Helmet_iron(pygame.sprite.Sprite):
    nom = "Iron Helmet"
    attribut = "Max health : +3 / Vision : -25"
    IDimage = (37,129,23,30)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Helmet_iron
        self.image = self.game.armor_spritesheet.get_sprite(37,129,23,30)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.addhealth = 3
        self.vision = 100
        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.helmet.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.helmet.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.helmet.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 

            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.helmet.ID != None:
                        helmet_instance = self.game.player.helmet.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.light.kill()
                    self.game.player.light = None
                    self.game.player.light = Light(self.game,self.game.player.x,self.game.player.y,self.vision,(255,255,255,65))
                    self.game.player.helmet.ID = Helmet_iron
                    self.game.player.helmet.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Helmet_Lava(pygame.sprite.Sprite):
    nom = "Lava Helmet"
    attribut = "Max health : +5 / Vision : 500"
    IDimage = (37,129,23,30)
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Helmet_Lava
        self.image = self.game.lavaequipement_spritesheet.get_sprite(416,0,32,32)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.addhealth = 5
        self.vision = 500
        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.helmet.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.helmet.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.helmet.ID.attribut
                 

            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:   
                    if self.game.player.helmet.ID != None:
                        helmet_instance = self.game.player.helmet.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.light.kill()
                    self.game.player.light = None
                    self.game.player.light = Light(self.game,self.game.player.x,self.game.player.y,self.vision,(255,0,0,25))
                    self.game.player.helmet.ID = Helmet_Lava
                    self.game.player.helmet.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Pants_leather(pygame.sprite.Sprite):
    nom = "Leather Pants"
    attribut = "Max health : +2"
    IDimage = (97,34,31,28)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Pants_leather
        self.image = self.game.armor_spritesheet.get_sprite(97,34,31,28)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.addhealth = 2

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.pants.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.pants.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.pants.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.pants.ID != None:
                        helmet_instance = self.game.player.pants.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.pants.ID = Pants_leather
                    self.game.player.pants.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Pants_chainmail(pygame.sprite.Sprite):
    nom = "Chainmail Pants"
    attribut = "Max health : +3"
    IDimage = (96,96,32,32)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Pants_chainmail
        self.image = self.game.armor_spritesheet.get_sprite(96,96,32,32)
        self.addhealth = 3
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.pants.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.pants.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.pants.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.pants.ID != None:
                        helmet_instance = self.game.player.pants.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.pants.ID = Pants_chainmail
                    self.game.player.pants.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Pants_iron(pygame.sprite.Sprite):
    nom = "Iron Pants"
    attribut = "Max health : +4"
    IDimage = (96,131,32,27)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Pants_iron
        self.image = self.game.armor_spritesheet.get_sprite(96,131,32,27)
        self.addhealth = 4
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.pants.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.pants.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.pants.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.pants.ID != None:
                        helmet_instance = self.game.player.pants.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.pants.ID = Pants_iron
                    self.game.player.pants.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Pants_Lava(pygame.sprite.Sprite):
    nom = "Lava Pants"
    attribut = "Max health : +10"
    IDimage = (96,131,32,27)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Pants_Lava
        self.image = self.game.lavaequipement_spritesheet.get_sprite(480,0,32,32)
        self.addhealth = 10
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.pants.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.pants.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.pants.ID.attribut
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.pants.ID != None:
                        helmet_instance = self.game.player.pants.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.pants.ID = Pants_Lava
                    self.game.player.pants.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Chest_leather(pygame.sprite.Sprite):
    nom = "Leather Chest"
    attribut = "Max health : +3"
    IDimage = (65,33,30,30)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Chest_leather
        self.image = self.game.armor_spritesheet.get_sprite(65,33,30,30)
        self.addhealth = 3
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.chest.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.chest.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.chest.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.chest.ID != None:
                        helmet_instance = self.game.player.chest.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.chest.ID = Chest_leather
                    self.game.player.chest.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Chest_chainmail(pygame.sprite.Sprite):
    nom = "Chainmail Chest"
    attribut = "Max health : +4"
    IDimage = (66,97,30,30)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Chest_chainmail
        self.image = self.game.armor_spritesheet.get_sprite(66,97,30,30)
        self.addhealth = 4
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.chest.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.chest.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.chest.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.chest.ID != None:
                        helmet_instance = self.game.player.chest.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.chest.ID = Chest_chainmail
                    self.game.player.chest.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Chest_iron(pygame.sprite.Sprite):
    nom = "Iron Chest"
    attribut = "Max health : +5"
    IDimage = (67,128,25,32)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Chest_iron
        self.image = self.game.armor_spritesheet.get_sprite(67,128,25,32)
        self.addhealth = 5
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.chest.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.chest.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.chest.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.chest.ID != None:
                        helmet_instance = self.game.player.chest.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.chest.ID = Chest_iron
                    self.game.player.chest.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Chest_Lava(pygame.sprite.Sprite):
    nom = "Lava Chest"
    attribut = "Max health : +15"
    IDimage = (67,128,25,32)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Chest_Lava
        self.image = self.game.lavaequipement_spritesheet.get_sprite(448,0,32,32)
        self.addhealth = 15
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.chest.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.chest.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.chest.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.chest.ID != None:
                        helmet_instance = self.game.player.chest.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= helmet_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.chest.ID = Chest_Lava
                    self.game.player.chest.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Boots_leather(pygame.sprite.Sprite):
    nom = "Leather Boots"
    attribut = "Max health : +1"
    attribut1 = "Speed : x1.2"
    IDimage = (130,33,27,30)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Boots_leather
        self.image = self.game.armor_spritesheet.get_sprite(130,33,27,30)
        self.addhealth = 1
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.vitesse = 1.2

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.boots.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.boots.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.boots.ID.attribut
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.boots.ID != None:
                        boots_instance = self.game.player.boots.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= boots_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.vitesse3 = self.vitesse
                    self.game.player.boots.ID = Boots_leather
                    self.game.player.boots.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Boots_chainmail(pygame.sprite.Sprite):
    nom = "Chainmail Boots"
    attribut = "Max health : +2"
    attribut1 = "Speed : x1"
    IDimage = (131,96,26,32)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Boots_chainmail
        self.image = self.game.armor_spritesheet.get_sprite(131,96,26,32)
        self.addhealth = 3
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                if (self.game.player.boots.ID != None):
                    self.game.player.afficheequipped.trueorfalse = True
                    self.game.player.afficheequipped.nom = self.game.player.boots.ID.nom
                    self.game.player.afficheequipped.attribut1 = self.game.player.boots.ID.attribut
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.boots.ID != None:
                        boots_instance = self.game.player.boots.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= boots_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.boots.ID = Boots_chainmail
                    self.game.player.boots.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Boots_iron(pygame.sprite.Sprite):
    nom = "Iron Boots"
    attribut = "Max health : +3"
    attribut1 = "Speed : x0.8"
    IDimage = (130,129,28,31)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Boots_iron
        self.image = self.game.armor_spritesheet.get_sprite(130,129,28,31)
        self.addhealth = 3
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.vitesse = 0.8

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.boots.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.boots.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.boots.ID.attribut
                self.game.player.afficheequipped.attribut2 = self.game.player.boots.ID.attribut1
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.boots.ID != None:
                        boots_instance = self.game.player.boots.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= boots_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.vitesse3 = self.vitesse
                    self.game.player.boots.ID = Boots_iron
                    self.game.player.boots.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Boots_Lava(pygame.sprite.Sprite):
    nom = "Lava Boots"
    attribut = "Max health : +5"
    attribut1 = "Speed : x1.4"
    IDimage = (544,0,32,32)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Boots_Lava
        self.image = self.game.lavaequipement_spritesheet.get_sprite(544,0,32,32)
        self.addhealth = 5
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.vitesse = 1.4

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
                self.game.player.afficheitem.attribut2 = self.attribut1
            if (hits) and (self.game.player.boots.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.boots.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.boots.ID.attribut
                self.game.player.afficheequipped.attribut2 = self.game.player.boots.ID.attribut1
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.boots.ID != None:
                        boots_instance = self.game.player.boots.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.healthbar.maxhealth -= boots_instance.addhealth
                    self.game.player.healthbar.maxhealth += self.addhealth
                    self.game.player.vitesse3 = self.vitesse
                    self.game.player.boots.ID = Boots_Lava
                    self.game.player.boots.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Necklace_copper(pygame.sprite.Sprite):
    nom = "Necklace Copper"
    attribut = "Il est cassé"
    IDimage = (193,129,28,31)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Necklace_copper
        self.image = self.game.armor_spritesheet.get_sprite(193,129,28,31)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.puissance = 0

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
        keys = pygame.key.get_pressed()
        if hits:
            self.game.player.afficheitem.trueorfalse = True
            self.game.player.afficheitem.nom = self.nom
            self.game.player.afficheitem.attribut1 = self.attribut
        if (hits) and (self.game.player.necklace.ID != None):
            self.game.player.afficheequipped.trueorfalse = True
            self.game.player.afficheequipped.nom = self.game.player.necklace.ID.nom
            self.game.player.afficheequipped.attribut1 = self.game.player.necklace.ID.attribut
        if not hits:
            self.game.player.afficheitem.trueorfalse = False
            self.game.player.afficheequipped.trueorfalse = False
                
        if hits and keys[pygame.K_e]:
            if self.game.player.take_timer() == False:
                if self.game.player.necklace.ID != None:
                    necklace_instance = self.game.player.necklace.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                    self.game.player.puissance -= necklace_instance.puissance
                self.game.player.necklace.ID = Necklace_copper
                self.game.player.necklace.image = self.image
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                self.kill()
                self.game.player.lasttaketimer = pygame.time.get_ticks()

class Necklace_rubis(pygame.sprite.Sprite):
    nom = "Necklace Rubis"
    attribut = "+2 de puissance"
    IDimage = (227,129,28,31)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Necklace_rubis
        self.image = self.game.armor_spritesheet.get_sprite(227,129,28,31)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.puissance = 2

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.necklace.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.necklace.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.necklace.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                 
            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.necklace.ID != None:
                        necklace_instance = self.game.player.necklace.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= necklace_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.necklace.ID = Necklace_rubis
                    self.game.player.necklace.image = self.image
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Necklace_saphir(pygame.sprite.Sprite):
    nom = "Necklace Saphir"
    attribut = "+300 ms invulnérabilité"
    IDimage = (157,129,29,30)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Necklace_saphir
        self.image = self.game.armor_spritesheet.get_sprite(321,129,29,30)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.puissance = 0

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
        keys = pygame.key.get_pressed()
        if hits:
            self.game.player.afficheitem.trueorfalse = True
            self.game.player.afficheitem.nom = self.nom
            self.game.player.afficheitem.attribut1 = self.attribut
        if (hits) and (self.game.player.necklace.ID != None):
            self.game.player.afficheequipped.trueorfalse = True
            self.game.player.afficheequipped.nom = self.game.player.necklace.ID.nom
            self.game.player.afficheequipped.attribut1 = self.game.player.necklace.ID.attribut
        if not hits:
            self.game.player.afficheitem.trueorfalse = False
            self.game.player.afficheequipped.trueorfalse = False
                
        if hits and keys[pygame.K_e]:
            if self.game.player.take_timer() == False:
                if self.game.player.necklace.ID != None:
                    necklace_instance = self.game.player.necklace.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                    self.game.player.puissance -= necklace_instance.puissance
                self.game.player.necklace.ID = Necklace_saphir
                self.game.player.necklace.image = self.image
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                self.kill()
                self.game.player.lasttaketimer = pygame.time.get_ticks()

class Necklace_emerald(pygame.sprite.Sprite):
    nom = "Necklace Emerald"
    attribut = "+1 PV toutes les 30 sec"
    IDimage = (289,129,30,30)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Necklace_emerald
        self.image = self.game.armor_spritesheet.get_sprite(289,129,30,30)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.puissance = 0

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
        keys = pygame.key.get_pressed()
        if hits:
            self.game.player.afficheitem.trueorfalse = True
            self.game.player.afficheitem.nom = self.nom
            self.game.player.afficheitem.attribut1 = self.attribut
        if (hits) and (self.game.player.necklace.ID != None):
            self.game.player.afficheequipped.trueorfalse = True
            self.game.player.afficheequipped.nom = self.game.player.necklace.ID.nom
            self.game.player.afficheequipped.attribut1 = self.game.player.necklace.ID.attribut
        if not hits:
            self.game.player.afficheitem.trueorfalse = False
            self.game.player.afficheequipped.trueorfalse = False
                
        if hits and keys[pygame.K_e]:
            if self.game.player.take_timer() == False:
                if self.game.player.necklace.ID != None:
                    necklace_instance = self.game.player.necklace.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                    self.game.player.puissance -= necklace_instance.puissance
                self.game.player.necklace.ID = Necklace_emerald
                self.game.player.necklace.image = self.image
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                self.kill()
                self.game.player.lasttaketimer = pygame.time.get_ticks()

class Ring_copper(pygame.sprite.Sprite):
    nom = "Ring Copper"
    attribut = "A capout"
    IDimage = (196,104,24,17)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Ring_copper
        self.image = self.game.armor_spritesheet.get_sprite(196,104,24,17)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)
        self.puissance = 0

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
        keys = pygame.key.get_pressed()
        if hits:
            self.game.player.afficheitem.trueorfalse = True
            self.game.player.afficheitem.nom = self.nom
            self.game.player.afficheitem.attribut1 = self.attribut
        if (hits) and (self.game.player.ring.ID != None):
            self.game.player.afficheequipped.trueorfalse = True
            self.game.player.afficheequipped.nom = self.game.player.ring.ID.nom
            self.game.player.afficheequipped.attribut1 = self.game.player.ring.ID.attribut
        if not hits:
            self.game.player.afficheitem.trueorfalse = False
            self.game.player.afficheequipped.trueorfalse = False
                
        if hits and keys[pygame.K_e]:
            if self.game.player.take_timer() == False:
                if self.game.player.ring.ID != None:
                    ring_instance = self.game.player.ring.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                    self.game.player.puissance -= ring_instance.puissance
                self.game.player.ring.ID = Ring_copper
                self.game.player.ring.image = self.image
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                self.kill()
                self.game.player.lasttaketimer = pygame.time.get_ticks()

class Ring_rubis(pygame.sprite.Sprite):
    nom = "Ring Rubis"
    attribut = "+1 puissance"
    IDimage = (230,103,22,18)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Ring_rubis
        self.image = self.game.armor_spritesheet.get_sprite(230,103,22,18)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.puissance = 1


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
        keys = pygame.key.get_pressed()
        if hits:
            self.game.player.afficheitem.trueorfalse = True
            self.game.player.afficheitem.nom = self.nom
            self.game.player.afficheitem.attribut1 = self.attribut
        if (hits) and (self.game.player.ring.ID != None):
            self.game.player.afficheequipped.trueorfalse = True
            self.game.player.afficheequipped.nom = self.game.player.ring.ID.nom
            self.game.player.afficheequipped.attribut1 = self.game.player.ring.ID.attribut
        if not hits:
            self.game.player.afficheitem.trueorfalse = False
            self.game.player.afficheequipped.trueorfalse = False
                
        if hits and keys[pygame.K_e]:
            if self.game.player.take_timer() == False:
                if self.game.player.ring.ID != None:
                    ring_instance = self.game.player.ring.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                    self.game.player.puissance -= ring_instance.puissance
                self.game.player.puissance += self.puissance
                self.game.player.ring.ID = Ring_rubis
                self.game.player.ring.image = self.image
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                self.kill()
                self.game.player.lasttaketimer = pygame.time.get_ticks()

class Ring_saphir(pygame.sprite.Sprite):
    nom = "Ring Saphir"
    attribut = "+150 ms invulnérabilité"
    IDimage = (292,101,24,22)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Ring_saphir
        self.image = self.game.armor_spritesheet.get_sprite(292,101,24,22)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.puissance = 0

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
        keys = pygame.key.get_pressed()
        if hits:
            self.game.player.afficheitem.trueorfalse = True
            self.game.player.afficheitem.nom = self.nom
            self.game.player.afficheitem.attribut1 = self.attribut
        if (hits) and (self.game.player.ring.ID != None):
            self.game.player.afficheequipped.trueorfalse = True
            self.game.player.afficheequipped.nom = self.game.player.ring.ID.nom
            self.game.player.afficheequipped.attribut1 = self.game.player.ring.ID.attribut
        if not hits:
            self.game.player.afficheitem.trueorfalse = False
            self.game.player.afficheequipped.trueorfalse = False
                
        if hits and keys[pygame.K_e]:
            if self.game.player.take_timer() == False:
                if self.game.player.ring.ID != None:
                    ring_instance = self.game.player.ring.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                    self.game.player.puissance -= ring_instance.puissance
                self.game.player.ring.ID = Ring_saphir
                self.game.player.ring.image = self.image
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                self.kill()
                self.game.player.lasttaketimer = pygame.time.get_ticks()

class Ring_emerald(pygame.sprite.Sprite):
    nom = "Ring Emerald"
    attribut = "+1 PV toutes les 60 sec"
    IDimage = (262,103,22,19)
    def __init__(self,game, x, y):

        self.game = game
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Ring_emerald
        self.image = self.game.armor_spritesheet.get_sprite(262,103,22,19)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.puissance = 0

    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0



    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
        keys = pygame.key.get_pressed()
        if hits:
            self.game.player.afficheitem.trueorfalse = True
            self.game.player.afficheitem.nom = self.nom
            self.game.player.afficheitem.attribut1 = self.attribut
        if (hits) and (self.game.player.ring.ID != None):
            self.game.player.afficheequipped.trueorfalse = True
            self.game.player.afficheequipped.nom = self.game.player.ring.ID.nom
            self.game.player.afficheequipped.attribut1 = self.game.player.ring.ID.attribut
        if not hits:
            self.game.player.afficheitem.trueorfalse = False
            self.game.player.afficheequipped.trueorfalse = False
                
        if hits and keys[pygame.K_e]:
            if self.game.player.take_timer() == False:
                if self.game.player.ring.ID != None:
                    ring_instance = self.game.player.ring.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                    self.game.player.puissance -= ring_instance.puissance
                self.game.player.ring.ID = Ring_emerald
                self.game.player.ring.image = self.image
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False
                self.kill()
                self.game.player.lasttaketimer = pygame.time.get_ticks()

class Earth_Shatter(pygame.sprite.Sprite):
    nom = "Earth Shatter"
    attribut = "Puissance : +13 \n ça fais boum boum quand tu tapes hihihi"
    IDimage = "self.weapon2_spritesheet.get_sprite(215,4,26,68)"
    IDattack = ("self.earthshatter_spritesheet.get_sprite(0, 0, 110, 90)",
        "self.earthshatter_spritesheet.get_sprite(110, 0, 110, 90)",
        "self.earthshatter_spritesheet.get_sprite(220, 0, 110, 90)",
        "self.earthshatter_spritesheet.get_sprite(330, 0, 110, 90)","self.earthshatter_spritesheet.get_sprite(0, 90, 90, 110)",
        "self.earthshatter_spritesheet.get_sprite(90, 90, 90, 110)",
        "self.earthshatter_spritesheet.get_sprite(180, 90, 90, 110)",
        "self.earthshatter_spritesheet.get_sprite(270, 90, 90, 110)","self.earthshatter_spritesheet.get_sprite(0, 200, 110, 90)",
        "self.earthshatter_spritesheet.get_sprite(110, 200, 110, 90)",
        "self.earthshatter_spritesheet.get_sprite(220, 200, 110, 90)",
        "self.earthshatter_spritesheet.get_sprite(330, 200, 110, 90)","self.earthshatter_spritesheet.get_sprite(0, 290, 90, 110)",
        "self.earthshatter_spritesheet.get_sprite(90, 290, 90, 110)",
        "self.earthshatter_spritesheet.get_sprite(180, 290, 90, 110)",
        "self.earthshatter_spritesheet.get_sprite(270, 290, 90, 110)")
    
    IDpos = (
        "self.player.rect.x - (TILESIZE+30)",
        "self.player.rect.y - (TILESIZE/2)+10",
        "self.player.rect.x - (TILESIZE/2)+10",
        "self.player.rect.y + TILESIZE",
        "self.player.rect.x + TILESIZE",
        "self.player.rect.y - (TILESIZE/2)",
        "self.player.rect.x - (TILESIZE/2)+10",
        "self.player.rect.y - (TILESIZE+30)"
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Earth_Shatter
        self.image = self.game.weapon2_spritesheet.get_sprite(215,4,26,68)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 13

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.right_attacksanimation = [self.game.earthshatter_spritesheet.get_sprite(0, 0, 110, 90),
        self.game.earthshatter_spritesheet.get_sprite(110, 0, 110, 90),
        self.game.earthshatter_spritesheet.get_sprite(220, 0, 110, 90),
        self.game.earthshatter_spritesheet.get_sprite(330, 0, 110, 90),]

        self.down_attacksanimation = [self.game.earthshatter_spritesheet.get_sprite(0, 90, 90, 110),
        self.game.earthshatter_spritesheet.get_sprite(90, 90, 90, 110),
        self.game.earthshatter_spritesheet.get_sprite(180, 90, 90, 110),
        self.game.earthshatter_spritesheet.get_sprite(270, 90, 90, 110),]

        self.left_attacksanimation = [self.game.earthshatter_spritesheet.get_sprite(0, 200, 110, 90),
        self.game.earthshatter_spritesheet.get_sprite(110, 200, 110, 90),
        self.game.earthshatter_spritesheet.get_sprite(220, 200, 110, 90),
        self.game.earthshatter_spritesheet.get_sprite(330, 200, 110, 90),]

        self.up_attacksanimation = [self.game.earthshatter_spritesheet.get_sprite(0, 290, 90, 110),
        self.game.earthshatter_spritesheet.get_sprite(90, 290, 90, 110),
        self.game.earthshatter_spritesheet.get_sprite(180, 290, 90, 110),
        self.game.earthshatter_spritesheet.get_sprite(270, 290, 90, 110),]


        self.scythe_x_left = self.game.player.rect.x - (TILESIZE+30)
        self.scythe_y_left = self.game.player.rect.y - (TILESIZE/2)+10
        self.scythe_x_down = self.game.player.rect.x - (TILESIZE/2)+10
        self.scythe_y_down = self.game.player.rect.y + TILESIZE
        self.scythe_x_right = self.game.player.rect.x + TILESIZE
        self.scythe_y_right = self.game.player.rect.y - (TILESIZE/2)
        self.scythe_x_up = self.game.player.rect.x - (TILESIZE/2)+10
        self.scythe_y_up = self.game.player.rect.y - (TILESIZE+30)
        self.animation_number = 4


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Earth_Shatter
                    self.game.player.widthattack = 60
                    self.game.player.heightattack = 50
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.right_attacksanimation
                    self.game.player.downattack_animations = self.down_attacksanimation
                    self.game.player.leftattack_animations = self.left_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Supernova_Scepter(pygame.sprite.Sprite):
    nom = "Supernova Scepter, \n The Celestial Voidcleaver, \n Annihilator of All Realms."
    attribut = "Puissance : ?????"
    IDimage = "self.weapon4_spritesheet.get_sprite(103,4,18,44)"
    IDattack = ("self.novascepter_spritesheet.get_sprite(0, 0, 256, 256)","self.novascepter_spritesheet.get_sprite(256, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*2, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*3, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*4, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*5, 0, 256, 256)","self.novascepter_spritesheet.get_sprite(0, 0, 256, 256)","self.novascepter_spritesheet.get_sprite(256, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*2, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*3, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*4, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*5, 0, 256, 256)","self.novascepter_spritesheet.get_sprite(0, 0, 256, 256)","self.novascepter_spritesheet.get_sprite(256, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*2, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*3, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*4, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*5, 0, 256, 256)","self.novascepter_spritesheet.get_sprite(0, 0, 256, 256)","self.novascepter_spritesheet.get_sprite(256, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*2, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*3, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*4, 0, 256, 256)",
                                  "self.novascepter_spritesheet.get_sprite(256*5, 0, 256, 256)")
    
    IDpos = (
        "self.player.rect.x - (TILESIZE+20) - 250",
        "self.player.rect.y - (TILESIZE/2) - 100",
        "self.player.rect.x - (TILESIZE/2) - 100",
        "self.player.rect.y + TILESIZE + 50",
        "self.player.rect.x + TILESIZE + 50",
        "self.player.rect.y - (TILESIZE/2) - 100",
        "self.player.rect.x - (TILESIZE/2) - 100",
        "self.player.rect.y - (TILESIZE+20) - 250"
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Supernova_Scepter
        self.image = self.game.weapon4_spritesheet.get_sprite(103,4,18,44)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 9999

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.novascepterattack = [self.game.novascepter_spritesheet.get_sprite(0, 0, 256, 256),
                                  self.game.novascepter_spritesheet.get_sprite(256, 0, 256, 256),
                                  self.game.novascepter_spritesheet.get_sprite(256*2, 0, 256, 256),
                                  self.game.novascepter_spritesheet.get_sprite(256*3, 0, 256, 256),
                                  self.game.novascepter_spritesheet.get_sprite(256*4, 0, 256, 256),
                                  self.game.novascepter_spritesheet.get_sprite(256*5, 0, 256, 256)]

        self.right_attacksanimation = self.novascepterattack

        self.down_attacksanimation = self.novascepterattack

        self.left_attacksanimation = self.novascepterattack

        self.up_attacksanimation = self.novascepterattack


        self.scythe_x_left = self.game.player.rect.x - (TILESIZE+20) - 250
        self.scythe_y_left = self.game.player.rect.y - (TILESIZE/2) - 100
        self.scythe_x_down = self.game.player.rect.x - (TILESIZE/2) - 100
        self.scythe_y_down = self.game.player.rect.y + TILESIZE + 50
        self.scythe_x_right = self.game.player.rect.x + TILESIZE + 50
        self.scythe_y_right = self.game.player.rect.y - (TILESIZE/2) - 100
        self.scythe_x_up = self.game.player.rect.x - (TILESIZE/2) - 100
        self.scythe_y_up = self.game.player.rect.y - (TILESIZE+20) - 250
        self.animation_number = 6


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Supernova_Scepter
                    self.game.player.widthattack = 256
                    self.game.player.heightattack = 256
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.right_attacksanimation
                    self.game.player.downattack_animations = self.down_attacksanimation
                    self.game.player.leftattack_animations = self.left_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks()

class Flamestrike_Mallet(pygame.sprite.Sprite):
    nom = "Flamestrike Mallet"
    attribut = "Puissance : 10"
    IDimage = "self.weapon_spritesheet.get_sprite(198,0,42,57)"
    IDattack = ("self.impactblue_spritesheet.get_sprite(0, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*2, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*3, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*4, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*5, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*6, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*7, 1088, 64, 64)","self.impactblue_spritesheet.get_sprite(0, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*2, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*3, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*4, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*5, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*6, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*7, 1088, 64, 64)","self.impactblue_spritesheet.get_sprite(0, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*2, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*3, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*4, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*5, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*6, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*7, 1088, 64, 64)","self.impactblue_spritesheet.get_sprite(0, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*2, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*3, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*4, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*5, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*6, 1088, 64, 64)",
                                  "self.impactblue_spritesheet.get_sprite(64*7, 1088, 64, 64)")
    IDpos = (
        "self.player.rect.x - 62",
        "self.player.rect.y - 32",
        "self.player.rect.x - 15",
        "self.player.rect.y + 35",
        "self.player.rect.x + 30",
        "self.player.rect.y - 32",
        "self.player.rect.x - 15",
        "self.player.rect.y - 80"
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Flamestrike_Mallet
        self.image = self.game.weapon_spritesheet.get_sprite(198,0,42,57)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 10

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.Flamestrike_Mallet_Attack = [self.game.impactblue_spritesheet.get_sprite(0, 1088, 64, 64),
                                  self.game.impactblue_spritesheet.get_sprite(64, 1088, 64, 64),
                                  self.game.impactblue_spritesheet.get_sprite(64*2, 1088, 64, 64),
                                  self.game.impactblue_spritesheet.get_sprite(64*3, 1088, 64, 64),
                                  self.game.impactblue_spritesheet.get_sprite(64*4, 1088, 64, 64),
                                  self.game.impactblue_spritesheet.get_sprite(64*5, 1088, 64, 64),
                                  self.game.impactblue_spritesheet.get_sprite(64*6, 1088, 64, 64),
                                  self.game.impactblue_spritesheet.get_sprite(64*7, 1088, 64, 64)]

        self.right_attacksanimation = self.Flamestrike_Mallet_Attack

        self.down_attacksanimation = self.Flamestrike_Mallet_Attack

        self.left_attacksanimation = self.Flamestrike_Mallet_Attack

        self.up_attacksanimation = self.Flamestrike_Mallet_Attack


        self.scythe_x_left = self.game.player.rect.x - 62
        self.scythe_y_left = self.game.player.rect.y - 32
        self.scythe_x_down = self.game.player.rect.x - 15
        self.scythe_y_down = self.game.player.rect.y + 35
        self.scythe_x_right = self.game.player.rect.x + 30
        self.scythe_y_right = self.game.player.rect.y - 32
        self.scythe_x_up = self.game.player.rect.x - 15
        self.scythe_y_up = self.game.player.rect.y - 80
        self.animation_number = 6


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Flamestrike_Mallet
                    self.game.player.widthattack = 64
                    self.game.player.heightattack = 64
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.right_attacksanimation
                    self.game.player.downattack_animations = self.down_attacksanimation
                    self.game.player.leftattack_animations = self.left_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks() 

class Crimson_Blade(pygame.sprite.Sprite):
    nom = "Crimson Blade"
    attribut = "Puissance : 7"
    IDimage = "self.weapon3_spritesheet.get_sprite(116,102,13,31)"
    IDattack = ("self.bloodslash_spritesheet.get_sprite(0, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(24, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(48, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(72, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(96, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(120, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(144, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(168, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(192, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(216, 24, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(0, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(64, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(128, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(192, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(256, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(320, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(384, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(448, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(512, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(576, 88, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(0, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(24, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(48, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(72, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(96, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(120, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(144, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(168, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(192, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(216, 112, 24, 64)",
"self.bloodslash_spritesheet.get_sprite(0, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(64, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(128, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(192, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(256, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(320, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(384, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(448, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(512, 0, 64, 24)",
"self.bloodslash_spritesheet.get_sprite(576, 0, 64, 24)",)
    IDpos = (
        "self.player.rect.x - 30",
        "self.player.rect.y - 20",
        "self.player.rect.x - 15",
        "self.player.rect.y + 25",
        "self.player.rect.x + 30",
        "self.player.rect.y - 20",
        "self.player.rect.x - 15",
        "self.player.rect.y - 25",
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Crimson_Blade
        self.image = self.game.weapon3_spritesheet.get_sprite(116,102,13,31)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 7

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.right_attacksanimation = [self.game.bloodslash_spritesheet.get_sprite(0, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(64, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(128, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(192, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(256, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(320, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(384, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(448, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(512, 0, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(576, 0, 64, 24),]

        self.down_attacksanimation = [self.game.bloodslash_spritesheet.get_sprite(0, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(24, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(48, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(72, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(96, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(120, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(144, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(168, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(192, 24, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(216, 24, 24, 64),]

        self.left_attacksanimation = [self.game.bloodslash_spritesheet.get_sprite(0, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(64, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(128, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(192, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(256, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(320, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(384, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(448, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(512, 88, 64, 24),
self.game.bloodslash_spritesheet.get_sprite(576, 88, 64, 24),]

        self.up_attacksanimation = [self.game.bloodslash_spritesheet.get_sprite(0, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(24, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(48, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(72, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(96, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(120, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(144, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(168, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(192, 112, 24, 64),
self.game.bloodslash_spritesheet.get_sprite(216, 112, 24, 64),]


        self.scythe_x_left = self.game.player.rect.x - 30
        self.scythe_y_left = self.game.player.rect.y - 20
        self.scythe_x_down = self.game.player.rect.x - 15
        self.scythe_y_down = self.game.player.rect.y + 35
        self.scythe_x_right = self.game.player.rect.x + 35
        self.scythe_y_right = self.game.player.rect.y - 20
        self.scythe_x_up = self.game.player.rect.x - 15
        self.scythe_y_up = self.game.player.rect.y - 35
        self.animation_number = 10


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Crimson_Blade
                    self.game.player.widthattack = 64
                    self.game.player.heightattack = 24
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.down_attacksanimation
                    self.game.player.downattack_animations = self.left_attacksanimation
                    self.game.player.leftattack_animations = self.up_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks() 

class Celestial_Scepter(pygame.sprite.Sprite):
    nom = "Celestial Scepter"
    attribut = "Puissance : 3"
    IDimage = "self.weapon4_spritesheet.get_sprite(58,54,22,40)"
    IDattack = ("self.fallingstar_spritesheet.get_sprite(0, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(60, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(120, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(180, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(240, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(300, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(360, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(420, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(480, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(540, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(600, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(660, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(720, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(780, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(840, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(0, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(60, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(120, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(180, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(240, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(300, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(360, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(420, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(480, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(540, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(600, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(660, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(720, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(780, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(840, 170, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(0, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(60, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(120, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(180, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(240, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(300, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(360, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(420, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(480, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(540, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(600, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(660, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(720, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(780, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(840, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(0, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(60, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(120, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(180, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(240, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(300, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(360, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(420, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(480, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(540, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(600, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(660, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(720, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(780, 0, 60, 110)",
"self.fallingstar_spritesheet.get_sprite(840, 0, 60, 110)",)
    IDpos = (
        "self.player.rect.x - 80",
        "self.player.rect.y - 80",
        "self.player.rect.x - 15",
        "self.player.rect.y + 35",
        "self.player.rect.x + 60",
        "self.player.rect.y - 80",
        "self.player.rect.x - 15",
        "self.player.rect.y - 155",
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Celestial_Scepter
        self.image = self.game.weapon4_spritesheet.get_sprite(58,54,22,40)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 3

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.right_attacksanimation = [self.game.fallingstar_spritesheet.get_sprite(0, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(60, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(120, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(180, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(240, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(300, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(360, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(420, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(480, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(540, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(600, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(660, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(720, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(780, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(840, 0, 60, 110),]

        self.down_attacksanimation = [self.game.fallingstar_spritesheet.get_sprite(0, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(60, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(120, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(180, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(240, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(300, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(360, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(420, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(480, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(540, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(600, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(660, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(720, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(780, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(840, 170, 60, 110),]

        self.left_attacksanimation = [self.game.fallingstar_spritesheet.get_sprite(0, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(60, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(120, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(180, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(240, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(300, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(360, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(420, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(480, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(540, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(600, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(660, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(720, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(780, 170, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(840, 170, 60, 110),]

        self.up_attacksanimation = [self.game.fallingstar_spritesheet.get_sprite(0, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(60, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(120, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(180, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(240, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(300, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(360, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(420, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(480, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(540, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(600, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(660, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(720, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(780, 0, 60, 110),
self.game.fallingstar_spritesheet.get_sprite(840, 0, 60, 110),]


        self.scythe_x_left = self.game.player.rect.x - 80
        self.scythe_y_left = self.game.player.rect.y - 80
        self.scythe_x_down = self.game.player.rect.x - 15
        self.scythe_y_down = self.game.player.rect.y + 35
        self.scythe_x_right = self.game.player.rect.x + 60
        self.scythe_y_right = self.game.player.rect.y -80
        self.scythe_x_up = self.game.player.rect.x - 15
        self.scythe_y_up = self.game.player.rect.y - 155
        self.animation_number = 15


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Celestial_Scepter
                    self.game.player.widthattack = 60
                    self.game.player.heightattack = 110
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.down_attacksanimation
                    self.game.player.downattack_animations = self.left_attacksanimation
                    self.game.player.leftattack_animations = self.up_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks() 

class Nebula_GreatSword(pygame.sprite.Sprite):
    nom = "Nebula Greatsword"
    attribut = "Puissance : 5"
    IDimage = "self.weapon_spritesheet.get_sprite(148,33,16,40)"
    IDattack = ("self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32)",
"self.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32)",)
    IDpos = (
        "self.player.rect.x - 50",
        "self.player.rect.y ",
        "self.player.rect.x",
        "self.player.rect.y + 50",
        "self.player.rect.x + 50",
        "self.player.rect.y",
        "self.player.rect.x ",
        "self.player.rect.y - 50",
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Nebula_GreatSword
        self.image = self.game.weapon_spritesheet.get_sprite(148,33,16,40)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 5

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.nebulaattacks = [self.game.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(0, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(32, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(64, 0, 32, 32),
self.game.nebulaattacks_spritesheet.get_sprite(96, 0, 32, 32),]

        self.right_attacksanimation = self.nebulaattacks

        self.down_attacksanimation = self.nebulaattacks

        self.left_attacksanimation = self.nebulaattacks

        self.up_attacksanimation = self.nebulaattacks


        self.scythe_x_left = self.game.player.rect.x - 50
        self.scythe_y_left = self.game.player.rect.y 
        self.scythe_x_down = self.game.player.rect.x
        self.scythe_y_down = self.game.player.rect.y + 50
        self.scythe_x_right = self.game.player.rect.x + 50
        self.scythe_y_right = self.game.player.rect.y
        self.scythe_x_up = self.game.player.rect.x 
        self.scythe_y_up = self.game.player.rect.y - 50
        self.animation_number = 16


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Nebula_GreatSword
                    self.game.player.widthattack = 40
                    self.game.player.heightattack = 40
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.down_attacksanimation
                    self.game.player.downattack_animations = self.left_attacksanimation
                    self.game.player.leftattack_animations = self.up_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks() 

class Seraphic_Blade(pygame.sprite.Sprite):
    nom = "Seraphic Blade"
    attribut = "Puissance : 4"
    IDimage = "self.weapon_spritesheet.get_sprite(110,75,16,40)"
    IDattack = ("self.whitecircleattacks_spritesheet.get_sprite(0, 0, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(35, 0, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(70, 0, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(105, 0, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(140, 0, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(0, 32, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(32, 32, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(64, 32, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(96, 32, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(128, 32, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(0, 67, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(35, 67, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(70, 67, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(105, 67, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(140, 67, 35, 32)",
"self.whitecircleattacks_spritesheet.get_sprite(0, 99, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(32, 99, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(64, 99, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(96, 99, 32, 35)",
"self.whitecircleattacks_spritesheet.get_sprite(128, 99, 32, 35)",)
    IDpos = (
        "self.player.rect.x - 30",
        "self.player.rect.y ",
        "self.player.rect.x",
        "self.player.rect.y + 30",
        "self.player.rect.x + 30",
        "self.player.rect.y",
        "self.player.rect.x ",
        "self.player.rect.y - 30",
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Seraphic_Blade
        self.image = self.game.weapon_spritesheet.get_sprite(110,75,16,40)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 4

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.right_attacksanimation = [self.game.whitecircleattacks_spritesheet.get_sprite(0, 0, 35, 32),
self.game.whitecircleattacks_spritesheet.get_sprite(35, 0, 35, 32),
self.game.whitecircleattacks_spritesheet.get_sprite(70, 0, 35, 32),
self.game.whitecircleattacks_spritesheet.get_sprite(105, 0, 35, 32),
self.game.whitecircleattacks_spritesheet.get_sprite(140, 0, 35, 32),]

        self.down_attacksanimation = [self.game.whitecircleattacks_spritesheet.get_sprite(0, 32, 32, 35),
self.game.whitecircleattacks_spritesheet.get_sprite(32, 32, 32, 35),
self.game.whitecircleattacks_spritesheet.get_sprite(64, 32, 32, 35),
self.game.whitecircleattacks_spritesheet.get_sprite(96, 32, 32, 35),
self.game.whitecircleattacks_spritesheet.get_sprite(128, 32, 32, 35),]

        self.left_attacksanimation = [self.game.whitecircleattacks_spritesheet.get_sprite(0, 67, 35, 32),
self.game.whitecircleattacks_spritesheet.get_sprite(35, 67, 35, 32),
self.game.whitecircleattacks_spritesheet.get_sprite(70, 67, 35, 32),
self.game.whitecircleattacks_spritesheet.get_sprite(105, 67, 35, 32),
self.game.whitecircleattacks_spritesheet.get_sprite(140, 67, 35, 32),]

        self.up_attacksanimation = [self.game.whitecircleattacks_spritesheet.get_sprite(0, 99, 32, 35),
self.game.whitecircleattacks_spritesheet.get_sprite(32, 99, 32, 35),
self.game.whitecircleattacks_spritesheet.get_sprite(64, 99, 32, 35),
self.game.whitecircleattacks_spritesheet.get_sprite(96, 99, 32, 35),
self.game.whitecircleattacks_spritesheet.get_sprite(128, 99, 32, 35),]






        self.scythe_x_left = self.game.player.rect.x - 30
        self.scythe_y_left = self.game.player.rect.y 
        self.scythe_x_down = self.game.player.rect.x
        self.scythe_y_down = self.game.player.rect.y + 30
        self.scythe_x_right = self.game.player.rect.x + 30
        self.scythe_y_right = self.game.player.rect.y
        self.scythe_x_up = self.game.player.rect.x 
        self.scythe_y_up = self.game.player.rect.y - 30
        self.animation_number = 5


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Seraphic_Blade
                    self.game.player.widthattack = 40
                    self.game.player.heightattack = 40
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.down_attacksanimation
                    self.game.player.downattack_animations = self.left_attacksanimation
                    self.game.player.leftattack_animations = self.up_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks() 

class Azure_Blade(pygame.sprite.Sprite):
    nom = "Azure Blade"
    attribut = "Puissance : 4"
    IDimage = "self.weapon_spritesheet.get_sprite(146,75,16,40)"
    IDattack = ("self.bluecircleattacks_spritesheet.get_sprite(0, 0, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(35, 0, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(70, 0, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(105, 0, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(140, 0, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(0, 32, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(32, 32, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(64, 32, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(96, 32, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(128, 32, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(0, 67, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(35, 67, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(70, 67, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(105, 67, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(140, 67, 35, 32)",
"self.bluecircleattacks_spritesheet.get_sprite(0, 99, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(32, 99, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(64, 99, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(96, 99, 32, 35)",
"self.bluecircleattacks_spritesheet.get_sprite(128, 99, 32, 35)",)
    IDpos = (
        "self.player.rect.x - 30",
        "self.player.rect.y ",
        "self.player.rect.x",
        "self.player.rect.y + 30",
        "self.player.rect.x + 30",
        "self.player.rect.y",
        "self.player.rect.x ",
        "self.player.rect.y - 30",
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Seraphic_Blade
        self.image = self.game.weapon_spritesheet.get_sprite(146,75,16,40)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 4

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.right_attacksanimation = [self.game.bluecircleattacks_spritesheet.get_sprite(0, 0, 35, 32),
self.game.bluecircleattacks_spritesheet.get_sprite(35, 0, 35, 32),
self.game.bluecircleattacks_spritesheet.get_sprite(70, 0, 35, 32),
self.game.bluecircleattacks_spritesheet.get_sprite(105, 0, 35, 32),
self.game.bluecircleattacks_spritesheet.get_sprite(140, 0, 35, 32),]

        self.down_attacksanimation = [self.game.bluecircleattacks_spritesheet.get_sprite(0, 32, 32, 35),
self.game.bluecircleattacks_spritesheet.get_sprite(32, 32, 32, 35),
self.game.bluecircleattacks_spritesheet.get_sprite(64, 32, 32, 35),
self.game.bluecircleattacks_spritesheet.get_sprite(96, 32, 32, 35),
self.game.bluecircleattacks_spritesheet.get_sprite(128, 32, 32, 35),]

        self.left_attacksanimation = [self.game.bluecircleattacks_spritesheet.get_sprite(0, 67, 35, 32),
self.game.bluecircleattacks_spritesheet.get_sprite(35, 67, 35, 32),
self.game.bluecircleattacks_spritesheet.get_sprite(70, 67, 35, 32),
self.game.bluecircleattacks_spritesheet.get_sprite(105, 67, 35, 32),
self.game.bluecircleattacks_spritesheet.get_sprite(140, 67, 35, 32),]

        self.up_attacksanimation = [self.game.bluecircleattacks_spritesheet.get_sprite(0, 99, 32, 35),
self.game.bluecircleattacks_spritesheet.get_sprite(32, 99, 32, 35),
self.game.bluecircleattacks_spritesheet.get_sprite(64, 99, 32, 35),
self.game.bluecircleattacks_spritesheet.get_sprite(96, 99, 32, 35),
self.game.bluecircleattacks_spritesheet.get_sprite(128, 99, 32, 35),]






        self.scythe_x_left = self.game.player.rect.x - 30
        self.scythe_y_left = self.game.player.rect.y 
        self.scythe_x_down = self.game.player.rect.x
        self.scythe_y_down = self.game.player.rect.y + 30
        self.scythe_x_right = self.game.player.rect.x + 30
        self.scythe_y_right = self.game.player.rect.y
        self.scythe_x_up = self.game.player.rect.x 
        self.scythe_y_up = self.game.player.rect.y - 30
        self.animation_number = 5


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Azure_Blade
                    self.game.player.widthattack = 40
                    self.game.player.heightattack = 40
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.down_attacksanimation
                    self.game.player.downattack_animations = self.left_attacksanimation
                    self.game.player.leftattack_animations = self.up_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks() 

class Lustrous_Blade(pygame.sprite.Sprite):
    nom = "Lustrous Blade"
    attribut = "Puissance : 2"
    IDimage = "self.weapon_spritesheet.get_sprite(128,75,16,40)"
    IDattack = ("self.yellowcircle_spritesheet.get_sprite(0, 0, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(35, 0, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(70, 0, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(105, 0, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(140, 0, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(0, 32, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(32, 32, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(64, 32, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(96, 32, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(128, 32, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(0, 67, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(35, 67, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(70, 67, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(105, 67, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(140, 67, 35, 32)",
"self.yellowcircle_spritesheet.get_sprite(0, 99, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(32, 99, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(64, 99, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(96, 99, 32, 35)",
"self.yellowcircle_spritesheet.get_sprite(128, 99, 32, 35)",)
    IDpos = (
        "self.player.rect.x - 30",
        "self.player.rect.y ",
        "self.player.rect.x",
        "self.player.rect.y + 30",
        "self.player.rect.x + 30",
        "self.player.rect.y",
        "self.player.rect.x ",
        "self.player.rect.y - 30",
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Lustrous_Blade
        self.image = self.game.weapon_spritesheet.get_sprite(128,75,16,40)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 2

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.right_attacksanimation = [self.game.yellowcircle_spritesheet.get_sprite(0, 0, 35, 32),
self.game.yellowcircle_spritesheet.get_sprite(35, 0, 35, 32),
self.game.yellowcircle_spritesheet.get_sprite(70, 0, 35, 32),
self.game.yellowcircle_spritesheet.get_sprite(105, 0, 35, 32),
self.game.yellowcircle_spritesheet.get_sprite(140, 0, 35, 32),]

        self.down_attacksanimation = [self.game.yellowcircle_spritesheet.get_sprite(0, 32, 32, 35),
self.game.yellowcircle_spritesheet.get_sprite(32, 32, 32, 35),
self.game.yellowcircle_spritesheet.get_sprite(64, 32, 32, 35),
self.game.yellowcircle_spritesheet.get_sprite(96, 32, 32, 35),
self.game.yellowcircle_spritesheet.get_sprite(128, 32, 32, 35),]

        self.left_attacksanimation = [self.game.yellowcircle_spritesheet.get_sprite(0, 67, 35, 32),
self.game.yellowcircle_spritesheet.get_sprite(35, 67, 35, 32),
self.game.yellowcircle_spritesheet.get_sprite(70, 67, 35, 32),
self.game.yellowcircle_spritesheet.get_sprite(105, 67, 35, 32),
self.game.yellowcircle_spritesheet.get_sprite(140, 67, 35, 32),]

        self.up_attacksanimation = [self.game.yellowcircle_spritesheet.get_sprite(0, 99, 32, 35),
self.game.yellowcircle_spritesheet.get_sprite(32, 99, 32, 35),
self.game.yellowcircle_spritesheet.get_sprite(64, 99, 32, 35),
self.game.yellowcircle_spritesheet.get_sprite(96, 99, 32, 35),
self.game.yellowcircle_spritesheet.get_sprite(128, 99, 32, 35),]




        self.scythe_x_left = self.game.player.rect.x - 30
        self.scythe_y_left = self.game.player.rect.y 
        self.scythe_x_down = self.game.player.rect.x
        self.scythe_y_down = self.game.player.rect.y + 30
        self.scythe_x_right = self.game.player.rect.x + 30
        self.scythe_y_right = self.game.player.rect.y
        self.scythe_x_up = self.game.player.rect.x 
        self.scythe_y_up = self.game.player.rect.y - 30
        self.animation_number = 5


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Lustrous_Blade
                    self.game.player.widthattack = 40
                    self.game.player.heightattack = 40
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.down_attacksanimation
                    self.game.player.downattack_animations = self.left_attacksanimation
                    self.game.player.leftattack_animations = self.up_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks() 

class Heavenly_Wand(pygame.sprite.Sprite):
    nom = "Heavenly Wand"
    attribut = "Puissance : 2"
    IDimage = "self.weapon4_spritesheet.get_sprite(121,4,20,46)"
    IDattack = ("self.bluething_spritesheet.get_sprite(0, 0, 36, 32)",
"self.bluething_spritesheet.get_sprite(36, 0, 36, 32)",
"self.bluething_spritesheet.get_sprite(72, 0, 36, 32)",
"self.bluething_spritesheet.get_sprite(108, 0, 36, 32)",
"self.bluething_spritesheet.get_sprite(144, 0, 36, 32)",
"self.bluething_spritesheet.get_sprite(180, 0, 36, 32)",
"self.bluething_spritesheet.get_sprite(216, 0, 36, 32)",
"self.bluething_spritesheet.get_sprite(0, 32, 32, 36)",
"self.bluething_spritesheet.get_sprite(32, 32, 32, 36)",
"self.bluething_spritesheet.get_sprite(64, 32, 32, 36)",
"self.bluething_spritesheet.get_sprite(96, 32, 32, 36)",
"self.bluething_spritesheet.get_sprite(128, 32, 32, 36)",
"self.bluething_spritesheet.get_sprite(160, 32, 32, 36)",
"self.bluething_spritesheet.get_sprite(192, 32, 32, 36)",
"self.bluething_spritesheet.get_sprite(0, 68, 36, 32)",
"self.bluething_spritesheet.get_sprite(36, 68, 36, 32)",
"self.bluething_spritesheet.get_sprite(72, 68, 36, 32)",
"self.bluething_spritesheet.get_sprite(108, 68, 36, 32)",
"self.bluething_spritesheet.get_sprite(144, 68, 36, 32)",
"self.bluething_spritesheet.get_sprite(180, 68, 36, 32)",
"self.bluething_spritesheet.get_sprite(216, 68, 36, 32)",
"self.bluething_spritesheet.get_sprite(0, 100, 32, 36)",
"self.bluething_spritesheet.get_sprite(32, 100, 32, 36)",
"self.bluething_spritesheet.get_sprite(64, 100, 32, 36)",
"self.bluething_spritesheet.get_sprite(96, 100, 32, 36)",
"self.bluething_spritesheet.get_sprite(128, 100, 32, 36)",
"self.bluething_spritesheet.get_sprite(160, 100, 32, 36)",
"self.bluething_spritesheet.get_sprite(192, 100, 32, 36)",)
    IDpos = (
        "self.player.rect.x - 50",
        "self.player.rect.y ",
        "self.player.rect.x",
        "self.player.rect.y + 50",
        "self.player.rect.x + 50",
        "self.player.rect.y",
        "self.player.rect.x ",
        "self.player.rect.y - 50",
    )
    
    def __init__(self,game, x, y):

        self.game = game 
        self._layer = ITEM_LAYER

        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.ID = Heavenly_Wand
        self.image = self.game.weapon4_spritesheet.get_sprite(121,4,20,46)

        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

        self.puissance = 2

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos = (x,y)

        self.right_attacksanimation = [self.game.bluething_spritesheet.get_sprite(0, 0, 36, 32),
self.game.bluething_spritesheet.get_sprite(36, 0, 36, 32),
self.game.bluething_spritesheet.get_sprite(72, 0, 36, 32),
self.game.bluething_spritesheet.get_sprite(108, 0, 36, 32),
self.game.bluething_spritesheet.get_sprite(144, 0, 36, 32),
self.game.bluething_spritesheet.get_sprite(180, 0, 36, 32),
self.game.bluething_spritesheet.get_sprite(216, 0, 36, 32),]

        self.down_attacksanimation = [self.game.bluething_spritesheet.get_sprite(0, 32, 32, 36),
self.game.bluething_spritesheet.get_sprite(32, 32, 32, 36),
self.game.bluething_spritesheet.get_sprite(64, 32, 32, 36),
self.game.bluething_spritesheet.get_sprite(96, 32, 32, 36),
self.game.bluething_spritesheet.get_sprite(128, 32, 32, 36),
self.game.bluething_spritesheet.get_sprite(160, 32, 32, 36),
self.game.bluething_spritesheet.get_sprite(192, 32, 32, 36),]

        self.left_attacksanimation = [self.game.bluething_spritesheet.get_sprite(0, 68, 36, 32),
self.game.bluething_spritesheet.get_sprite(36, 68, 36, 32),
self.game.bluething_spritesheet.get_sprite(72, 68, 36, 32),
self.game.bluething_spritesheet.get_sprite(108, 68, 36, 32),
self.game.bluething_spritesheet.get_sprite(144, 68, 36, 32),
self.game.bluething_spritesheet.get_sprite(180, 68, 36, 32),
self.game.bluething_spritesheet.get_sprite(216, 68, 36, 32),]

        self.up_attacksanimation = [self.game.bluething_spritesheet.get_sprite(0, 100, 32, 36),
self.game.bluething_spritesheet.get_sprite(32, 100, 32, 36),
self.game.bluething_spritesheet.get_sprite(64, 100, 32, 36),
self.game.bluething_spritesheet.get_sprite(96, 100, 32, 36),
self.game.bluething_spritesheet.get_sprite(128, 100, 32, 36),
self.game.bluething_spritesheet.get_sprite(160, 100, 32, 36),
self.game.bluething_spritesheet.get_sprite(192, 100, 32, 36),]

        self.scythe_x_left = self.game.player.rect.x - 50
        self.scythe_y_left = self.game.player.rect.y 
        self.scythe_x_down = self.game.player.rect.x
        self.scythe_y_down = self.game.player.rect.y + 50
        self.scythe_x_right = self.game.player.rect.x + 50
        self.scythe_y_right = self.game.player.rect.y
        self.scythe_x_up = self.game.player.rect.x 
        self.scythe_y_up = self.game.player.rect.y - 50
        self.animation_number = 7


    def update(self):
        self.game.screen.blit(self.image,self.pos)
        self.collide()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


    def collide(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            keys = pygame.key.get_pressed()
            if hits:
                self.game.player.afficheitem.trueorfalse = True
                self.game.player.afficheitem.nom = self.nom
                self.game.player.afficheitem.attribut1 = self.attribut
            if (hits) and (self.game.player.epee.ID != None):
                self.game.player.afficheequipped.trueorfalse = True
                self.game.player.afficheequipped.nom = self.game.player.epee.ID.nom
                self.game.player.afficheequipped.attribut1 = self.game.player.epee.ID.attribut
            if not hits:
                self.game.player.afficheitem.trueorfalse = False
                self.game.player.afficheequipped.trueorfalse = False


            if hits and keys[pygame.K_e]:
                if self.game.player.take_timer() == False:
                    if self.game.player.epee.ID != None:
                        epee_instance = self.game.player.epee.ID(self.game,self.game.player.rect.x,self.game.player.rect.y)
                        self.game.player.puissance -= epee_instance.puissance
                    self.game.player.puissance += self.puissance
                    self.game.player.epee.ID = Heavenly_Wand
                    self.game.player.widthattack = 40
                    self.game.player.heightattack = 40
                    self.game.player.epee.image = self.image
                    self.game.player.rightattack_animations = self.down_attacksanimation
                    self.game.player.downattack_animations = self.left_attacksanimation
                    self.game.player.leftattack_animations = self.up_attacksanimation
                    self.game.player.upattack_animations = self.right_attacksanimation
                    self.game.player.arme_x_up = self.scythe_x_up
                    self.game.player.arme_y_up = self.scythe_y_up
                    self.game.player.arme_x_down = self.scythe_x_down
                    self.game.player.arme_y_down = self.scythe_y_down
                    self.game.player.arme_x_left = self.scythe_x_left
                    self.game.player.arme_y_left = self.scythe_y_left
                    self.game.player.arme_x_right = self.scythe_x_right
                    self.game.player.arme_y_right = self.scythe_y_right
                    self.game.player.animation_number = self.animation_number
                    self.game.player.afficheitem.trueorfalse = False
                    self.game.player.afficheequipped.trueorfalse = False
                    self.kill()
                    self.game.player.lasttaketimer = pygame.time.get_ticks() 