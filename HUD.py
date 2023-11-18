from typing import Any
from config import *
import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self,game,x,y,health,maxhealth,affichage):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.afficher = affichage
        self.health = health
        self.maxhealth = maxhealth
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.barredevie = pygame.Surface((self.maxhealth*31,30))
        self.barredevie.fill(SIENNA)
        pygame.draw.rect(self.barredevie,RED,(5,5,self.health*30,20))

        self.image = self.barredevie

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, HealthBar):
                self.spriteduhealthbar = sprite
        


    def take_damage(self,damage):
        self.health -= damage

    def heal(self,heal):
        if self.health < self.maxhealth:
            self.health += heal
            self.game.player.potion.potion_bu()
    def update(self):
        self.image = self.affichageur(self.afficher)
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def affichageur(self,affichage):
        if affichage == True:
            self.barredevie = pygame.Surface((self.maxhealth*30,30))
            self.barredevie.fill(GREY)
            pygame.draw.rect(self.barredevie,LIGHTRED,(5,5,(self.health*30)-10,20 ))
            self.image =self.barredevie
            return self.image
        if affichage == False:
            self.image = self.game.terrain_spritesheet.get_sprite(0,960,32,32)
            return self.image
        
class Etage(pygame.sprite.Sprite):
    def __init__(self,game,x,y,etage):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.etageici = etage
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.sprite_etage = [self.game.etage_spritesheet.get_sprite(0, 0, 158, 46),
                        self.game.etage_spritesheet.get_sprite(158, 0, 158, 46),
                        self.game.etage_spritesheet.get_sprite(316, 0, 158, 46),
                        self.game.etage_spritesheet.get_sprite(474, 0, 158, 46),
                        self.game.etage_spritesheet.get_sprite(632, 0, 158, 46),
                        self.game.etage_spritesheet.get_sprite(790, 0, 158, 46),
                        self.game.etage_spritesheet.get_sprite(948, 0, 158, 46),]
 
        self.image = self.sprite_etage[(self.etageici)-1]   
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y



           
        for sprite in self.game.all_sprites:
            if isinstance(sprite, Etage):
                self.spriteduetage = sprite


    def monter(self):
        self.etageici -= 1
        self.image = self.sprite_etage[self.etageici-1]

    def descendre(self):
        self.etageici += 1
        self.image = self.sprite_etage[self.etageici-1]
    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class PotionHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,nombre):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.nbrpotion = nombre
        self.pospotion = (x,y)
        self.posnbr = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
       
        self.spritenbr = [self.game.potion_spritesheet.get_sprite(400, 0, 80, 60),
                    self.game.potion_spritesheet.get_sprite(0, 0, 80, 60),
                    self.game.potion_spritesheet.get_sprite(80, 0, 80, 60),
                    self.game.potion_spritesheet.get_sprite(160, 0, 80, 60),
                    self.game.potion_spritesheet.get_sprite(240, 0, 80, 60),
                    self.game.potion_spritesheet.get_sprite(320, 0, 80, 60),]
        
        self.image = self.spritenbr[self.nbrpotion]
            

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
        self.image = self.game.potion_spritesheet.get_sprite(400,0,80,60)
 


        for sprite in self.game.all_sprites:
            if isinstance(sprite, PotionHUD):
                self.spriteduhubpotion = sprite
        

        
    def item_pris(self):
        self.nbrpotion += 1
        self.image = self.spritenbr[self.nbrpotion]

    def potion_bu(self):
        self.nbrpotion -= 1
        self.image = self.spritenbr[self.nbrpotion]

    def update(self):

        self.game.screen.blit(self.image,self.posnbr)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class AfficheItem(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = HEALTH_LAYER
        self.trueorfalse = False

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.font = pygame.font.Font('mandalorelasertitle.ttf', 25)
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.nom = None
        self.attribut1 = None
        self.attribut2 = None

        self.x_change = 0
        self.y_change = 0
        

        self.spriteaffiche = self.game.affiche_spritesheet.get_sprite(0,0,225,145)
        self.draw_text(self.spriteaffiche,self.nom,self.font,SIENNA,25,25)
        self.draw_text(self.spriteaffiche,self.attribut1,self.font,SIENNA,15,50)
        self.image = self.spriteaffiche

            

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
 


        for sprite in self.game.all_sprites:
            if isinstance(sprite, AfficheItem):
                self.spriteduafficheitem = sprite
        
    def draw_text(self,affiche,text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        affiche.blit(img,(x,y))  

    def update(self):
        self.image = self.affichage(self.trueorfalse)
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def affichage(self,affichage):
        if affichage == True:
            self.spriteaffiche = self.game.affiche_spritesheet.get_sprite(0,0,225,145)
            self.font = pygame.font.Font('mandalorelasertitle.ttf', 23)
            self.draw_text(self.spriteaffiche,self.nom,self.font,BLUE,25,25)
            self.font = pygame.font.Font('mandalorelasertitle.ttf', 18)
            self.draw_text(self.spriteaffiche,self.attribut1,self.font,BLUE,25,65)
            if self.attribut2 != None:
                self.draw_text(self.spriteaffiche,self.attribut2,self.font,BLUE,25,85)
                self.attribut2 = None
            self.image = self.spriteaffiche
            return self.image
        if affichage == False:
            self.image = self.game.terrain_spritesheet.get_sprite(0,960,32,32)
            return self.image
        
class AfficheEquipped(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = HEALTH_LAYER
        self.trueorfalse = False

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.font = pygame.font.Font('mandalorelasertitle.ttf', 25)
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.nom = None
        self.attribut1 = None
        self.attribut2 = None

        self.x_change = 0
        self.y_change = 0
        

        self.spriteaffiche = self.game.affiche_spritesheet.get_sprite(0,0,225,145)
        self.draw_text(self.spriteaffiche,self.nom,self.font,SIENNA,25,25)
        self.draw_text(self.spriteaffiche,self.attribut1,self.font,SIENNA,15,50)
        self.image = self.spriteaffiche

            

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
 


        for sprite in self.game.all_sprites:
            if isinstance(sprite, AfficheEquipped):
                self.spriteduafficheequipped = sprite
        
    def draw_text(self,affiche,text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        affiche.blit(img,(x,y))  

    def update(self):
        self.image = self.affichage(self.trueorfalse)
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def affichage(self,affichage):
        if affichage == True:
            self.spriteaffiche = self.game.affiche_spritesheet.get_sprite(0,0,225,145)
            self.font = pygame.font.Font('mandalorelasertitle.ttf', 23)
            self.draw_text(self.spriteaffiche,self.nom,self.font,LIMEGREEN,25,25)
            self.font = pygame.font.Font('mandalorelasertitle.ttf', 18)
            self.draw_text(self.spriteaffiche,self.attribut1,self.font,LIMEGREEN,25,65)
            if self.attribut2 != None:
                self.draw_text(self.spriteaffiche,self.attribut2,self.font,LIMEGREEN,25,85)
                self.attribut2 = None
            self.image = self.spriteaffiche
            return self.image
        if affichage == False:
            self.image = self.game.terrain_spritesheet.get_sprite(0,960,32,32)
            return self.image

class EpeeHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.ID = None
        self.image = image
            
        

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, EpeeHUD):
                self.spriteduEpeeHUD = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class CasqueHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.ID = None
        self.image = image
            
        

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, CasqueHUD):
                self.spriteduCasqueHUD = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class ChestHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.ID = None
        self.image = image
            
        

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, ChestHUD):
                self.spriteduChestHUD = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class PantsHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.ID = None
        self.image = image
            
        

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, PantsHUD):
                self.spriteduPantsHUD = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class BootsHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.ID = None
        self.image = image
            
        

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, BootsHUD):
                self.spritedesBootsHUD = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class RangeHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.ID = None
        self.image = image
            
        

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, RangeHUD):
                self.spriteRangeHUD = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class RingHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.ID = None
        self.image = image
            
        

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, RingHUD):
                self.spriteRingHUD = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class NecklaceHUD(pygame.sprite.Sprite):
    def __init__(self,game,x,y,image):

        self.game = game
        self._layer = HEALTH_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0
        
        self.ID = None
        self.image = image
            
        

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, NecklaceHUD):
                self.spriteNecklaceHUD = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

