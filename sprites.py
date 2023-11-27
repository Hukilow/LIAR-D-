from typing import Any
import pygame
from config import *
from enemy import *
from Blocks import *
from HUD import *
from Item import *
import math
import random
import time


vec = pygame.math.Vector2

def vecteur(endroit,WIN_WIDTH,WIN_HEIGHT):
    if endroit == "HAUTGAUCHE":
        soustraire = (WIN_WIDTH,WIN_HEIGHT)
    if endroit == "BASGAUCHE":
        soustraire = (WIN_WIDTH,0)
    if endroit == "HAUTDROIT":
        soustraire = (0,WIN_HEIGHT)
    if endroit == "BASDROIT":
        soustraire = (0,0)
    if endroit == "MILLIEUGAUCHE":
        soustraire = (WIN_WIDTH,WIN_HEIGHT/2)
    if endroit == "MILLIEUDROIT":
        soustraire = (0,WIN_HEIGHT/2)
    if endroit == "MILLIEUHAUT":
        soustraire = (WIN_WIDTH/2, WIN_HEIGHT)
    if endroit == "MILLIEUBAS":
        soustraire = (WIN_WIDTH/2,0)

    looking_vector = pygame.Vector2(1,1)
    CENTER = (WIN_WIDTH/2,WIN_HEIGHT/2)
    CENTER = pygame.Vector2(CENTER)

    delta = (WIN_WIDTH-soustraire[0],WIN_HEIGHT-soustraire[1]) - CENTER
    angle_to_mouse = math.atan2(delta.y, delta.x)
    looking_vector.xy = (100*math.cos(angle_to_mouse), 100*math.sin(angle_to_mouse))
    return looking_vector.xy




