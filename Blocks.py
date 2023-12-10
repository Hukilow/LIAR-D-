from typing import Any
from config import *
from Item import *
import math

class Block(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        #self.image = self.game.terrain_spritesheet.get_sprite(145, 384, self.width, self.height)
        self.image = self.game.mur_spritesheet.get_sprite(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



class Ground(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        #self.image = self.game.terrain_spritesheet.get_sprite(349,160, self.width, self.height)
        self.image = self.game.sol_spritesheet.get_sprite(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 

class EchelleHaut(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.echellehaut
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.terrain_spritesheet.get_sprite(931, 326, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class EchelleBas(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.echellebas
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.terrain_spritesheet.get_sprite(931, 326, 32, 16)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Trap(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.trap
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.trap_spritesheet.get_sprite(0,0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.trap = False
        self.animation_loop = 0

        self.trapsprite = [self.game.trap_spritesheet.get_sprite(0,0 , 32,32),
                           self.game.trap_spritesheet.get_sprite(48,0, 32,32),
                           self.game.trap_spritesheet.get_sprite(96, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(144, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(192, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(240, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(288, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(336,0, 32,32),
                           self.game.trap_spritesheet.get_sprite(384, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(432, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(480, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(528, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(576, 0, 32,32),
                           self.game.trap_spritesheet.get_sprite(624, 0, 32,32),]

    def update(self):
        self.animate()
        
    def animate(self):
            hits = pygame.sprite.spritecollide(self, self.game.playerhitbox, False)
            if hits:
                self.trap = True
            if self.trap == True:
                self.image = self.trapsprite[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                print(self.animation_loop)
                if self.animation_loop >= 14:
                    self.trap = False
                    self.animation_loop = 0

                

class Escalier(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.escalier
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(288,640, 64, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Escaliercasse(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.escaliercasse
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(288,576, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre1(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre1
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(0, 0, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre2(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre2
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(33, 66, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre3(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre3
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(32, 0, 30, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre4(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre4
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(64, 65, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre5(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre5
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(32, 32, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre6(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre6
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(0, 66, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre7(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre7
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(64, 0, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre8(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre8
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(64, 32, 32, 31)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffre9(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.coffre9
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.allchests_spritesheet.get_sprite(0, 32, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Coffrecasse(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.coffrecasse
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.pos = (x,y)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        
        self.image = self.game.terrain_spritesheet.get_sprite(329, 515, 32, 32)

        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        print("init")
        print(self.pos)
        self.game.screen.blit(self.image,self.pos)

    def update(self):
        self.game.screen.blit(self.image,self.pos)

class Lave(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(480, 0, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave1(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(480, 64, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave2(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(512, 64, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave3(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(544, 64, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave4(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(480, 96, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave5(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(512, 96, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave6(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(544, 96, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave7(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(480, 128, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave8(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(512, 128, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Lave9(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.lave
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(544, 128, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cailloux1(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.caillouxgroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960, 480, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cailloux2(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.caillouxgroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(928, 512, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cailloux3(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.caillouxgroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960, 512, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cailloux4(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.caillouxgroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(992, 512, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cailloux5(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.caillouxgroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(928, 576, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cailloux6(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.caillouxgroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(928, 608, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cailloux7(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.caillouxgroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960, 608, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cailloux8(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game= game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.caillouxgroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(992, 576, 32, 32)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