class PlayerHitbox(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = HITBOX_LAYER

        self.groups = self.game.all_sprites, self.game.playerhitbox
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.pos = (x,y)

        self.x = x
        self.y = y

        self.derniertempsechelle = pygame.time.get_ticks()

        self.x_change = 9  #Pour que la hitbox soit au milieu du joueur NE PAS CHANGER
        self.y_change = 5  #Pour que la hitbox soit au milieu du joueur NE PAS CHANGER
        
        
        self.image = self.game.terrain_spritesheet.get_sprite(36,289,17,25)
            
        self.vitesse = self.game.player.vitesse
        self.vitesse2 = self.game.player.vitesse2
        self.vitesse3 = self.game.player.vitesse3

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, PlayerHitbox):
                self.spriteduplayerhitbox = sprite

    def update(self):
        self.game.screen.blit(self.image,self.pos)

        self.rect.x += self.x_change
        #self.collide_blocks('x')
        self.rect.y += self.y_change
        #self.collide_blocks('y')
        self.collide_enemyattacks()
        self.collide_enemy()
        self.collide_lava()
        self.speed()
        self.speed_lava()
        self.collide_echelle()

        self.vitesse = self.game.player.vitesse
        self.vitesse2 = self.game.player.vitesse2
        self.vitesse3 = self.game.player.vitesse3


        self.x_change = 0
        self.y_change = 0

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 2000
    
    def speed(self):
        if self.invincibility() == False:
            self.game.player.vitesse = 1
        else:
            if self.game.player.vitesse3 >= 1.2:
                self.game.player.vitesse = 1
            else:
                self.game.player.vitesse = 1.3

    def invincibility_lava(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 500
    
    def invincibility_trap(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 1250

    def speed_lava(self):
        if self.invincibility_lava() == False:
            self.game.player.vitesse2 = 1
        else:
            self.game.player.vitesse2 = 0.7

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            if self.invincibility() == False:
                self.game.player.healthbar.take_damage(1+self.game.multiplicateur_difficulte_attack_enemies)
                self.derniertemps = pygame.time.get_ticks()
                print(self.derniertemps)
            
            if self.game.player.healthbar.health <= 0 :
                self.kill()
                self.game.playing = False

    def collide_enemyattacks(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacksenemy, False)
        if hits:
            print("hit")
            if self.invincibility() == False:
                self.game.player.healthbar.take_damage(self.game.player.enemyattacks)
                self.derniertemps = pygame.time.get_ticks()
                print(self.derniertemps)
            
            if self.game.player.healthbar.health <= 0 :
                self.kill()
                self.game.playing = False

    def collide_lava(self):
        hits = pygame.sprite.spritecollide(self, self.game.trap, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.lave, False)
        if hits:
            if self.invincibility_lava() == False:
                self.game.player.healthbar.take_damage(2)
                self.derniertemps2 = pygame.time.get_ticks()
                print(self.derniertemps2)
            
            if self.game.player.healthbar.health < 0 :
                self.kill()
                self.game.playing = False

        if hits1:
            if self.invincibility_trap() == False:
                self.game.player.healthbar.take_damage(2)
                self.derniertemps2 = pygame.time.get_ticks()
                print(self.derniertemps2)
            
            if self.game.player.healthbar.health < 0 :
                self.kill()
                self.game.playing = False
        

    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1, False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9:
            if hits1:
                hit = hits1
            elif hits:
                hit = hits
            elif hits2:
                hit = hits2
            elif hits3:
                hit = hits3
            elif hits3:
                hit = hits3
            elif hits4:
                hit = hits4
            elif hits5:
                hit = hits5
            elif hits6:
                hit = hits6
            elif hits7:
                hit = hits7
            elif hits8:
                hit = hits8
            elif hits9:
                hit = hits9

            if direction == 'x':
                    if self.x_change > 0:
                        for sprite in self.game.all_sprites:
                            sprite.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.rect.x = hit[0].rect.left - self.rect.width
                        self.game.player.healthbar.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.etage.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.potion.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.epee.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.ranged.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.helmet.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.chest.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.pants.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.boots.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.ring.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.necklace.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.afficheitem.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.afficheequipped.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                    if self.x_change < 0:
                        for sprite in self.game.all_sprites:
                            sprite.rect.x -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.rect.x = hit[0].rect.right
                        self.game.player.healthbar.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.etage.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.potion.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.epee.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.ranged.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.helmet.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.chest.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.pants.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.boots.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.ring.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.necklace.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.afficheitem.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.afficheequipped.rect.x += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3

            if direction == 'y':
                    if self.y_change > 0:
                        for sprite in self.game.all_sprites:
                            sprite.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.rect.y = hit[0].rect.top - self.rect.height
                        self.game.player.healthbar.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.etage.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.potion.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.epee.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.ranged.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.helmet.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.chest.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.pants.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.boots.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.ring.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.necklace.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.afficheitem.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.afficheequipped.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                    if self.y_change < 0:
                        for sprite in self.game.all_sprites:
                            sprite.rect.y -= PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.rect.y = hit[0].rect.bottom
                        self.game.player.healthbar.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.etage.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.potion.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.epee.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.ranged.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.helmet.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.chest.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.pants.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.boots.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.ring.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.necklace.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.afficheitem.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3
                        self.game.player.afficheequipped.rect.y += PLAYER_SPEED*self.vitesse*self.vitesse2*self.vitesse3

    def monter_descendretime(self):
        return self.derniertempsechelle > pygame.time.get_ticks() - 1000

    def collide_echelle(self):
        hit = pygame.sprite.spritecollide(self, self.game.echellehaut, False)
        hit2 = pygame.sprite.spritecollide(self, self.game.echellebas, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.escalier, False)
        keys = pygame.key.get_pressed()

        if hit and keys[pygame.K_SPACE]:
            #if self.monter_descendretime() == False:
                #self.descendre_etage()
            self.game.player.etage.descendre()
            for sprite in self.game.all_sprites:
                if (self.game.player.spritedujoueur != sprite) and (self.game.player.light.spritedelalumiere != sprite) and (self.game.player.healthbar.spriteduhealthbar != sprite) and (self.game.player.etage.spriteduetage != sprite) and (self.game.player.potion.spriteduhubpotion!= sprite) and (self.game.player.epee.spriteduEpeeHUD != sprite) and (self.game.player.helmet.spriteduCasqueHUD != sprite) and (self.game.player.chest.spriteduChestHUD != sprite) and (self.game.player.pants.spriteduPantsHUD != sprite) and (self.game.player.boots.spritedesBootsHUD != sprite) and (self.game.player.necklace.spriteNecklaceHUD != sprite) and (self.game.player.ring.spriteRingHUD != sprite) and (self.game.player.ranged.spriteRangeHUD != sprite) and (self.game.player.afficheequipped.spriteduafficheequipped != sprite) and (self.game.player.afficheitem.spriteduafficheitem != sprite) and (self.spriteduplayerhitbox != sprite):
                    sprite.kill()
            self.game.createTilemapboss(tilemap_boss,False)
                #self.derniertempsechelle = pygame.time.get_ticks()
        if hit2 and keys[pygame.K_SPACE]:
            if self.monter_descendretime() == False:
                self.monter_etage()
                self.derniertempsechelle = pygame.time.get_ticks()
        if hits3 and keys[pygame.K_SPACE]:
            self.game.player.etage.descendre()
            for sprite in self.game.all_sprites:
                if (self.game.player.spritedujoueur != sprite) and (self.game.player.light.spritedelalumiere != sprite) and (self.game.player.healthbar.spriteduhealthbar != sprite) and (self.game.player.etage.spriteduetage != sprite) and (self.game.player.potion.spriteduhubpotion!= sprite) and (self.game.player.epee.spriteduEpeeHUD != sprite) and (self.game.player.helmet.spriteduCasqueHUD != sprite) and (self.game.player.chest.spriteduChestHUD != sprite) and (self.game.player.pants.spriteduPantsHUD != sprite) and (self.game.player.boots.spritedesBootsHUD != sprite) and (self.game.player.necklace.spriteNecklaceHUD != sprite) and (self.game.player.ring.spriteRingHUD != sprite) and (self.game.player.ranged.spriteRangeHUD != sprite) and (self.game.player.afficheequipped.spriteduafficheequipped != sprite) and (self.game.player.afficheitem.spriteduafficheitem != sprite) and (self.spriteduplayerhitbox != sprite):
                    sprite.kill()
            self.game.createTilemapboss(tilemap_boss)

    def descendre_etage(self):
            if self.game.player.etage.etageici == 1:
                tilemap = self.game.all_maps.tilemap2
            elif self.game.player.etage.etageici == 2:
                tilemap = self.game.all_maps.tilemap3
            elif self.game.player.etage.etageici == 3:
                tilemap = self.game.all_maps.tilemap4
            elif self.game.player.etage.etageici == 4:
                tilemap = self.game.all_maps.tilemap5
            elif self.game.player.etage.etageici == 5:
                tilemap = self.game.all_maps.tilemap6
            for sprite in self.game.all_sprites:
                if (self.game.player.spritedujoueur != sprite) and (self.game.player.light.spritedelalumiere != sprite) and (self.game.player.healthbar.spriteduhealthbar != sprite) and (self.game.player.etage.spriteduetage != sprite) and (self.game.player.potion.spriteduhubpotion!= sprite) and (self.game.player.epee.spriteduEpeeHUD != sprite) and (self.game.player.helmet.spriteduCasqueHUD != sprite) and (self.game.player.chest.spriteduChestHUD != sprite) and (self.game.player.pants.spriteduPantsHUD != sprite) and (self.game.player.boots.spritedesBootsHUD != sprite) and (self.game.player.necklace.spriteNecklaceHUD != sprite) and (self.game.player.ring.spriteRingHUD != sprite) and (self.game.player.ranged.spriteRangeHUD != sprite) and (self.game.player.afficheequipped.spriteduafficheequipped != sprite) and (self.game.player.afficheitem.spriteduafficheitem != sprite) and (self.spriteduplayerhitbox != sprite):
                    sprite.kill()
            self.game.createTilemap2(tilemap,"descendre")
            self.game.player.etage.descendre()

    def monter_etage(self):

            if self.game.player.etage.etageici == 2:
                tilemap = self.game.all_maps.tilemap1
            elif self.game.player.etage.etageici == 3:
                tilemap = self.game.all_maps.tilemap2
            elif self.game.player.etage.etageici == 4:
                tilemap = self.game.all_maps.tilemap3
            elif self.game.player.etage.etageici == 5:
                tilemap = self.game.all_maps.tilemap4
            elif self.game.player.etage.etageici == 6:
                tilemap = self.game.all_maps.tilemap5
            for sprite in self.game.all_sprites:
                if (self.game.player.spritedujoueur != sprite) and (self.game.player.light.spritedelalumiere != sprite) and (self.game.player.healthbar.spriteduhealthbar != sprite) and (self.game.player.etage.spriteduetage != sprite) and (self.game.player.potion.spriteduhubpotion!= sprite) and (self.game.player.epee.spriteduEpeeHUD != sprite) and (self.game.player.helmet.spriteduCasqueHUD != sprite) and (self.game.player.chest.spriteduChestHUD != sprite) and (self.game.player.pants.spriteduPantsHUD != sprite) and (self.game.player.boots.spritedesBootsHUD != sprite) and (self.game.player.necklace.spriteNecklaceHUD != sprite) and (self.game.player.ring.spriteRingHUD != sprite) and (self.game.player.ranged.spriteRangeHUD != sprite) and (self.game.player.afficheequipped.spriteduafficheequipped != sprite) and (self.game.player.afficheitem.spriteduafficheitem != sprite) and (self.spriteduplayerhitbox != sprite):
                   sprite.kill()
            self.game.createTilemap2(tilemap,"monter")
            self.game.player.etage.monter()


class Light(pygame.sprite.Sprite):
    def __init__(self,game,x,y,radius,couleur_intensite):
        
        self.game = game
        self._layer = LIGHT_LAYER

        self.groups = self.game.all_sprites, self.game.light
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x_change = 0
        self.y_change = 0
        
        self.x = x
        self.y = y
        self.pos = (self.x,self.y)

        self.couleur_rgb_et_intensite = couleur_intensite
        self.light_radius = radius
        self.light_mask = pygame.Surface((self.game.WIN_WIDTH+50, self.game.WIN_HEIGHT+50), pygame.SRCALPHA)
        self.light_mask.fill((0, 0, 0))
        self.image = self.light_mask

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        for sprite in self.game.all_sprites:
            if isinstance(sprite, Light):
                self.spritedelalumiere = sprite
        self.game.screen.blit(self.image,self.pos)
        
    def update(self):
        
        self.pos = (self.x,self.y)
        pygame.draw.circle(self.light_mask, (self.couleur_rgb_et_intensite), (self.x + self.game.WIN_WIDTH/2+40,self.y + self.game.WIN_HEIGHT/2+40), self.light_radius)
        self.rect = self.light_mask.get_rect(center=(self.game.WIN_WIDTH/2,self.game.WIN_HEIGHT/2))

        self.image = self.light_mask
        self.game.screen.blit(self.image, self.pos, special_flags=pygame.BLEND_MULT)

        self.x += self.x_change
        self.y += self.y_change

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0