class Spritesheet:
    def __init__(self,file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self,x,y,width,height):
        sprite = pygame.Surface([width,height])
        sprite.blit(self.sheet, (0,0), (x,y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite
class Spritesheetblanc:
    def __init__(self,file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self,x,y,width,height):
        sprite = pygame.Surface([width,height])
        sprite.blit(self.sheet, (0,0), (x,y, width, height))
        sprite.set_colorkey(WHITE)
        return sprite

class Player(pygame.sprite.Sprite): 
    def __init__(self, game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER #Couche pour savoir qui est au dessus
        self.groups = self.game.all_sprites #ajoute le player aux sprites groupes
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.GAUCHE = (vecteur("HAUTGAUCHE",self.game.WIN_WIDTH,self.game.WIN_HEIGHT), vecteur("BASGAUCHE",self.game.WIN_WIDTH,self.game.WIN_HEIGHT))
        self.DROITE = (vecteur("HAUTDROIT",self.game.WIN_WIDTH,self.game.WIN_HEIGHT), vecteur("BASDROIT",self.game.WIN_WIDTH,self.game.WIN_HEIGHT))
        self.HAUT = (vecteur("HAUTGAUCHE",self.game.WIN_WIDTH,self.game.WIN_HEIGHT), vecteur("HAUTDROIT",self.game.WIN_WIDTH,self.game.WIN_HEIGHT))
        self.BAS = (vecteur("BASGAUCHE",self.game.WIN_WIDTH,self.game.WIN_HEIGHT), vecteur("BASDROIT",self.game.WIN_WIDTH,self.game.WIN_HEIGHT))
        self.MILLIEUGAUCHE = vecteur("MILLIEUGAUCHE",self.game.WIN_WIDTH,self.game.WIN_HEIGHT)
        self.MILLIEUDROIT = vecteur("MILLIEUDROIT",self.game.WIN_WIDTH,self.game.WIN_HEIGHT)
        self.MILLIEUHAUT = vecteur("MILLIEUHAUT",self.game.WIN_WIDTH,self.game.WIN_HEIGHT)
        self.MILLIEUBAS = vecteur("MILLIEUBAS",self.game.WIN_WIDTH,self.game.WIN_HEIGHT)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.vitesse = 1
        self.vitesse2 = 1 
        self.vitesse3 = 1

        self.movement_loop = 0

        self.x_change = 0
        self.y_change = 0
        
        self.healh = 10*self.game.multiplicateur_difficulte_hp

        self.puissance = 1
        self.widthattack = 32
        self.heightattack = 32

        self.enemyattacks = 1

        self.light = Light(game,self.x,self.y,900,(255, 167, 38, 50))

        self.epee = EpeeHUD(game,(self.x-(self.game.WIN_WIDTH/2))+20,(self.y-(self.game.WIN_HEIGHT/2))+50,self.game.equipement_spritesheet.get_sprite(0, 0, 32, 32))
        self.helmet = CasqueHUD(game,(self.x-(self.game.WIN_WIDTH/2))+60,(self.y-(self.game.WIN_HEIGHT/2))+30,self.game.equipement_spritesheet.get_sprite(36,0, 32, 32))
        self.chest = ChestHUD(game,(self.x-(self.game.WIN_WIDTH/2))+60,(self.y-(self.game.WIN_HEIGHT/2))+70,self.game.equipement_spritesheet.get_sprite(36, 36, 32, 32))
        self.pants = PantsHUD(game,(self.x-(self.game.WIN_WIDTH/2))+60,(self.y-(self.game.WIN_HEIGHT/2))+110,self.game.equipement_spritesheet.get_sprite(36, 72, 32, 32))
        self.boots = BootsHUD(game,(self.x-(self.game.WIN_WIDTH/2))+60,(self.y-(self.game.WIN_HEIGHT/2))+150,self.game.equipement_spritesheet.get_sprite(36, 112, 32, 28))
        self.ranged = RangeHUD(game,(self.x-(self.game.WIN_WIDTH/2))+100,(self.y-(self.game.WIN_HEIGHT/2))+50,self.game.equipement_spritesheet.get_sprite(72, 72, 32, 32))
        self.ring = RingHUD(game,(self.x-(self.game.WIN_WIDTH/2))+20,(self.y-(self.game.WIN_HEIGHT/2))+110,self.game.equipement_spritesheet.get_sprite(112, 36, 28, 32))
        self.necklace = NecklaceHUD(game,(self.x-(self.game.WIN_WIDTH/2))+100,(self.y-(self.game.WIN_HEIGHT/2))+110,self.game.equipement_spritesheet.get_sprite(108, 108, 32, 32))
        self.healthbar = HealthBar(game,(self.x-(self.game.WIN_WIDTH/2))+10,(self.y+(self.game.WIN_HEIGHT/2))-40,self.healh,self.healh,True)
        self.etage = Etage(game,self.x+(self.game.WIN_WIDTH/2)-180,self.y-(self.game.WIN_HEIGHT/2)+20,1)
        self.potion = PotionHUD(game,self.x+(self.game.WIN_WIDTH/2)-82,self.y+(self.game.WIN_HEIGHT/2)-63,0)

        self.afficheitem = AfficheItem(game,self.x-(self.game.WIN_WIDTH/2)+10,self.y-(self.game.WIN_HEIGHT/2)+395)
        self.afficheequipped = AfficheEquipped(game,self.x-(self.game.WIN_WIDTH/2)+10,self.y-(self.game.WIN_HEIGHT/2)+240)

        self.lasttaketimer = pygame.time.get_ticks()
        self.lastdrinktimer = pygame.time.get_ticks()
        self.time = pygame.time.get_ticks()

        self.facing= 'down'
        self.animation_loop = 1
        self.image = self.game.character_spritesheet.get_sprite(3,2, 28, 28)
        self.rect = self.image.get_rect() #comme la hitbox, son endroit 
        self.rect.x = self.x
        self.rect.y = self.y
        self.down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        self.left_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        self.up_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        self.right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]
        

        self.rightattack_animations = []
        self.downattack_animations = []
        self.leftattack_animations = []
        self.upattack_animations = []

        self.arme_x_left = None
        self.arme_y_left = None
        self.arme_x_down = None
        self.arme_y_down = None
        self.arme_x_right = None
        self.arme_y_right = None
        self.arme_x_up = None
        self.arme_y_up = None

        self.animation_number = 5 

        for sprite in self.game.all_sprites:
            if isinstance(sprite, Player):
                self.spritedujoueur = sprite
        

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0


        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.healthbar.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.etage.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.potion.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.epee.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.ranged.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.helmet.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.chest.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.pants.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.boots.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.ring.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.necklace.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.game.hitbox.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.afficheitem.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.afficheequipped.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.healthbar.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.etage.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.potion.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.epee.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.ranged.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.helmet.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.chest.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.pants.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.boots.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.ring.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.necklace.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.game.hitbox.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.afficheitem.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.afficheequipped.x_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
        if keys[pygame.K_z]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.healthbar.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.etage.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.potion.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.epee.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.ranged.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.helmet.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.chest.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.pants.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.boots.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.ring.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.necklace.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.game.hitbox.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.afficheitem.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.afficheequipped.y_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.healthbar.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.etage.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.potion.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.epee.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.ranged.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.helmet.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.chest.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.pants.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.boots.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.ring.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.necklace.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.game.hitbox.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.afficheitem.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
            self.afficheequipped.y_change += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
        if keys[pygame.K_g] and self.potion.nbrpotion >= 1:
            if self.drink_timer() == False:
                self.healthbar.heal(1)
                self.lastdrinktimer = pygame.time.get_ticks()

        looking_vector = pygame.Vector2(1,1)
        CENTER = (self.game.WIN_WIDTH/2, self.game.WIN_HEIGHT/2)
        CENTER = pygame.Vector2(CENTER)

        # Relative position of mouse
        mouse_pos = pygame.mouse.get_pos()
        delta = mouse_pos - CENTER

        # Calculate the angle 
        angle_to_mouse = math.atan2(delta.y, delta.x)
        looking_vector.xy = (100*math.cos(angle_to_mouse), 100*math.sin(angle_to_mouse))

        if (((looking_vector.xy[0] <= self.GAUCHE[1][0]) and (looking_vector.xy[0] >= self.MILLIEUGAUCHE[0])) and ((looking_vector.xy[1] <= self.GAUCHE[1][1]) and (looking_vector.xy[1] >= self.GAUCHE[0][1]))):
            self.facing = 'left'
        if (((looking_vector.xy[0] <= self.MILLIEUDROIT[0]) and (looking_vector.xy[0] >= self.DROITE[1][0])) and ((looking_vector.xy[1] <= self.DROITE[1][1]) and (looking_vector.xy[1] >= self.DROITE[0][1]))):
            self.facing = 'right'
        if (((looking_vector.xy[0] >= self.HAUT[0][0]) and (looking_vector.xy[0] <= self.HAUT[1][0])) and ((looking_vector.xy[1] <= self.HAUT[1][1]) and (looking_vector.xy[1] >= self.MILLIEUHAUT[1]))):
            self.facing = 'up'
        if (((looking_vector.xy[0] >= self.BAS[0][0]) and (looking_vector.xy[0] <= self.BAS[1][0])) and ((looking_vector.xy[1] <= self.MILLIEUBAS[1]) and (looking_vector.xy[1] >= self.BAS[1][1]))):
            self.facing = 'down'

    def take_timer(self):
        return self.lasttaketimer > pygame.time.get_ticks() - 500
    
    def drink_timer(self):
        return self.lastdrinktimer > pygame.time.get_ticks() - 1500


    def animate(self):
        if self.facing == 'down':
            if self.y_change == 0 and self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3,2, self.width, self.height)
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
        if self.facing == "left":
            if self.x_change == 0 and self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    
        if self.facing == "right":
            if self.x_change == 0 and self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0 and self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

    """def knockback(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        hits2 = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if (self.facing == 'right') and (hits) and not (hits2):
            self.STUN_player = True
            max_travel = KNOCKBACK_SPEED*3
            for i in range(max_travel):
                self.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                self.healthbar.x_change -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                for sprite in self.game.all_sprites:
                    sprite.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                temps = pygame.time.get_ticks()
                while (pygame.time.get_ticks()) - temps < 2:
                    self.collide_blocks("x")

                
            self.STUN_player = False


        if (self.facing == 'left') and (hits) and not (hits2):
            movement_loop = 0
            max_travel = KNOCKBACK_SPEED*3
            self.x_change += KNOCKBACK_SPEED*3
            self.healthbar.x_change += KNOCKBACK_SPEED*3
            for sprite in self.game.all_sprites:
                sprite.rect.x -= KNOCKBACK_SPEED*3
            movement_loop -= 1 
            if movement_loop <= -max_travel:
                max_travel = movement_loop
                
        if (self.facing == 'down') and (hits) and not (hits2) :
            movement_loop = 0
            max_travel = KNOCKBACK_SPEED*3
            self.y_change -= KNOCKBACK_SPEED*3
            self.healthbar.y_change -= KNOCKBACK_SPEED*3
            for sprite in self.game.all_sprites:
                sprite.rect.y += KNOCKBACK_SPEED*3
            movement_loop -= 1 
            if movement_loop <= -max_travel:
                max_travel = movement_loop
        if (self.facing == 'up') and (hits) and not (hits2) :
            movement_loop = 0
            max_travel = KNOCKBACK_SPEED*3
            self.y_change += KNOCKBACK_SPEED*3
            self.healthbar.y_change += KNOCKBACK_SPEED*3
            for sprite in self.game.all_sprites:
                sprite.rect.y -= KNOCKBACK_SPEED*3
            movement_loop -= 1 
            if movement_loop <= -max_travel:
                max_travel = movement_loop"""
    

class Button():
    def __init__(self,x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('mandalorelasertitle.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
    

class Attack(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        if self.game.player.epee.ID != None:
            if self.game.player.facing == 'up':
                self.x = self.game.player.arme_x_up
                self.y = self.game.player.arme_y_up

            if self.game.player.facing == 'down':
                self.x = self.game.player.arme_x_down
                self.y = self.game.player.arme_y_down

            if self.game.player.facing == 'left':
                self.x = self.game.player.arme_x_left
                self.y = self.game.player.arme_y_left

            if self.game.player.facing == 'right':
                self.x = self.game.player.arme_x_right
                self.y = self.game.player.arme_y_right

        else: 
            if self.game.player.facing == 'up':
                self.x = self.game.player.rect.x
                self.y = self.game.player.rect.y - TILESIZE
            if self.game.player.facing == 'down':
                self.x = self.game.player.rect.x
                self.y = self.game.player.rect.y + TILESIZE
            if self.game.player.facing == 'left':
                self.x = self.game.player.rect.x - TILESIZE
                self.y = self.game.player.rect.y
            if self.game.player.facing == 'right':
                self.x = self.game.player.rect.x + TILESIZE
                self.y = self.game.player.rect.y
        print(self.x)
        print(self.y)

        self.width = self.game.player.widthattack
        self.height = self.game.player.heightattack
        
        self.animation_loop = 0

        self.image = self.game.attack_spritesheet.get_sprite(0,0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.game.player.epee.ID != None:

            self.right_animations = self.game.player.rightattack_animations

            self.down_animations = self.game.player.downattack_animations
            self.left_animations = self.game.player.leftattack_animations
            self.up_animations = self.game.player.upattack_animations
        else:
            self.right_animations = [self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height)]

            self.down_animations = [self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height)]

            self.left_animations = [self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height)]

            self.up_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
                            self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height)]

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hit1 = pygame.sprite.spritecollide(self, self.game.coffre1, True)
        hit2 = pygame.sprite.spritecollide(self, self.game.coffre2, True)
        hit3 = pygame.sprite.spritecollide(self, self.game.coffre3, True)
        hit4 = pygame.sprite.spritecollide(self, self.game.coffre4, True)
        hit5 = pygame.sprite.spritecollide(self, self.game.coffre5, True)
        hit6 = pygame.sprite.spritecollide(self, self.game.coffre6, True)
        hit7 = pygame.sprite.spritecollide(self, self.game.coffre7, True)
        hit8 = pygame.sprite.spritecollide(self, self.game.coffre8, True)
        hit9 = pygame.sprite.spritecollide(self, self.game.coffre9, True)
        if hit1:
            for coffre in hit1:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST1")
            arme(self.game,x_coffre+10,y_coffre)
        if hit2:
            for coffre in hit2:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST2")
            arme(self.game,x_coffre+10,y_coffre)
        if hit3:
            for coffre in hit3:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST3")
            arme(self.game,x_coffre+10,y_coffre)
        if hit4:
            for coffre in hit4:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST4")
            arme(self.game,x_coffre+10,y_coffre)
        if hit5:
            for coffre in hit5:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST5")
            arme(self.game,x_coffre+10,y_coffre)
        if hit6:
            for coffre in hit6:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST6")
            arme(self.game,x_coffre+10,y_coffre)
        if hit7:
            for coffre in hit7:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST7")
            arme(self.game,x_coffre+10,y_coffre)
        if hit8:
            for coffre in hit8:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST8")
            arme(self.game,x_coffre+10,y_coffre)
        if hit9:
            for coffre in hit9:
                x_coffre = coffre.rect.x
                y_coffre = coffre.rect.y
            arme = self.dropchest("DROPCHEST9")
            arme(self.game,x_coffre+10,y_coffre)


    def dropchest(self,DROPCHEST):
        if DROPCHEST == "DROPCHEST1": # couloir commun
            DROPCHEST = [Crimson_Blade,Flamestrike_Mallet]
            return random.choice(DROPCHEST)
        elif DROPCHEST == "DROPCHEST2": # couloir peu commun
            DROPCHEST = [Scythe,GreatSword,HellScythe,SnakeSword,WintersBallad,Hematite_Blade]
            return random.choice(DROPCHEST)
        elif DROPCHEST == "DROPCHEST3": # couloir rare
            DROPCHEST = [Boots_iron,Chest_iron,Helmet_iron,Pants_iron,Scythe]
            return random.choice(DROPCHEST)
        elif DROPCHEST == "DROPCHEST4": # couloir epic
            DROPCHEST = [SnakeSword]
            return random.choice(DROPCHEST)
        elif DROPCHEST == "DROPCHEST5": # salle rare
            DROPCHEST = [Necklace_copper,Ring_copper]
            return random.choice(DROPCHEST)
        elif DROPCHEST == "DROPCHEST6": # couloir légendaire
            DROPCHEST = [Necklace_rubis,Ring_rubis]
            return random.choice(DROPCHEST)
        elif DROPCHEST == "DROPCHEST7": # salle commun
            DROPCHEST = [Necklace_rubis,Ring_rubis]
            return random.choice(DROPCHEST)
        elif DROPCHEST == "DROPCHEST8":  # salle légendaire
            DROPCHEST = [Necklace_emerald]
            return random.choice(DROPCHEST)
        elif DROPCHEST == "DROPCHEST9": # couloir ???
            DROPCHEST = [Ring_emerald]
            return random.choice(DROPCHEST)
        
    def animate(self):
        direction = self.game.player.facing

        if direction == 'up':
            try:
                self.image = self.up_animations[math.floor(self.animation_loop)]
            except:
                pass
            self.animation_loop += 0.5
            if self.animation_loop >= self.game.player.animation_number:
                self.kill()

        if direction == 'down':
            try:
                self.image = self.down_animations[math.floor(self.animation_loop)]
            except:
                pass
            self.animation_loop += 0.5
            if self.animation_loop >= self.game.player.animation_number:
                self.kill()

        if direction == 'right':
            try:
                self.image = self.right_animations[math.floor(self.animation_loop)]
            except:
                pass
            self.animation_loop += 0.5
            if self.animation_loop >= self.game.player.animation_number:
                self.kill()

        if direction == 'left':
            try:
                self.image = self.left_animations[math.floor(self.animation_loop)]
            except:
                pass
            self.animation_loop += 0.5
            if self.animation_loop >= self.game.player.animation_number:
                self.kill()

