import pygame
import time

class Tower:
    def __init__(self, side, size,screen):
        self.tower_evolution = 0
        self.side = side
        self.size = size
        self.screen = screen
        self.color = (255, 00, 00)
        self.max_health = 1000
        self.damage = 0
        
    def draw_tower_ev_hp(self):  
        if self.side == "left":
          font = pygame.font.Font(None, 36)
          text = font.render(f"Health : {self.max_health - self.damage}", 1, (255, 255, 255))
          self.screen.blit(text, (0, self.screen.get_height() - self.size - 30))
          pygame.draw.rect(self.screen, self.color, (0, self.screen.get_height() - self.size,self.size, self.size))
        else:
          font = pygame.font.Font(None, 36)
          text = font.render(f"Health : {self.max_health - self.damage}", 1, (255, 255, 255))
          self.screen.blit(text, (self.screen.get_width() - self.size, self.screen.get_height() - self.size - 30))
          pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - self.size, self.screen.get_height() - self.size,self.size, self.size))


    
class Troops:
    def __init__(self, troop_type, screen):
        self.troopsr_evolution = 0
        self.screen = screen
        self.x = 350
        self.y = screen.get_height()
        self.troop_type = troop_type
        self.bumped = False
        if troop_type == "attacker":
            self.size = 50
            self._init_attacker()
        if troop_type == "archer":
            self.size = 30
            self._init_archer()
        if troop_type == "tank":
            self.size = 100
            self._init_tank()
        if troop_type == "none":
            self.size = 100
            self._init_none()
    
    def _init_attacker(self):
        if self.troopsr_evolution == 0:
            self.health = 120
            self.damage = 70
        size = 50
        
        self.x += size
        
        
    def _init_archer(self):
        if self.troopsr_evolution == 0:
            self.health = 80
            self.damage = 50
        size = 30
        self.x += size
    def _init_tank(self):
        if self.troopsr_evolution == 0:
            self.health = 200
            self.damage = 100
        size = 100
        self.x += size
    def _init_none(self):
        if self.troopsr_evolution == 0:
            self.health = 200
            self.damage = 100
        size = 100
        self.x += size
    def troop_move(self):
        if not self.bumped:
            if self.troop_type == "attacker":
                size = 50
                pygame.draw.rect(self.screen, (00,00,00), (self.x, self.y - size, size, size))
                self.x += 50
                pygame.draw.rect(self.screen, (00,00,255), (self.x, self.y - size, size, size))
                time.sleep(0.4)
            elif self.troop_type == "archer":
                size = 30
                pygame.draw.rect(self.screen, (00,00,00), (self.x, self.y - size, size, size))
                self.x += 50
                pygame.draw.rect(self.screen, (00,142,150), (self.x, self.y - size, size, size))
                time.sleep(0.2)
            elif self.troop_type == "tank":
                size = 100
                pygame.draw.rect(self.screen, (00,00,00), (self.x, self.y - size, size, size))
                self.x += 50
                pygame.draw.rect(self.screen, (150,00,255), (self.x, self.y - size, size, size))
                time.sleep(0.5)
            elif self.troop_type == "none":
                size = 100
                pygame.draw.rect(self.screen, (00,00,00), (self.x, self.y - size, size, size))
                self.x = 1400
                pygame.draw.rect(self.screen, (150,00,255), (self.x, self.y - size, size, size))
    def bump(self, other_troop):
        """Check if the troop has bumped into another troop."""
        # check if the x-coordinates of the two troops overlap
        # if self.x + self.size >= other_troop.x - self.size - 20:
        #     self.bumped = True  # set the bumped flag to True
        #     return True
        # else:
        #     self.bumped = False
        #     return False
        if self.x < other_troop.x + other_troop.size + 100 and self.x + self.size + 100 > other_troop.x:
            self.x = other_troop.x - self.size  # Stop the current troop
            return True
        self.bumped = False
        return False
        
        
        

