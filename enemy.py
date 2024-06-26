from config import *
import math
from HUD import *
from Item import *
from Blocks import *

class AttackEnemy(pygame.sprite.Sprite):
    def __init__(self, game ,x ,y,width, height, number, facing,right_animations,left_animations,up_animations,down_animations):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.attacksenemy
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.facing = facing

        self.x = x
        self.y = y


        self.width = width
        self.height = height
        
        self.animation_loop = 0
        self.animation_number = number

        self.image = self.game.void_spritesheet.get_sprite(0,0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.right_animations = right_animations
        self.down_animations = down_animations
        self.left_animations = left_animations
        self.up_animations = up_animations
        


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
            DROPCHEST = [Potion,Potion,Potion,Scythe,Lustrous_Blade,Heavenly_Wand,Boots_leather,Chest_leather,Pants_leather,Helmet_leather,Ring_copper,Necklace_copper]
            return random.choice(DROPCHEST)
        
        elif DROPCHEST == "DROPCHEST2": # couloir peu commun
            DROPCHEST = [Boots_leather,Chest_leather,Helmet_leather,Pants_leather,Potion,Potion,Potion,Boots_chainmail,Helmet_chainmail,Heavenly_Wand,Celestial_Scepter,Seraphic_Blade,Azure_Blade,Ring_copper,Necklace_copper]
            return random.choice(DROPCHEST)
        
        elif DROPCHEST == "DROPCHEST3": # couloir rare
            DROPCHEST = [Boots_leather,Chest_leather,Helmet_leather,Pants_leather,Potion,Potion,Potion,Boots_chainmail,Chest_chainmail,Pants_chainmail,Helmet_chainmail,Seraphic_Blade,Azure_Blade,Nebula_GreatSword,WintersBallad,Ring_copper,Necklace_copper]
            return random.choice(DROPCHEST)
        
        elif DROPCHEST == "DROPCHEST4": # couloir epic
            DROPCHEST = [Potion,Potion,Potion,Boots_chainmail,Chest_chainmail,Pants_chainmail,Helmet_chainmail,Boots_iron,Helmet_iron,WintersBallad,Crimson_Blade,HellScythe,Ring_emerald,Ring_rubis,Ring_saphir]
            return random.choice(DROPCHEST)
        
        elif DROPCHEST == "DROPCHEST5": # couloir légendaire
            DROPCHEST = [Potion,Potion,Potion,Chest_chainmail,Pants_chainmail,Boots_iron,Helmet_iron,Chest_iron,Pants_iron,HellScythe,Hematite_Blade,Flamestrike_Mallet,Ring_emerald,Ring_rubis,Ring_saphir]
            return random.choice(DROPCHEST)
        
        elif DROPCHEST == "DROPCHEST6": # couloir ???
            DROPCHEST = [Boots_Lava,Chest_Lava,Pants_Lava,Helmet_Lava,Supernova_Scepter]
            return random.choice(DROPCHEST)
        
        elif DROPCHEST == "DROPCHEST7": # salle commun
            DROPCHEST = [Potion,Necklace_emerald,Necklace_rubis,Necklace_saphir,Boots_iron,Chest_iron,Pants_iron,Helmet_iron,GreatSword]
            return random.choice(DROPCHEST)
        
        elif DROPCHEST == "DROPCHEST8":  # salle épique
            DROPCHEST = [Potion,Necklace_emerald,Necklace_rubis,Necklace_saphir,Chest_iron,Pants_iron,GreatSword,SnakeSword]
            return random.choice(DROPCHEST)
        
        elif DROPCHEST == "DROPCHEST9": # salle légendaire
            DROPCHEST = [Potion,Necklace_emerald,Necklace_rubis,Necklace_saphir,Chest_iron,SnakeSword,Potion,Necklace_emerald,Necklace_rubis,Necklace_saphir,Chest_iron,SnakeSword,Potion,Necklace_emerald,Necklace_rubis,Necklace_saphir,Chest_iron,SnakeSword,Boots_Lava,Chest_Lava,Pants_Lava,Helmet_Lava]
            return random.choice(DROPCHEST)
        
    def animate(self):
        direction = self.facing

        if direction == 'up':
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= self.animation_number:
                self.kill()

        if direction == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= self.animation_number:
                self.kill()

        if direction == 'right':
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= self.animation_number:
                self.kill()

        if direction == 'left':
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= self.animation_number:
                self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = 1
        self.health = 10
        self.maxhealth = 10
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7,15)

        self.down_animations = [self.game.enemy_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(68, 2, self.width, self.height)]

        self.up_animations = [self.game.enemy_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.enemy_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.enemy_spritesheet.get_sprite(68, 34, self.width, self.height)]

        self.left_animations = [self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(68, 98, self.width, self.height)]

        self.right_animations = [self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(68, 66, self.width, self.height)]


    def update(self):
        self.movement()
        self.animate()
        self.collide_attack()
        self.speed()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

                    
    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED*self.vitesse
            self.movement_loop -= 1 
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
                
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED*self.vitesse
            self.movement_loop += 1 
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

    def animate(self):
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3,2, self.width, self.height)
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def speed(self):
        if self.invincibility() == False:
            self.vitesse = 1
        else:
            self.vitesse = 0.5

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
class Knight(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

     

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = KNIGHT_SPEED
        self.health = round(KNIGHT_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(KNIGHT_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()
        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = 15

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 200  # Portée de détection du joueur en pixels
        self.is_attacking = False  # Indicateur d'attaque


        self.right_attacksanimations = [self.game.knightattacks_spritesheet.get_sprite(0, 0, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(50, 0 ,50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(100, 0, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(150, 0, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(200, 0, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(250, 0, 50, 40),]

        self.down_attacksanimations = [self.game.knightattacks_spritesheet.get_sprite(0, 40, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(40, 40, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(80, 40, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(120, 40, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(160, 40, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(200, 40, 40, 50),]

        self.left_attacksanimations = [self.game.knightattacks_spritesheet.get_sprite(0, 90, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(50, 90, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(100, 90, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(150, 90, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(200, 90, 50, 40),
                           self.game.knightattacks_spritesheet.get_sprite(250, 90, 50, 40),]

        self.up_attacksanimations = [self.game.knightattacks_spritesheet.get_sprite(0, 130, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(40, 130, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(80, 130, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(120, 130, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(160, 130, 40, 50),
                           self.game.knightattacks_spritesheet.get_sprite(200, 130, 40, 50),]

        self.down_animations = [self.game.knight_spritesheet.get_sprite(0, 0, 52, 47),
                           self.game.knight_spritesheet.get_sprite(52, 0, 52, 47),
                           self.game.knight_spritesheet.get_sprite(104, 0, 52, 47),
                           self.game.knight_spritesheet.get_sprite(156, 0, 52, 47),]

        self.left_animations = [self.game.knight_spritesheet.get_sprite(0, 47, 52, 47),
                           self.game.knight_spritesheet.get_sprite(52, 47, 52, 47),
                           self.game.knight_spritesheet.get_sprite(104, 47, 52, 47),
                           self.game.knight_spritesheet.get_sprite(156, 47, 52, 47),]

        self.right_animations = [self.game.knight_spritesheet.get_sprite(0, 94, 52, 47),
                           self.game.knight_spritesheet.get_sprite(52, 94, 52, 47),
                           self.game.knight_spritesheet.get_sprite(104, 94, 52, 47),
                           self.game.knight_spritesheet.get_sprite(156, 94, 52, 47),]

        self.up_animations = [self.game.knight_spritesheet.get_sprite(0, 141, 52, 47),
                           self.game.knight_spritesheet.get_sprite(52, 141, 52, 47),
                           self.game.knight_spritesheet.get_sprite(104, 141, 52, 47),
                           self.game.knight_spritesheet.get_sprite(156, 141, 52, 47),]
    
        self.down_idleanimations = [self.game.knightidle_spritesheet.get_sprite(0, 0, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(52, 0, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(104, 0, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(156, 0, 52, 47),]

        self.up_idleanimations = [self.game.knightidle_spritesheet.get_sprite(0, 141, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(52, 141, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(104, 141, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(156, 141, 52, 47),]

        self.left_idleanimations = [self.game.knightidle_spritesheet.get_sprite(0, 47, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(52, 47, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(104, 47, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(156, 47, 52, 47),]

        self.right_idleanimations = [self.game.knightidle_spritesheet.get_sprite(0, 94, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(52, 94, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(104, 94, 52, 47),
                           self.game.knightidle_spritesheet.get_sprite(156, 94, 52, 47),]


    def update(self):
        self.collide_attack()
        if self.player:
            distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery))
            
            if distance_to_player <= self.detect_range:
                if distance_to_player >= self.detect_range-165:
                    self.is_attacking = False
                    self.follow_player()
                    self.animate()
                else:
                    self.is_attacking = True
                    self.animateidle()

            else:
                self.is_attacking = False
                self.animateidle()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.attack()

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

                    

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 1
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 1
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 1

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 1

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

    def follow_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 200
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 2000
    
    def attack(self):
        if self.is_attacking == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 1*self.game.multiplicateur_difficulte_attack_enemies
                    if self.facing == 'up':
                        xatt = self.rect.x
                        yatt = self.rect.y - TILESIZE
                    if self.facing == 'down':
                        xatt = self.rect.x
                        yatt = self.rect.y + TILESIZE
                    if self.facing == 'left':
                        xatt = self.rect.x - TILESIZE
                        yatt = self.rect.y
                    if self.facing == 'right':
                        xatt = self.rect.x + TILESIZE
                        yatt = self.rect.y
                    AttackEnemy(self.game,xatt,yatt,52,47,6,self.facing,self.right_attacksanimations,self.left_attacksanimations,self.up_attacksanimations,self.down_attacksanimations)

class AngryMaid(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

        self.angry = False

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = MAID_SPEED
        self.health = round(ANGRY_MAID_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(ANGRY_MAID_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()
        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = 15

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 300  # Portée de détection du joueur en pixels
        self.is_attacking = False  # Indicateur d'attaque

        self.down_animations = [self.game.maid_spritesheet.get_sprite(0, 0, 50, 45),
                           self.game.maid_spritesheet.get_sprite(50, 0, 50, 45),
                           self.game.maid_spritesheet.get_sprite(100, 0, 50, 45),
                           self.game.maid_spritesheet.get_sprite(150, 0, 50, 45),]

        self.left_animations = [self.game.maid_spritesheet.get_sprite(0, 45, 50, 45),
                           self.game.maid_spritesheet.get_sprite(50, 45, 50, 45),
                           self.game.maid_spritesheet.get_sprite(100, 45, 50, 45),
                           self.game.maid_spritesheet.get_sprite(150, 45, 50, 45),]

        self.right_animations = [self.game.maid_spritesheet.get_sprite(0, 90, 50, 45),
                           self.game.maid_spritesheet.get_sprite(50, 90, 50, 45),
                           self.game.maid_spritesheet.get_sprite(100, 90, 50, 45),
                           self.game.maid_spritesheet.get_sprite(150, 90, 50, 45),]

        self.up_animations = [self.game.maid_spritesheet.get_sprite(0, 135, 50, 45),
                           self.game.maid_spritesheet.get_sprite(50, 135, 50, 45),
                           self.game.maid_spritesheet.get_sprite(100, 135, 50, 45),
                           self.game.maid_spritesheet.get_sprite(150, 135, 50, 45),]
        
        self.attackspriteanimation = [self.game.attackmaid_spritesheet.get_sprite(0, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(110, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(220, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(330, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(440, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(550, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(660, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(770, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(880, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(990, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1100, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1210, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1320, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1430, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1540, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1650, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1760, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1870, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(1980, 0, 110, 110),
                                    self.game.attackmaid_spritesheet.get_sprite(2090, 0, 110, 110),]
        
        self.right_attacksanimations = self.attackspriteanimation

        self.down_attacksanimations = self.attackspriteanimation

        self.left_attacksanimations = self.attackspriteanimation

        self.up_attacksanimations = self.attackspriteanimation
    
        self.down_idleanimations = [self.game.maididle_spritesheet.get_sprite(0, 0, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(50, 0, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(100, 0, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(150, 0, 50, 45),]

        self.left_idleanimations = [self.game.maididle_spritesheet.get_sprite(0, 45, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(50, 45, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(100, 45, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(150, 45, 50, 45),]

        self.right_idleanimations = [self.game.maididle_spritesheet.get_sprite(0, 90, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(50, 90, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(100, 90, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(150, 90, 50, 45),]

        self.up_idleanimations = [self.game.maididle_spritesheet.get_sprite(0, 135, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(50, 135, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(100, 135, 50, 45),
                           self.game.maididle_spritesheet.get_sprite(150, 135, 50, 45),]


    def update(self):
        self.collide_attack()
        if self.player:
            distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery))
            if distance_to_player <= self.detect_range:
                if not self.angry:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.angry = True
                if self.angry:
                    if distance_to_player >= self.detect_range-250:
                        self.is_attacking = False
                        self.follow_player(True)
                        self.animate()
                    else: 
                        self.is_attacking = True
                        self.animateidle()
                else:
                    self.follow_player(False)
                    self.is_attacking = False
                    self.animateidle()
            else:
                self.animateidle()
                self.is_attacking = False

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.attack()

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 1
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 1
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 1

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 1

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

    def follow_player(self,justfacing):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            if justfacing:
                self.x_change = -self.vitesse
                self.facing = 'left'
            else:
                self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            if justfacing:
                self.x_change = self.vitesse
                self.facing = 'right'
            else:
                self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            if justfacing:
                self.y_change = -self.vitesse
                self.facing = 'up'
            else:
                self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            if justfacing:
                self.y_change = self.vitesse
                self.facing = 'down'
            else:
                self.facing = 'down'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health < self.healthbar.maxhealth:
                self.angry = True
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 200
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 2000
    
    def attack(self):
        if self.is_attacking == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 2+self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x - TILESIZE
                        yatt = self.rect.y - ((TILESIZE*2)+20)
                    if self.facing == 'down':
                        xatt = self.rect.x - TILESIZE
                        yatt = self.rect.y + (TILESIZE-10)
                    if self.facing == 'left':
                        xatt = self.rect.x - ((TILESIZE*2)+16)
                        yatt = self.rect.y - TILESIZE
                    if self.facing == 'right':
                        xatt = self.rect.x + TILESIZE/2
                        yatt = self.rect.y - TILESIZE
                    AttackEnemy(self.game,xatt,yatt,110,110,20,self.facing,self.right_attacksanimations,self.left_attacksanimations,self.up_attacksanimations,self.down_attacksanimations)

class Slime(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

     

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = SLIME_SPEED
        self.health = round(SLIME_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(SLIME_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()

        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = 15

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 250  # Portée de détection du joueur en pixels
        self.is_attacking = False  # Indicateur d'attaque

        self.right_animations = [self.game.slime_spritesheet.get_sprite(8, 144, 16, 16),
                           self.game.slime_spritesheet.get_sprite(40, 144, 16, 16),
                           self.game.slime_spritesheet.get_sprite(74, 144, 16, 16),
                           self.game.slime_spritesheet.get_sprite(104, 144, 16, 16),]

        self.left_animations = [self.game.slime_spritesheet.get_sprite(8, 176, 16, 16),
                           self.game.slime_spritesheet.get_sprite(40, 176, 16, 16),
                           self.game.slime_spritesheet.get_sprite(74, 176, 16, 16),
                           self.game.slime_spritesheet.get_sprite(104, 176, 16, 16),]

        self.down_animations = [self.game.slime_spritesheet.get_sprite(8, 208, 16, 16),
                           self.game.slime_spritesheet.get_sprite(40, 208, 16, 16),
                           self.game.slime_spritesheet.get_sprite(74, 208, 16, 16),
                           self.game.slime_spritesheet.get_sprite(104, 208, 16, 16),]

        self.up_animations = [self.game.slime_spritesheet.get_sprite(8 ,240, 16, 16),
                           self.game.slime_spritesheet.get_sprite(40, 240, 16, 16),
                           self.game.slime_spritesheet.get_sprite(74, 240, 16, 16),
                           self.game.slime_spritesheet.get_sprite(104, 240, 16, 16),]
        
        
        self.right_attacksanimations = [self.game.slimeattacks_spritesheet.get_sprite(0, 0, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(108, 0, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(216, 0, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(324, 0, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(432, 0, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(540, 0, 108, 64),]

        self.down_attacksanimations = [self.game.slimeattacks_spritesheet.get_sprite(0, 64, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(64, 64, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(128, 64, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(192, 64, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(256, 64, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(320, 64, 64, 108),]

        self.left_attacksanimations = [self.game.slimeattacks_spritesheet.get_sprite(0, 172, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(108, 172, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(216, 172, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(324, 172, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(432, 172, 108, 64),
                                    self.game.slimeattacks_spritesheet.get_sprite(540, 172, 108, 64),]

        self.up_attacksanimations = [self.game.slimeattacks_spritesheet.get_sprite(0, 236, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(64, 236, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(128, 236, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(192, 236, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(256, 236, 64, 108),
                                    self.game.slimeattacks_spritesheet.get_sprite(320, 236, 64, 108),]
    
        self.right_idleanimations = [self.game.slime_spritesheet.get_sprite(8, 19, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(40, 19, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(8, 19, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(40, 19, 16, 13),]

        self.left_idleanimations = [self.game.slime_spritesheet.get_sprite(8, 51, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(40, 51, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(8, 51, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(40, 51, 16, 13)]

        self.down_idleanimations = [self.game.slime_spritesheet.get_sprite(8, 83, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(40, 83, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(8, 83, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(40, 83, 16, 13),]

        self.up_idleanimations = [self.game.slime_spritesheet.get_sprite(8, 115, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(40, 115, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(8, 115, 16, 13),
                                    self.game.slime_spritesheet.get_sprite(40, 115, 16, 13),]


    def update(self):
        self.collide_attack()
        if self.player:
            distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery))
            
            if distance_to_player <= self.detect_range:
                if distance_to_player >= self.detect_range-200:
                    self.is_attacking = False
                    self.follow_player()
                    self.animate()
                else:
                    self.is_attacking = True
                    self.animateidle()

            else:
                self.is_attacking = False
                self.animateidle()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.attack()

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

                    

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

    def follow_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 200
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 2000
    
    def attack(self):
        if self.is_attacking == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 2 +self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x - TILESIZE+5 
                        yatt = self.rect.y - ((TILESIZE*2)+25)
                    if self.facing == 'down':
                        xatt = self.rect.x - (TILESIZE-7)
                        yatt = self.rect.y + (TILESIZE-35)
                    if self.facing == 'left':
                        xatt = self.rect.x - ((TILESIZE*2)+20)
                        yatt = self.rect.y - (TILESIZE-8)
                    if self.facing == 'right':
                        xatt = self.rect.x + (TILESIZE/2)-15
                        yatt = self.rect.y - (TILESIZE-5)
                    AttackEnemy(self.game,xatt,yatt,108,64,6,self.facing,self.right_attacksanimations,self.left_attacksanimations,self.up_attacksanimations,self.down_attacksanimations)

class Beetle(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

     

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = BETTLE_SPEED
        self.health = round(BEETLE_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(BEETLE_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()
        self.derniertemps3 = pygame.time.get_ticks()
        self.derniertemps4 = pygame.time.get_ticks()
        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.is_loaded = False

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = 15

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 250  # Portée de détection du joueur en pixels
        self.is_attacking = False  # Indicateur d'attaque

        self.down_animations = [self.game.beetle_spritesheet.get_sprite(0, 0, 42,39),
                           self.game.beetle_spritesheet.get_sprite(42, 0, 42,39),
                           self.game.beetle_spritesheet.get_sprite(84, 0, 42,39),
                           self.game.beetle_spritesheet.get_sprite(126, 0, 42,39),]

        self.left_animations = [self.game.beetle_spritesheet.get_sprite(0, 39, 42,39),
                           self.game.beetle_spritesheet.get_sprite(42, 39, 42,39),
                           self.game.beetle_spritesheet.get_sprite(84, 39, 42,39),
                           self.game.beetle_spritesheet.get_sprite(126, 39, 42,39),]

        self.right_animations = [self.game.beetle_spritesheet.get_sprite(0, 78, 42,39),
                           self.game.beetle_spritesheet.get_sprite(42, 78, 42,39),
                           self.game.beetle_spritesheet.get_sprite(84, 78, 42,39),
                           self.game.beetle_spritesheet.get_sprite(126, 78, 42,39),]

        self.up_animations = [self.game.beetle_spritesheet.get_sprite(0 ,117, 42,39),
                           self.game.beetle_spritesheet.get_sprite(42, 117, 42,39),
                           self.game.beetle_spritesheet.get_sprite(84, 117, 42,39),
                           self.game.beetle_spritesheet.get_sprite(126, 117, 42,39),]
        
        
        self.left_attacksanimations = [self.game.beetleattacks_spritesheet.get_sprite(0, 0, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200, 0, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*2, 0, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*3, 0, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*4, 0, 200, 32),]

        self.up_attacksanimations = [self.game.beetleattacks_spritesheet.get_sprite(0, 32, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(32, 32, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(64, 32, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(96, 32, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(128, 32, 32, 200),]

        self.right_attacksanimations = [self.game.beetleattacks_spritesheet.get_sprite(0, 232, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200, 232, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*2, 232, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*3, 232, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*4, 232, 200, 32),]


        self.down_attacksanimations = [self.game.beetleattacks_spritesheet.get_sprite(0, 264, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(32, 264, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(64, 264, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(96, 264, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(128, 264, 32, 200),]
        

        self.right_circleanimation = [self.game.greencircle_spritesheet.get_sprite(0, 0, 160, 200),
self.game.greencircle_spritesheet.get_sprite(160, 0, 160, 200),
self.game.greencircle_spritesheet.get_sprite(320, 0, 160, 200),
self.game.greencircle_spritesheet.get_sprite(480, 0, 160, 200),
self.game.greencircle_spritesheet.get_sprite(0, 0, 160, 200),
self.game.greencircle_spritesheet.get_sprite(160, 0, 160, 200),
self.game.greencircle_spritesheet.get_sprite(320, 0, 160, 200),
self.game.greencircle_spritesheet.get_sprite(480, 0, 160, 200),]

        self.down_circleanimation = [self.game.greencircle_spritesheet.get_sprite(0, 200, 200, 160),
self.game.greencircle_spritesheet.get_sprite(200, 200, 200, 160),
self.game.greencircle_spritesheet.get_sprite(400, 200, 200, 160),
self.game.greencircle_spritesheet.get_sprite(600, 200, 200, 160),
self.game.greencircle_spritesheet.get_sprite(0, 200, 200, 160),
self.game.greencircle_spritesheet.get_sprite(200, 200, 200, 160),
self.game.greencircle_spritesheet.get_sprite(400, 200, 200, 160),
self.game.greencircle_spritesheet.get_sprite(600, 200, 200, 160),]

        self.left_circleanimation = [self.game.greencircle_spritesheet.get_sprite(0, 360, 160, 200),
self.game.greencircle_spritesheet.get_sprite(160, 360, 160, 200),
self.game.greencircle_spritesheet.get_sprite(320, 360, 160, 200),
self.game.greencircle_spritesheet.get_sprite(480, 360, 160, 200),
self.game.greencircle_spritesheet.get_sprite(0, 360, 160, 200),
self.game.greencircle_spritesheet.get_sprite(160, 360, 160, 200),
self.game.greencircle_spritesheet.get_sprite(320, 360, 160, 200),
self.game.greencircle_spritesheet.get_sprite(480, 360, 160, 200),]

        self.up_circleanimation = [self.game.greencircle_spritesheet.get_sprite(0, 560, 200, 160),
self.game.greencircle_spritesheet.get_sprite(200, 560, 200, 160),
self.game.greencircle_spritesheet.get_sprite(400, 560, 200, 160),
self.game.greencircle_spritesheet.get_sprite(600, 560, 200, 160),
self.game.greencircle_spritesheet.get_sprite(0, 560, 200, 160),
self.game.greencircle_spritesheet.get_sprite(200, 560, 200, 160),
self.game.greencircle_spritesheet.get_sprite(400, 560, 200, 160),
self.game.greencircle_spritesheet.get_sprite(600, 560, 200, 160),]


        self.down_idleanimations = [self.game.beetleidle_spritesheet.get_sprite(0, 0, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(42, 0, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(84, 0, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(126, 0, 42,39),]

        self.left_idleanimations = [self.game.beetleidle_spritesheet.get_sprite(0, 39, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(42, 39, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(84, 39, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(126, 39, 42,39),]

        self.right_idleanimations = [self.game.beetleidle_spritesheet.get_sprite(0, 78, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(42, 78, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(84, 78, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(126, 78, 42,39),]

        self.up_idleanimations = [self.game.beetleidle_spritesheet.get_sprite(0 ,117, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(42, 117, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(84, 117, 42,39),
                           self.game.beetleidle_spritesheet.get_sprite(126, 117, 42,39),]


    def update(self):
        self.collide_attack()
        if self.clicktime2() == False:
            if self.attacktime2() == False:
                self.derniertemps4 = pygame.time.get_ticks()
                self.derniertemps3 = pygame.time.get_ticks()
                self.game.player.enemyattacks = 2+self.game.multiplicateur_difficulte_attack_enemies 
                if self.facing == 'up':
                    xatt = self.rect.x -75
                    yatt = self.rect.y -55
                if self.facing == 'down':
                    xatt = self.rect.x -75
                    yatt = self.rect.y -55

                if self.facing == 'left':
                    xatt = self.rect.x -55
                    yatt = self.rect.y -75

                if self.facing == 'right':
                    xatt = self.rect.x -55
                    yatt = self.rect.y -75

                AttackEnemy(self.game,xatt,yatt,160,200,8,self.facing,self.right_circleanimation,self.left_circleanimation,self.up_circleanimation,self.down_circleanimation)

        if self.player:
            distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery)) 
            if distance_to_player <= self.detect_range:
                if distance_to_player >= self.detect_range-100:
                    self.is_attacking = False
                    self.follow_player()
                    self.animate()
                else:
                    self.is_attacking = True
                    self.animateidle()

            else:
                self.is_attacking = False
                self.animateidle()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.attack()

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

                    

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

    def follow_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 200
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 2000
    
    def attacktime2(self):
        return self.derniertemps3 > pygame.time.get_ticks() - 300
    
    def clicktime2(self):
        return self.derniertemps4 > pygame.time.get_ticks() - 1000
    
    def attack(self):
        if self.is_attacking == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 2+self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x +5
                        yatt = self.rect.y - 200
                    if self.facing == 'down':
                        xatt = self.rect.x +5
                        yatt = self.rect.y + 45

                    if self.facing == 'left':
                        xatt = self.rect.x -200
                        yatt = self.rect.y

                    if self.facing == 'right':
                        xatt = self.rect.x + TILESIZE
                        yatt = self.rect.y

                    AttackEnemy(self.game,xatt,yatt,200,32,5,self.facing,self.right_attacksanimations,self.left_attacksanimations,self.up_attacksanimations,self.down_attacksanimations)

class Boss(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.attaque_en_cours = False

        self.etage = tilemap

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = BOSS_SPEED
        self.health = round(BOSS_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(BOSS_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()
        self.derniertemps3 = pygame.time.get_ticks()
        self.derniertemps4 = pygame.time.get_ticks()
        self.tempsavancer = pygame.time.get_ticks()
        self.invocation_times = pygame.time.get_ticks()
        self.approach_times = pygame.time.get_ticks()
        self.phase1 = True
        self.phase2 = False
        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0 , 64,70)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.is_loaded = False
        self.wait = False
        self.facing = "left"

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = 50

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 600  # Portée de détection du joueur en pixels
        self.is_attacking = False  # Indicateur d'attaque

        self.down_animations = [
            self.game.boss_spritesheet.get_sprite(0, 120, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 120, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 120, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 120, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 120, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 120, 64, 70),
        ]

        self.left_animations = [
            self.game.boss_spritesheet.get_sprite(0, 693, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 693, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 693, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 693, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 693, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 693, 64, 70),
        ]

        self.right_animations = [
            self.game.boss_spritesheet.get_sprite(0, 2303, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 2303, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 2303, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 2303, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 2303, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 2303, 64, 70),
        ]

        self.up_animations = [
            self.game.boss_spritesheet.get_sprite(0, 1272, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 1272, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 1272, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 1272, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 1272, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 1272, 64, 70),
        ]
        



        self.down_idleanimations = [
            self.game.boss_spritesheet.get_sprite(0, 22, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 22, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 22, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 22, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 22, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 22, 64, 70),
        ]

        self.left_idleanimations = [
            self.game.boss_spritesheet.get_sprite(0, 598, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 598, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 598, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 598, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 598, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 598, 64, 70),
        ]

        self.right_idleanimations = [
            self.game.boss_spritesheet.get_sprite(0, 1750, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 1750, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 1750, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 1750, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 1750, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 1750, 64, 70),
        ]

        self.up_idleanimations = [
            self.game.boss_spritesheet.get_sprite(0, 1174, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 1174, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 1174, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 1174, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 1174, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 1174, 64, 70),
        ]





        self.attack_close_down = [
            self.game.boss_spritesheet.get_sprite(0, 213, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 213, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 213, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 213, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 213, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 213, 64, 70),
        ]

        self.attack_close_up = [
            self.game.boss_spritesheet.get_sprite(0, 1365, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 1365, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 1365, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 1365, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 1365, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 1365, 64, 70),
        ]

        self.attack_close_left = [
            self.game.boss_spritesheet.get_sprite(0, 789, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 789, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 789, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 789, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 789, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 789, 64, 70),
        ]

        self.attack_close_right =[
            self.game.boss_spritesheet.get_sprite(0, 1941, 64, 70),
            self.game.boss_spritesheet.get_sprite(64, 1941, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*2, 1941, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*3, 1941, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*4, 1941, 64, 70),
            self.game.boss_spritesheet.get_sprite(64*5, 1941, 64, 70),
        ]




        self.attack_medium_down = [self.game.bosscircle_spritesheet.get_sprite(0, 64, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(64, 64, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(128, 64, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(192, 64, 64, 64),]

        self.attack_medium_up =[self.game.bosscircle_spritesheet.get_sprite(0, 192, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(64, 192, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(128, 192, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(192, 192, 64, 64),]

        self.attack_medium_left = [self.game.bosscircle_spritesheet.get_sprite(0, 128, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(64, 128, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(128, 128, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(192, 128, 64, 64),]

        self.attack_medium_right = [self.game.bosscircle_spritesheet.get_sprite(0, 0, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(64, 0, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(128, 0, 64, 64),
self.game.bosscircle_spritesheet.get_sprite(192, 0, 64, 64),]
        
        

        self.attack_medium_right_proj = [self.game.bossprojectile_spritesheet.get_sprite(0, 0, 210, 64),
self.game.bossprojectile_spritesheet.get_sprite(210, 0, 210, 64),
self.game.bossprojectile_spritesheet.get_sprite(420, 0, 210, 64),
self.game.bossprojectile_spritesheet.get_sprite(630, 0, 210, 64),
self.game.bossprojectile_spritesheet.get_sprite(840, 0, 210, 64),]

        self.attack_medium_down_proj = [self.game.bossprojectile_spritesheet.get_sprite(0, 64, 64, 210),
self.game.bossprojectile_spritesheet.get_sprite(64, 64, 64, 210),
self.game.bossprojectile_spritesheet.get_sprite(128, 64, 64, 210),
self.game.bossprojectile_spritesheet.get_sprite(192, 64, 64, 210),
self.game.bossprojectile_spritesheet.get_sprite(256, 64, 64, 210),]

        self.attack_medium_left_proj = [self.game.bossprojectile_spritesheet.get_sprite(0, 274, 210, 64),
self.game.bossprojectile_spritesheet.get_sprite(210, 274, 210, 64),
self.game.bossprojectile_spritesheet.get_sprite(420, 274, 210, 64),
self.game.bossprojectile_spritesheet.get_sprite(630, 274, 210, 64),
self.game.bossprojectile_spritesheet.get_sprite(840, 274, 210, 64),]

        self.attack_medium_up_proj = [self.game.bossprojectile_spritesheet.get_sprite(0, 338, 64, 210),
self.game.bossprojectile_spritesheet.get_sprite(64, 338, 64, 210),
self.game.bossprojectile_spritesheet.get_sprite(128, 338, 64, 210),
self.game.bossprojectile_spritesheet.get_sprite(192, 338, 64, 210),
self.game.bossprojectile_spritesheet.get_sprite(256, 338, 64, 210),]
        


        self.teleportation = [self.game.impactwhite_spritesheet.get_sprite(0, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(64, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(128, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(192, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(256, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(320, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(384, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(448, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(0, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(64, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(128, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(192, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(256, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(320, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(384, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(448, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(0, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(64, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(128, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(192, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(256, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(320, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(384, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(448, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(0, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(64, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(128, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(192, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(256, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(320, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(384, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(448, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(0, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(64, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(128, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(192, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(256, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(320, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(384, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(448, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(0, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(64, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(128, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(192, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(256, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(320, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(384, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(448, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(0, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(64, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(128, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(192, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(256, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(320, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(384, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(448, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(0, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(64, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(128, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(192, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(256, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(320, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(384, 1408, 64, 64),
self.game.impactwhite_spritesheet.get_sprite(448, 1408, 64, 64),]

        self.teleportation_down = self.teleportation
        self.teleportation_up = self.teleportation
        self.teleportation_left = self.teleportation
        self.teleportation_right = self.teleportation

        self.attacklong1 = [self.game.impactblue_spritesheet.get_sprite(0, 1600, 64, 64),
self.game.impactblue_spritesheet.get_sprite(64, 1600, 64, 64),
self.game.impactblue_spritesheet.get_sprite(128, 1600, 64, 64),
self.game.impactblue_spritesheet.get_sprite(192, 1600, 64, 64),
self.game.impactblue_spritesheet.get_sprite(256, 1600, 64, 64),
self.game.impactblue_spritesheet.get_sprite(320, 1600, 64, 64),
self.game.impactblue_spritesheet.get_sprite(384, 1600, 64, 64),
self.game.impactblue_spritesheet.get_sprite(448, 1600, 64, 64),
self.game.impactblue_spritesheet.get_sprite(512, 1600, 64, 64),]

        self.attack_long_down1 = self.attacklong1
        self.attack_long_up1 = self.attacklong1
        self.attack_long_right1 = self.attacklong1
        self.attack_long_left1 = self.attacklong1
    
        self.attacklong2 = [self.game.impactpurple_spritesheet.get_sprite(0, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(64, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(128, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(192, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(256, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(320, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(384, 704, 64, 64),]

        self.attack_long_down2 = self.attacklong2
        self.attack_long_up2 = self.attacklong2
        self.attack_long_right2 = self.attacklong2
        self.attack_long_left2 = self.attacklong2

        self.effetcollidelava = [self.game.impactpurple_spritesheet.get_sprite(0, 64, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(64, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(128, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(192, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(256, 704, 64, 64),
self.game.impactpurple_spritesheet.get_sprite(320, 704, 64, 64),]

        self.effetcollidelavadown = self.effetcollidelava
        self.effetcollidelavaup = self.effetcollidelava
        self.effetcollidelavaright = self.effetcollidelava
        self.effetcollidelavaleft = self.effetcollidelava

        for sprite in self.game.all_sprites:
            if isinstance(sprite, Boss):
                self.spriteduboss = sprite


    def update(self):
        self.collide_attack()
        self.look_at_player()
        self.animateidle()
        if self.wait == False:
            if self.player:
                distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery)) 
                if distance_to_player <= self.detect_range-550:
                    self.attackclose()
                    
                elif distance_to_player <= self.detect_range-400:
                    self.attackmedium()
                    self.move_away_from_player()
                elif distance_to_player <= self.detect_range:
                    self.attacklong()
                    self.approach_times = pygame.time.get_ticks()
                    if self.approach_time:
                        self.approach_player()


                    
        if self.wait == True:
            self.change_map()
                    

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0 

    def approach_time(self):
        return self.approach_times > pygame.time.get_ticks() - 2500
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            if direction == "x":
                if hits:
                    if self.x_change > 0:
                        self.rect.x = hits[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hits[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hits[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hits[0].rect.bottom

    def collide_lava(self):
        hits = pygame.sprite.spritecollide(self, self.game.lava, False)
        if hits:
            if self.facing == 'up':
                xatt = self.rect.x 
                yatt = self.rect.y 

            if self.facing == 'down':
                xatt = self.rect.x
                yatt = self.rect.y

            if self.facing == 'left':
                xatt = self.rect.x -200
                yatt = self.rect.y

            if self.facing == 'right':
                xatt = self.rect.x + TILESIZE
                yatt = self.rect.y
            AttackEnemy(self.game,xatt,yatt,64,64,6,self.facing,self.effetcollidelavaright,self.effetcollidelavaleft,self.effetcollidelavaup,self.effetcollidelavadown)

                    

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0

    def approach_player(self):
        # Fait en sorte que le boss se rapproche du joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centery < self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'

    def move_away_from_player(self):
        # Fait en sorte que le boss s'éloigne du joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'
        elif self.player.rect.centery < self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 175:
                if self.phase1 == True:
                    self.wait = True
                    xatt = self.rect.x
                    yatt = self.rect.y+22
                    self.derniertemps4 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks() 
                    self.game.player.enemyattacks = 2+self.game.multiplicateur_difficulte_attack_enemies 
                    self.derniertempsloading = pygame.time.get_ticks()
                    AttackEnemy(self.game,xatt,yatt,64,64,64,self.facing,self.teleportation_right,self.teleportation_left,self.teleportation_up,self.teleportation_down)
                    self.invocation_times = pygame.time.get_ticks()
                    self.phase2 = True
                    self.phase1 = False


            if self.healthbar.health <= 90:
                if self.phase2 == True:
                    self.wait = True
                    xatt = self.rect.x
                    yatt = self.rect.y+22
                    self.derniertemps4 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks() 
                    self.game.player.enemyattacks = 2+self.game.multiplicateur_difficulte_attack_enemies 
                    self.derniertempsloading = pygame.time.get_ticks()
                    AttackEnemy(self.game,xatt,yatt,64,64,64,self.facing,self.teleportation_right,self.teleportation_left,self.teleportation_up,self.teleportation_down)
                    self.invocation_times = pygame.time.get_ticks()
                    self.phase2 = False

            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.kill()
                self.game.win = True

    def change_map(self):
        if self.invocation_time() == False:
            for sprite in self.game .all_sprites:
                if (self.game.player.spritedujoueur != sprite) and (self.spriteduboss != sprite) and (self.game.player.light.spritedelalumiere != sprite) and (self.game.player.healthbar.spriteduhealthbar != sprite) and (self.game.player.etage.spriteduetage != sprite) and (self.game.player.potion.spriteduhubpotion!= sprite) and (self.game.player.epee.spriteduEpeeHUD != sprite) and (self.game.player.helmet.spriteduCasqueHUD != sprite) and (self.game.player.chest.spriteduChestHUD != sprite) and (self.game.player.pants.spriteduPantsHUD != sprite) and (self.game.player.boots.spritedesBootsHUD != sprite) and (self.game.player.necklace.spriteNecklaceHUD != sprite) and (self.game.player.ring.spriteRingHUD != sprite) and (self.game.player.ranged.spriteRangeHUD != sprite) and (self.game.player.afficheequipped.spriteduafficheequipped != sprite) and (self.game.player.afficheitem.spriteduafficheitem != sprite) and (self.game.hitbox.spriteduplayerhitbox != sprite):
                    sprite.kill()
            if self.healthbar.health <= 187:
                self.newmap = MapsBossPhase2.pop(MapsBossPhase2.index(random.choice(MapsBossPhase2)))
            if self.healthbar.health <= 90 and self.phase2:
                self.newmap = MapsBossPhase3.pop(MapsBossPhase3.index(random.choice(MapsBossPhase3)))
            self.game.createTilemapboss(self.newmap,True)
            self.wait = False

    def invocation_time(self):
        return self.invocation_times > pygame.time.get_ticks() - 2500

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 2000
    
    def attacktime2(self):
        return self.derniertemps3 > pygame.time.get_ticks() - 300
    
    def attackclose(self):
        if self.clicktime() == False:
            self.derniertemps2 = pygame.time.get_ticks()
            self.game.player.enemyattacks = 2+self.game.multiplicateur_difficulte_attack_enemies 
            if self.facing == 'up':
                xatt = self.rect.x
                yatt = self.rect.y - 100
            if self.facing == 'down':
                xatt = self.rect.x
                yatt = self.rect.y + 50

            if self.facing == 'left':
                xatt = self.rect.x -50
                yatt = self.rect.y

            if self.facing == 'right':
                xatt = self.rect.x + 50
                yatt = self.rect.y

            AttackEnemy(self.game,xatt,yatt,50,50,6,self.facing,self.attack_close_right,self.attack_close_left,self.attack_close_up,self.attack_close_down)
    
    def attackmedium(self):
        if not self.clicktime2() and not self.attaque_en_cours:
            if self.facing == 'up':
                xatt = self.rect.x 
                yatt = self.rect.y 

            if self.facing == 'down':
                xatt = self.rect.x
                yatt = self.rect.y

            if self.facing == 'left':
                xatt = self.rect.x -200
                yatt = self.rect.y

            if self.facing == 'right':
                xatt = self.rect.x + TILESIZE
                yatt = self.rect.y
            self.derniertemps4 = pygame.time.get_ticks()
            self.derniertemps1 = pygame.time.get_ticks() 
            self.game.player.enemyattacks = 2+self.game.multiplicateur_difficulte_attack_enemies 

            self.derniertempsloading = pygame.time.get_ticks()
            AttackEnemy(self.game,xatt,yatt,64,64,4,self.facing,self.attack_medium_right,self.attack_medium_left,self.attack_medium_up,self.attack_medium_down)
            self.attaque_en_cours = True
        if self.attaque_en_cours == True:
            if self.attacktime() == False:
                if self.facing == 'up':
                    xatt = self.rect.x
                    yatt = self.rect.y - 200

                if self.facing == 'down':
                    xatt = self.rect.x
                    yatt = self.rect.y + 45

                if self.facing == 'left':
                    xatt = self.rect.x -200
                    yatt = self.rect.y
                if self.facing == 'right':
                    xatt = self.rect.x + TILESIZE
                    yatt = self.rect.y
                AttackEnemy(self.game,xatt,yatt,210,64,5,self.facing,self.attack_medium_left_proj,self.attack_medium_right_proj,self.attack_medium_down_proj,self.attack_medium_up_proj)
                self.attaque_en_cours = False
                self.derniertemps4 = pygame.time.get_ticks()

    def clicktime2(self):
        return self.derniertemps4 > pygame.time.get_ticks() - 1000
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 150
    
    def advance_time(self):
        return self.tempsavancer > pygame.time.get_ticks() - 2500
    
    def attacklong(self):
        choix = random.choice([1,2])
        if self.clicktime() == False:
            self.derniertemps2 = pygame.time.get_ticks()
            self.game.player.enemyattacks = 2+self.game.multiplicateur_difficulte_attack_enemies 

            if choix == 1:
                if self.facing == 'up':
                    xatt = self.game.player.rect.x -15
                    yatt = self.game.player.rect.y -40

                if self.facing == 'down':
                    xatt = self.game.player.rect.x -5
                    yatt = self.game.player.rect.y -35

                if self.facing == 'left':
                    xatt = self.game.player.rect.x -15
                    yatt = self.game.player.rect.y -30

                if self.facing == 'right':
                    xatt = self.game.player.rect.x  -40
                    yatt = self.game.player.rect.y  -50
                AttackEnemy(self.game,xatt,yatt,64,64,9,self.facing,self.attack_long_right1,self.attack_long_left1,self.attack_long_up1,self.attack_long_down1)
            elif choix == 2:
                if self.facing == 'up':
                    xatt = self.game.player.rect.x -10
                    yatt = self.game.player.rect.y -10

                if self.facing == 'down':
                    xatt = self.game.player.rect.x -10
                    yatt = self.game.player.rect.y -10

                if self.facing == 'left':
                    xatt = self.game.player.rect.x - 10
                    yatt = self.game.player.rect.y - 20

                if self.facing == 'right':
                    xatt = self.game.player.rect.x -20
                    yatt = self.game.player.rect.y -10
                AttackEnemy(self.game,xatt,yatt,64,64,7,self.facing,self.attack_long_right2,self.attack_long_left2,self.attack_long_up2,self.attack_long_down2)



    def look_at_player(self):
        # Calcule la direction entre le boss et le joueur
        player_dx = self.player.rect.centerx - self.rect.centerx
        player_dy = self.player.rect.centery - self.rect.centery
        angle = math.degrees(math.atan2(-player_dy, player_dx))

        # Ajuste l'attribut "facing" en fonction de l'angle
        if -45 <= angle <= 45:
            self.facing = "right"
        elif 45 < angle <= 135:
            self.facing = "up"
        elif 135 < angle <= 180 or -180 <= angle <= -135:
            self.facing = "left"
        elif -135 < angle <= -45:
            self.facing = "down"

class Multicolor_Man(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

     

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = MULTICOLOR_MAN_SPEED
        self.health = round(MULTICOLOR_MAN_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(MULTICOLOR_MAN_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()

        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.animation_loopshort = 1
        self.animation_looplong = 1
        self.animation_loopidle = 1

        self.movement_loop = 0
        self.max_travel = 15

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 250  # Portée de détection du joueur en pixels
        self.is_attackingshort = False
        self.is_attackinglong = False

        self.right_animations = [self.game.multicolorwalk_spritesheet.get_sprite(576, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(624, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(672, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(720, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(768, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(816, 0, 48, 48),]

        self.left_animations = [self.game.multicolorwalk_spritesheet.get_sprite(864, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(912, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(960, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(1008, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(1056, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(1104, 0, 48, 48),]

        self.down_animations = [self.game.multicolorwalk_spritesheet.get_sprite(288, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(336, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(384, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(432, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(480, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(528, 0, 48, 48),]

        self.up_animations = [self.game.multicolorwalk_spritesheet.get_sprite(0 ,0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(48, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(96, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(144, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(192, 0, 48, 48),
                           self.game.multicolorwalk_spritesheet.get_sprite(240, 0, 48, 48),]
        
        
        self.right_idleanimations = [self.game.multicoloridle_spritesheet.get_sprite(192, 0, 48, 48),
                                    self.game.multicoloridle_spritesheet.get_sprite(240, 0, 48, 48),]

        self.left_idleanimations = [self.game.multicoloridle_spritesheet.get_sprite(288, 0, 48,48),
                                    self.game.multicoloridle_spritesheet.get_sprite(336, 0, 48,48),]

        self.down_idleanimations = [self.game.multicoloridle_spritesheet.get_sprite(0, 0, 48,48),
                                    self.game.multicoloridle_spritesheet.get_sprite(48, 0, 48,48),]

        self.up_idleanimations = [self.game.multicoloridle_spritesheet.get_sprite(96, 0, 48,48),
                                    self.game.multicoloridle_spritesheet.get_sprite(144, 0, 48,48),]
        

        
        self.up_attacksanimation = [self.game.purplecircleattack_spritesheet.get_sprite(0, 0, 35, 32),
                                    self.game.purplecircleattack_spritesheet.get_sprite(35, 0, 35, 32),
                                    self.game.purplecircleattack_spritesheet.get_sprite(70, 0, 35, 32),
                                    self.game.purplecircleattack_spritesheet.get_sprite(105, 0, 35, 32),
                                    self.game.purplecircleattack_spritesheet.get_sprite(140, 0, 35, 32),]

        self.right_attacksanimation = [self.game.purplecircleattack_spritesheet.get_sprite(0, 32, 32, 35),
                                    self.game.purplecircleattack_spritesheet.get_sprite(32, 32, 32, 35),
                                    self.game.purplecircleattack_spritesheet.get_sprite(64, 32, 32, 35),
                                    self.game.purplecircleattack_spritesheet.get_sprite(96, 32, 32, 35),
                                    self.game.purplecircleattack_spritesheet.get_sprite(128, 32, 32, 35),]

        self.down_attacksanimation = [self.game.purplecircleattack_spritesheet.get_sprite(0, 67, 35, 32),
                                    self.game.purplecircleattack_spritesheet.get_sprite(35, 67, 35, 32),
                                    self.game.purplecircleattack_spritesheet.get_sprite(70, 67, 35, 32),
                                    self.game.purplecircleattack_spritesheet.get_sprite(105, 67, 35, 32),
                                    self.game.purplecircleattack_spritesheet.get_sprite(140, 67, 35, 32),]

        self.left_attacksanimation = [self.game.purplecircleattack_spritesheet.get_sprite(0, 99, 32, 35),
                                self.game.purplecircleattack_spritesheet.get_sprite(32, 99, 32, 35),
                                self.game.purplecircleattack_spritesheet.get_sprite(64, 99, 32, 35),
                                self.game.purplecircleattack_spritesheet.get_sprite(96, 99, 32, 35),
                                self.game.purplecircleattack_spritesheet.get_sprite(128, 99, 32, 35),]
        
        self.right_attacksanimationpos = [self.game.multicolorattackshort_spritesheet.get_sprite(288, 0, 48, 48),
                                    self.game.multicolorattackshort_spritesheet.get_sprite(336, 0, 48, 48),
                                    self.game.multicolorattackshort_spritesheet.get_sprite(384, 0, 48, 48),]

        self.down_attacksanimationpos = [self.game.multicolorattackshort_spritesheet.get_sprite(0, 0, 48, 48),
                                    self.game.multicolorattackshort_spritesheet.get_sprite(48, 0, 48, 48),
                                    self.game.multicolorattackshort_spritesheet.get_sprite(96, 0, 48, 48),]

        self.left_attacksanimationpos = [self.game.multicolorattackshort_spritesheet.get_sprite(432, 0, 48, 48),
                                    self.game.multicolorattackshort_spritesheet.get_sprite(480, 0, 48, 48),
                                    self.game.multicolorattackshort_spritesheet.get_sprite(328, 0, 48, 48),]

        self.up_attacksanimationpos = [self.game.multicolorattackshort_spritesheet.get_sprite(144, 0, 48, 48),
                                self.game.multicolorattackshort_spritesheet.get_sprite(192, 0, 48, 48),
                                self.game.multicolorattackshort_spritesheet.get_sprite(240, 0, 48, 48),]
        


        self.longattack = [self.game.fireground_spritesheet.get_sprite(0, 0, 48, 32),
self.game.fireground_spritesheet.get_sprite(48, 0, 48, 32),
self.game.fireground_spritesheet.get_sprite(96, 0, 48, 32),
self.game.fireground_spritesheet.get_sprite(144, 0, 48, 32),]

        self.up_attacksanimationlong = self.longattack
        self.right_attacksanimationlong = self.longattack
        self.down_attacksanimationlong = self.longattack
        self.left_attacksanimationlong = self.longattack

        self.right_attackslonganimationpos = [self.game.multicolorattacklong_spritesheet.get_sprite(576, 0, 48, 48),
                                    self.game.multicolorattacklong_spritesheet.get_sprite(624, 0, 48, 48),]

        self.down_attackslonganimationpos = [self.game.multicolorattacklong_spritesheet.get_sprite(384, 0, 48, 48),
                                    self.game.multicolorattacklong_spritesheet.get_sprite(432, 0, 48, 48),]

        self.left_attackslonganimationpos = [self.game.multicolorattacklong_spritesheet.get_sprite(432, 0, 48, 48),
                                    self.game.multicolorattacklong_spritesheet.get_sprite(480, 0, 48, 48),]

        self.up_attackslonganimationpos = [self.game.multicolorattacklong_spritesheet.get_sprite(480, 0, 48, 48),
                                self.game.multicolorattacklong_spritesheet.get_sprite(528, 0, 48, 48),]

    def update(self):
        self.collide_attack()
        if self.player:
            distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery))
            if distance_to_player <= self.detect_range:
                if distance_to_player <= self.detect_range-150:
                    self.is_attackinglong = False
                    self.is_attackingshort = True
                    self.animateattackshort()
                    self.away_from_player()

                elif distance_to_player <= self.detect_range:
                    if distance_to_player >= self.detect_range-125:
                        self.follow_player()
                        self.animate()
                    else:
                        self.is_attackingshort = False
                        self.is_attackinglong = True
                        self.animateattacklong()
            else:
                self.is_attackingshort = False
                self.is_attackinglong = False
                self.animateidle()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.attackshort()
        self.attacklong()

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

                    

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 6:
                self.animation_loop = 0

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 2:
                self.animation_loopidle = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 2:
                self.animation_loopidle = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 2:
                self.animation_loopidle = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 2:
                self.animation_loopidle = 0

    def animateattackshort(self):
        if self.facing == "down":
            self.image = self.down_attacksanimationpos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 3:
                self.animation_loopshort = 0
            
        if self.facing == "left":
            self.image = self.left_attacksanimationpos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 3:
                self.animation_loopshort = 0
                    
        if self.facing == "right":
            self.image = self.right_attacksanimationpos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 3:
                self.animation_loopshort = 0

        if self.facing == "up":
            self.image = self.up_attacksanimationpos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 3:
                self.animation_loopshort = 0


    def animateattacklong(self):
        if self.facing == "down":
            self.image = self.down_attackslonganimationpos[math.floor(self.animation_looplong)]
            self.animation_looplong += 0.1
            if self.animation_looplong >= 2:
                self.animation_looplong = 0
            
        if self.facing == "left":
            self.image = self.left_attackslonganimationpos[math.floor(self.animation_looplong)]
            self.animation_looplong += 0.1
            if self.animation_looplong >= 2:
                self.animation_looplong = 0
                    
        if self.facing == "right":
            self.image = self.right_attackslonganimationpos[math.floor(self.animation_looplong)]
            self.animation_looplong += 0.1
            if self.animation_looplong >= 2:
                self.animation_looplong = 0

        if self.facing == "up":
            self.image = self.up_attackslonganimationpos[math.floor(self.animation_looplong)]
            self.animation_looplong += 0.1
            if self.animation_looplong >= 2:
                self.animation_looplong = 0

    def away_from_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'down'

    def follow_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 200
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 500
    
    def attackshort(self):
        if self.is_attackingshort == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 2 +self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x
                        yatt = self.rect.y - 50
                    if self.facing == 'down':
                        xatt = self.rect.x 
                        yatt = self.rect.y + 50
                    if self.facing == 'left':
                        xatt = self.rect.x - 50
                        yatt = self.rect.y
                    if self.facing == 'right':
                        xatt = self.rect.x + 50
                        yatt = self.rect.y
                    AttackEnemy(self.game,xatt,yatt,40,40,5,self.facing,self.right_attacksanimation,self.left_attacksanimation,self.up_attacksanimation,self.down_attacksanimation)


    def attacklong(self):
        if self.is_attackinglong == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 2 +self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x
                        yatt = self.rect.y - 100
                    if self.facing == 'down':
                        xatt = self.rect.x 
                        yatt = self.rect.y + 100
                    if self.facing == 'left':
                        xatt = self.rect.x - 100
                        yatt = self.rect.y
                    if self.facing == 'right':
                        xatt = self.rect.x + 100
                        yatt = self.rect.y
                    AttackEnemy(self.game,xatt,yatt,40,40,4,self.facing,self.right_attacksanimationlong,self.left_attacksanimationlong,self.up_attacksanimationlong,self.down_attacksanimationlong)

class Lost_Adventurer(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

     

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = ADVENTURER_SPEED
        self.health = round(ADVENTURER_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(ADVENTURER_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()

        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.animation_loopshort = 1
        self.animation_looplong = 1
        self.animation_loopidle = 1

        self.movement_loop = 0
        self.max_travel = 15

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 200  # Portée de détection du joueur en pixels
        self.is_attackingshort = False
        self.is_attackinglong = False

        self.right_animations = [self.game.adventurerwalk_spritesheet.get_sprite(0, 64, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(32, 64, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(64, 64, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(96, 64, 32, 32),]

        self.left_animations = [self.game.adventurerwalk_spritesheet.get_sprite(0, 96, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(32, 96, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(64, 96, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(96, 96, 32, 32),]

        self.down_animations = [self.game.adventurerwalk_spritesheet.get_sprite(0, 0, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(32, 0, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(64, 0, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(96, 0, 32, 32),]

        self.up_animations = [self.game.adventurerwalk_spritesheet.get_sprite(0 ,32, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(32, 32, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(64, 32, 32, 32),
                           self.game.adventurerwalk_spritesheet.get_sprite(96, 32, 32, 32),]
        
        
        self.right_idleanimations = [self.game.adventureridle_spritesheet.get_sprite(0, 64, 32, 32),
                                    self.game.adventureridle_spritesheet.get_sprite(32, 64, 32, 32),]

        self.left_idleanimations = [self.game.adventureridle_spritesheet.get_sprite(0, 96, 32,32),
                                    self.game.adventureridle_spritesheet.get_sprite(32, 96, 32,32),]

        self.down_idleanimations = [self.game.adventureridle_spritesheet.get_sprite(0, 0, 32,32),
                                    self.game.adventureridle_spritesheet.get_sprite(32, 0, 32,32),]

        self.up_idleanimations = [self.game.adventureridle_spritesheet.get_sprite(0, 32, 32,32),
                                    self.game.adventureridle_spritesheet.get_sprite(32, 32, 32,32),]
        

        
        self.up_attacksanimation = [self.game.shortadventurerattack_spritesheet.get_sprite(0, 131, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(32, 131, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(64, 131, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(96, 131, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(128, 131, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(160, 131, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(192, 131, 32, 67),]


        self.right_attacksanimation = [self.game.shortadventurerattack_spritesheet.get_sprite(0, 0, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(67, 0, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(134, 0, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(201, 0, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(268, 0, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(335, 0, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(402, 0, 67, 32),]

        self.down_attacksanimation = [self.game.shortadventurerattack_spritesheet.get_sprite(0, 32, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(32, 32, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(64, 32, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(96, 32, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(128, 32, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(160, 32, 32, 67),
self.game.shortadventurerattack_spritesheet.get_sprite(192, 32, 32, 67),]

        self.left_attacksanimation = [self.game.shortadventurerattack_spritesheet.get_sprite(0, 99, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(67, 99, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(134, 99, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(201, 99, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(268, 99, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(335, 99, 67, 32),
self.game.shortadventurerattack_spritesheet.get_sprite(402, 99, 67, 32),]
        
        self.right_attacksanimationpos = [self.game.adventurershortattackpos_spritesheet.get_sprite(0, 64, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(32, 64, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(64, 64, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(96, 64, 32, 32),]

        self.left_attacksanimationpos = [self.game.adventurershortattackpos_spritesheet.get_sprite(0, 96, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(32, 96, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(64, 96, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(96, 96, 32, 32),]

        self.down_attacksanimationpos = [self.game.adventurershortattackpos_spritesheet.get_sprite(0, 0, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(32, 0, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(64, 0, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(96, 0, 32, 32),]

        self.up_attacksanimationpos = [self.game.adventurershortattackpos_spritesheet.get_sprite(0 ,32, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(32, 32, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(64, 32, 32, 32),
                           self.game.adventurershortattackpos_spritesheet.get_sprite(96, 32, 32, 32),]
        


        self.left_attacksanimationslong = [self.game.beetleattacks_spritesheet.get_sprite(0, 0, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200, 0, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*2, 0, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*3, 0, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*4, 0, 200, 32),]

        self.up_attacksanimationslong = [self.game.beetleattacks_spritesheet.get_sprite(0, 32, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(32, 32, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(64, 32, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(96, 32, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(128, 32, 32, 200),]

        self.right_attacksanimationslong = [self.game.beetleattacks_spritesheet.get_sprite(0, 232, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200, 232, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*2, 232, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*3, 232, 200, 32),
                                    self.game.beetleattacks_spritesheet.get_sprite(200*4, 232, 200, 32),]


        self.down_attacksanimationslong = [self.game.beetleattacks_spritesheet.get_sprite(0, 264, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(32, 264, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(64, 264, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(96, 264, 32, 200),
                                    self.game.beetleattacks_spritesheet.get_sprite(128, 264, 32, 200),]

        self.right_attacksanimationlongpos = [self.game.adventurerlongattackpos_spritesheet.get_sprite(0, 64, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(32, 64, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(64, 64, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(96, 64, 32, 32),]

        self.left_attacksanimationlongpos = [self.game.adventurerlongattackpos_spritesheet.get_sprite(0, 96, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(32, 96, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(64, 96, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(96, 96, 32, 32),]

        self.down_attacksanimationlongpos = [self.game.adventurerlongattackpos_spritesheet.get_sprite(0, 0, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(32, 0, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(64, 0, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(96, 0, 32, 32),]

        self.up_attacksanimationlongpos = [self.game.adventurerlongattackpos_spritesheet.get_sprite(0 ,32, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(32, 32, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(64, 32, 32, 32),
                           self.game.adventurerlongattackpos_spritesheet.get_sprite(96, 32, 32, 32),]

    def update(self):
        self.collide_attack()
        if self.player:
            distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery))
            if distance_to_player <= self.detect_range:
                if distance_to_player <= self.detect_range-175:
                    self.is_attackinglong = False
                    self.is_attackingshort = True
                    self.animateattackshort()
                elif distance_to_player <= self.detect_range-50:
                    self.follow_player()
                    self.is_attackingshort = False
                    self.is_attackinglong = True
                    self.animateattacklong()
            else:
                self.is_attackingshort = False
                self.is_attackinglong = False
                self.animateidle()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.attackshort()
        self.attacklong()

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

                    

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 2:
                self.animation_loopidle = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 2:
                self.animation_loopidle = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 2:
                self.animation_loopidle = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 2:
                self.animation_loopidle = 0

    def animateattackshort(self):
        if self.facing == "down":
            self.image = self.down_attacksanimationpos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 4:
                self.animation_loopshort = 0
            
        if self.facing == "left":
            self.image = self.left_attacksanimationpos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 4:
                self.animation_loopshort = 0
                    
        if self.facing == "right":
            self.image = self.right_attacksanimationpos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 4:
                self.animation_loopshort = 0

        if self.facing == "up":
            self.image = self.up_attacksanimationpos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 4:
                self.animation_loopshort = 0


    def animateattacklong(self):
        if self.facing == "down":
            self.image = self.down_attacksanimationlongpos[math.floor(self.animation_looplong)]
            self.animation_looplong += 0.1
            if self.animation_looplong >= 4:
                self.animation_looplong = 0
            
        if self.facing == "left":
            self.image = self.left_attacksanimationlongpos[math.floor(self.animation_looplong)]
            self.animation_looplong += 0.1
            if self.animation_looplong >= 4:
                self.animation_looplong = 0
                    
        if self.facing == "right":
            self.image = self.right_attacksanimationlongpos[math.floor(self.animation_looplong)]
            self.animation_looplong += 0.1
            if self.animation_looplong >= 4:
                self.animation_looplong = 0

        if self.facing == "up":
            self.image = self.up_attacksanimationlongpos[math.floor(self.animation_looplong)]
            self.animation_looplong += 0.1
            if self.animation_looplong >= 4:
                self.animation_looplong = 0

    def away_from_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'down'

    def follow_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 200
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 500
    
    def attackshort(self):
        if self.is_attackingshort == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 2 +self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x - 10
                        yatt = self.rect.y - 60
                    if self.facing == 'down':
                        xatt = self.rect.x + 10
                        yatt = self.rect.y + 40
                    if self.facing == 'left':
                        xatt = self.rect.x - 60
                        yatt = self.rect.y + 15
                    if self.facing == 'right':
                        xatt = self.rect.x + 20
                        yatt = self.rect.y
                    AttackEnemy(self.game,xatt,yatt,70,32,7,self.facing,self.right_attacksanimation,self.left_attacksanimation,self.up_attacksanimation,self.down_attacksanimation)


    def attacklong(self):
        if self.is_attackinglong == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 2 +self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x
                        yatt = self.rect.y - 200
                    if self.facing == 'down':
                        xatt = self.rect.x 
                        yatt = self.rect.y + 30
                    if self.facing == 'left':
                        xatt = self.rect.x - 200
                        yatt = self.rect.y
                    if self.facing == 'right':
                        xatt = self.rect.x + 30
                        yatt = self.rect.y
                    AttackEnemy(self.game,xatt,yatt,200,35,5,self.facing,self.right_attacksanimationslong,self.left_attacksanimationslong,self.up_attacksanimationslong,self.down_attacksanimationslong)

class Zombie(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

     

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = ZOMBIE_SPEED
        self.health = round(ZOMBIE_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(ZOMBIE_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()

        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.animation_loopshort = 1
        self.animation_looplong = 1
        self.animation_loopidle = 1

        self.movement_loop = 0
        self.max_travel = 15

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 200  # Portée de détection du joueur en pixels
        self.is_attackingshort = False
        self.is_attackinglong = False

        self.right_animations = [self.game.zombiewalk_spritesheet.get_sprite(0, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(32, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(64, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(96, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(128, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(160, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(192, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(224, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(256, 64, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(288, 64, 32, 32),]

        self.left_animations = [self.game.zombiewalk_spritesheet.get_sprite(0, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(32, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(64, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(96, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(128, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(160, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(192, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(224, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(256, 96, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(288, 96, 32, 32),]

        self.down_animations = [self.game.zombiewalk_spritesheet.get_sprite(0, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(32, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(64, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(96, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(128, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(160, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(192, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(224, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(256, 0, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(288, 0, 32, 32),]

        self.up_animations = [self.game.zombiewalk_spritesheet.get_sprite(0, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(32, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(64, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(96, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(128, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(160, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(192, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(224, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(256, 32, 32, 32),
                           self.game.zombiewalk_spritesheet.get_sprite(288, 32, 32, 32),]
        
        
        self.right_idleanimations = [self.game.zombieidle_spritesheet.get_sprite(0, 64, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(32, 64, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(64, 64, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(96, 64, 32, 32),]

        self.left_idleanimations = [self.game.zombieidle_spritesheet.get_sprite(0, 96, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(32, 96, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(64, 96, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(96, 96, 32, 32),]

        self.down_idleanimations = [self.game.zombieidle_spritesheet.get_sprite(0, 0, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(32, 0, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(64, 0, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(96, 0, 32, 32),]

        self.up_idleanimations = [self.game.zombieidle_spritesheet.get_sprite(0 ,32, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(32, 32, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(64, 32, 32, 32),
                           self.game.zombieidle_spritesheet.get_sprite(96, 32, 32, 32),]
        

        
        self.down_attacksanimation = [self.game.zombieattack_spritesheet.get_sprite(0, 0, 57, 32),
        self.game.zombieattack_spritesheet.get_sprite(57, 0, 57, 32),
        self.game.zombieattack_spritesheet.get_sprite(114, 0, 57, 32),
        self.game.zombieattack_spritesheet.get_sprite(171, 0, 57, 32),
        self.game.zombieattack_spritesheet.get_sprite(228, 0, 57, 32),]

        self.left_attacksanimation = [self.game.zombieattack_spritesheet.get_sprite(0, 32, 32, 57),
        self.game.zombieattack_spritesheet.get_sprite(32, 32, 32, 57),
        self.game.zombieattack_spritesheet.get_sprite(64, 32, 32, 57),
        self.game.zombieattack_spritesheet.get_sprite(96, 32, 32, 57),
        self.game.zombieattack_spritesheet.get_sprite(128, 32, 32, 57),]

        self.up_attacksanimation = [self.game.zombieattack_spritesheet.get_sprite(0, 89, 57, 32),
        self.game.zombieattack_spritesheet.get_sprite(57, 89, 57, 32),
        self.game.zombieattack_spritesheet.get_sprite(114, 89, 57, 32),
        self.game.zombieattack_spritesheet.get_sprite(171, 89, 57, 32),
        self.game.zombieattack_spritesheet.get_sprite(228, 89, 57, 32),]

        self.right_attacksanimation = [self.game.zombieattack_spritesheet.get_sprite(0, 121, 32, 57),
        self.game.zombieattack_spritesheet.get_sprite(32, 121, 32, 57),
        self.game.zombieattack_spritesheet.get_sprite(64, 121, 32, 57),
        self.game.zombieattack_spritesheet.get_sprite(96, 121, 32, 57),
        self.game.zombieattack_spritesheet.get_sprite(128, 121, 32, 57),]


        
        self.right_attackanimationspos = [self.game.zombieattackpos_spritesheet.get_sprite(0, 64, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(32, 64, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(64, 64, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(96, 64, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(128, 64, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(160, 64, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(192, 64, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(224, 64, 32, 32),]

        self.left_attackanimationspos = [self.game.zombieattackpos_spritesheet.get_sprite(0, 96, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(32, 96, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(64, 96, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(96, 96, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(128, 96, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(160, 96, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(192, 96, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(224, 96, 32, 32),]

        self.down_attackanimationspos = [self.game.zombieattackpos_spritesheet.get_sprite(0, 0, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(32, 0, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(64, 0, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(96, 0, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(128, 0, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(160, 0, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(192, 0, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(224, 0, 32, 32),]

        self.up_attacksanimationspos = [self.game.zombieattackpos_spritesheet.get_sprite(0, 32, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(32, 32, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(64, 32, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(96, 32, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(128, 32, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(160, 32, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(192, 32, 32, 32),
                           self.game.zombieattackpos_spritesheet.get_sprite(224, 32, 32, 32),]
        

    def update(self):
        self.collide_attack()
        if self.player:
            distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery))
            if distance_to_player <= self.detect_range:
                if distance_to_player <= self.detect_range-175:
                    self.is_attackingshort = True
                    self.animateattackshort()
                else:
                    self.animate()
                    self.follow_player()
            else:
                self.is_attackingshort = False
                self.animateidle()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.attackshort()

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

                    

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 10:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 10:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 10:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 10:
                self.animation_loop = 0

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 4:
                self.animation_loopidle = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 4:
                self.animation_loopidle = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 4:
                self.animation_loopidle = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 4:
                self.animation_loopidle = 0

    def animateattackshort(self):
        if self.facing == "down":
            self.image = self.down_attackanimationspos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 8:
                self.animation_loopshort = 0
            
        if self.facing == "left":
            self.image = self.left_attackanimationspos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 8:
                self.animation_loopshort = 0
                    
        if self.facing == "right":
            self.image = self.right_attackanimationspos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 8:
                self.animation_loopshort = 0

        if self.facing == "up":
            self.image = self.up_attacksanimationspos[math.floor(self.animation_loopshort)]
            self.animation_loopshort += 0.1
            if self.animation_loopshort >= 8:
                self.animation_loopshort = 0


    def away_from_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'down'

    def follow_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 200
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 500
    
    def attackshort(self):
        if self.is_attackingshort == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 2 +self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x
                        yatt = self.rect.y - 20
                    if self.facing == 'down':
                        xatt = self.rect.x
                        yatt = self.rect.y + 20
                    if self.facing == 'left':
                        xatt = self.rect.x - 20
                        yatt = self.rect.y 
                    if self.facing == 'right':
                        xatt = self.rect.x + 20
                        yatt = self.rect.y
                    AttackEnemy(self.game,xatt,yatt,60,60,5,self.facing,self.right_attacksanimation,self.left_attacksanimation,self.up_attacksanimation,self.down_attacksanimation)




class Gardener(pygame.sprite.Sprite):
    def __init__(self,game,x,y,tilemap):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.__coortilemap = (y,x)

        self.etage = tilemap

     

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.vitesse = GARDENER_SPEED
        self.health = round(GARDENER_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.maxhealth = round(GARDENER_HEALTH*self.game.multiplicateur_difficulte_hp_enemies)
        self.healthbar = HealthBar(game,self.x+20,(self.y-30),self.health,self.maxhealth,False)

        self.derniertemps = pygame.time.get_ticks()
        self.derniertemps1 = pygame.time.get_ticks()
        self.derniertemps2 = pygame.time.get_ticks()

        self.x_change = 0
        self.y_change = 0
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.facing = random.choice(['left','right','up','down'])
        self.animation_loop = 1
        self.animation_loopshort = 1
        self.animation_looplong = 1
        self.animation_loopidle = 1

        self.movement_loop = 0
        self.max_travel = 15

        self.player = self.game.player  # Référence au joueur
        self.detect_range = 500  # Portée de détection du joueur en pixels
        self.is_attackingshort = False
        self.is_attackinglong = False

        self.down_animations = [self.game.gardenerwalk_spritesheet.get_sprite(0, 0, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(40, 0, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(80, 0, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(120, 0, 40, 36),]

        self.left_animations = [self.game.gardenerwalk_spritesheet.get_sprite(0, 36, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(40, 36, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(80, 36, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(120, 36, 40, 36),]

        self.right_animations = [self.game.gardenerwalk_spritesheet.get_sprite(0, 72, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(40, 72, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(80, 72, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(120, 72, 40, 36),]

        self.up_animations = [self.game.gardenerwalk_spritesheet.get_sprite(0 ,108, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(40, 108, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(80, 108, 40, 36),
                           self.game.gardenerwalk_spritesheet.get_sprite(120, 108, 40, 36),]
        
        
        self.down_idleanimations = [self.game.gardeneridle_spritesheet.get_sprite(0, 0, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(40, 0, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(80, 0, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(120, 0, 40, 36),]

        self.left_idleanimations = [self.game.gardeneridle_spritesheet.get_sprite(0, 36, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(40, 36, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(80, 36, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(120, 36, 40, 36),]

        self.right_idleanimations = [self.game.gardeneridle_spritesheet.get_sprite(0, 72, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(40, 72, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(80, 72, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(120, 72, 40, 36),]

        self.up_idleanimations = [self.game.gardeneridle_spritesheet.get_sprite(0 ,108, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(40, 108, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(80, 108, 40, 36),
                           self.game.gardeneridle_spritesheet.get_sprite(120, 108, 40, 36),]
        
        self.boom = [self.game.boom_spritesheet.get_sprite(0, 0, 256, 256),
                     self.game.boom_spritesheet.get_sprite(0, 0, 256, 256),
                     self.game.boom_spritesheet.get_sprite(0, 0, 256, 256),
                     self.game.boom_spritesheet.get_sprite(0, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*2, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*2, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*2, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*2, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*3, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*3, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*3, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*3, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*3, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*3, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*4, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*4, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*4, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*4, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*5, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*5, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*5, 0, 256, 256),
                                        self.game.boom_spritesheet.get_sprite(256*5, 0, 256, 256),]
        
        self.up_attacksanimation = self.boom
        self.right_attacksanimation = self.boom
        self.down_attacksanimation = self.boom
        self.left_attacksanimation = self.boom
        

    def update(self):
        self.collide_attack()
        if self.player:
            distance_to_player = math.dist((self.rect.centerx, self.rect.centery), (self.player.rect.centerx, self.player.rect.centery))
            if distance_to_player <= self.detect_range:
                self.follow_player()
                self.animate()
                if distance_to_player <= self.detect_range-475:
                    self.is_attackingshort = True
                    self.modify_tilemap()
                    self.kill()

            else:
                self.is_attackingshort = False
                self.animateidle()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.attackshort()

        self.x_change = 0
        self.y_change = 0 
        
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        hitslave = pygame.sprite.spritecollide(self, self.game.lave, False)
        hits1 = pygame.sprite.spritecollide(self, self.game.coffre1,False)
        hits2 = pygame.sprite.spritecollide(self, self.game.coffre2, False)
        hits3 = pygame.sprite.spritecollide(self, self.game.coffre3, False)
        hits4 = pygame.sprite.spritecollide(self, self.game.coffre4, False)
        hits5 = pygame.sprite.spritecollide(self, self.game.coffre5, False)
        hits6 = pygame.sprite.spritecollide(self, self.game.coffre6, False)
        hits7 = pygame.sprite.spritecollide(self, self.game.coffre7, False)
        hits8 = pygame.sprite.spritecollide(self, self.game.coffre8, False)
        hits9 = pygame.sprite.spritecollide(self, self.game.coffre9, False)
        if hits or hits1 or hits2 or hits3 or hits4 or hits5 or hits6 or hits7 or hits8 or hits9 or hitslave:
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
            elif hitslave:
                hit = hitslave
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.x = hit[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hit[0].rect.right

            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hit[0].rect.top - self.rect.width
                    if self.y_change < 0:
                        self.rect.y = hit[0].rect.bottom

                    

    def animate(self):
        if self.facing == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
            
        if self.facing == "left":
            self.image = self.left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0
                    
        if self.facing == "right":
            self.image = self.right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

        if self.facing == "up":
            self.image = self.up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 4:
                self.animation_loop = 0

    def animateidle(self):
        if self.facing == "down":
            self.image = self.down_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 4:
                self.animation_loopidle = 0
            
        if self.facing == "left":
            self.image = self.left_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 4:
                self.animation_loopidle = 0
                    
        if self.facing == "right":
            self.image = self.right_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 4:
                self.animation_loopidle = 0

        if self.facing == "up":
            self.image = self.up_idleanimations[math.floor(self.animation_loopidle)]
            self.animation_loopidle += 0.1
            if self.animation_loopidle >= 4:
                self.animation_loopidle = 0

    def away_from_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'down'

    def follow_player(self):
        # Déplace le chevalier vers le joueur
        if self.player.rect.centerx < self.rect.centerx:
            self.x_change = -self.vitesse
            self.facing = 'left'
        elif self.player.rect.centerx > self.rect.centerx:
            self.x_change = self.vitesse
            self.facing = 'right'

        if self.player.rect.centery < self.rect.centery:
            self.y_change = -self.vitesse
            self.facing = 'up'
        elif self.player.rect.centery > self.rect.centery:
            self.y_change = self.vitesse
            self.facing = 'down'

    def collide_attack(self):
        hits = pygame.sprite.spritecollide(self, self.game.attacks, False)
        if hits:
            if self.invincibility() == False:
                self.healthbar.take_damage(self.game.player.puissance)
                self.derniertemps = pygame.time.get_ticks()
            if self.healthbar.health <= 0:
                self.game.totalenemykill += 1
                self.modify_tilemap()
                self.kill()

    def modify_tilemap(self):
        if self.etage == "tilemap1":
            self.game.all_maps.tilemap1[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap2":
            self.game.all_maps.tilemap2[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap3":
            self.game.all_maps.tilemap3[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap4":
            self.game.all_maps.tilemap4[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap5":
            self.game.all_maps.tilemap5[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'
        elif self.etage == "tilemap6":
            self.game.all_maps.tilemap6[1][self.__coortilemap[0]][self.__coortilemap[1]] = '.'

    def invincibility(self):
        return self.derniertemps > pygame.time.get_ticks() - 750
    
    def attacktime(self):
        return self.derniertemps1 > pygame.time.get_ticks() - 200
    
    def clicktime(self):
        return self.derniertemps2 > pygame.time.get_ticks() - 500
    
    def attackshort(self):
        if self.is_attackingshort == True:
            if self.clicktime() == False:
                if self.attacktime() == False:
                    self.derniertemps2 = pygame.time.get_ticks()
                    self.derniertemps1 = pygame.time.get_ticks()
                    self.game.player.enemyattacks = 9 +self.game.multiplicateur_difficulte_attack_enemies 
                    if self.facing == 'up':
                        xatt = self.rect.x - 128
                        yatt = self.rect.y - 80
                    if self.facing == 'down':
                        xatt = self.rect.x - 128
                        yatt = self.rect.y - 160
                    if self.facing == 'left':
                        xatt = self.rect.x - 160
                        yatt = self.rect.y - 128
                    if self.facing == 'right':
                        xatt = self.rect.x - 80
                        yatt = self.rect.y - 128
                    AttackEnemy(self.game,xatt,yatt,256,256,25,self.facing,self.right_attacksanimation,self.left_attacksanimation,self.up_attacksanimation,self.down_attacksanimation)