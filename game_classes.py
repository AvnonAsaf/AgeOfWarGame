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
        self._troops: list[Troop] = []
    
    def add_troop(self, troop_type):
        troop = Troop(troop_type, self.screen)
        self._troops.append(troop)
    
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
        enemy = Troop("enemy", self.screen)
        for troop in self._troops:
            
            troop.check_bump(self._troops, enemy)
            troop.troop_move()
            enemy.draw()
            troop.draw()
            


class Troop:
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
        if troop_type == "enemy":
            self.size = 80
            self._init_enemy()
    
    def _init_attacker(self):
        if self.troopsr_evolution == 0:
            self.health = 120
            self.damage = 70
            self.vel = 2
        self.x += self.size

    def _init_archer(self):
        if self.troopsr_evolution == 0:
            self.health = 80
            self.damage = 50
            self.vel = 3
        self.x += self.size
    def _init_tank(self):
        if self.troopsr_evolution == 0:
            self.health = 200
            self.damage = 100
            self.vel = 1
        self.x += self.size
    def _init_enemy(self):
        if self.troopsr_evolution == 0:
            self.health = 200
            self.damage = 100
            self.vel = 1
        self.x = 1500
   
    def troop_move(self):
        if self.bumped:
            return
        self.x += self.vel
    
    def attack(self, enemy):
        enemy.health -= self.damage

        
                
    def draw(self):
        size = self.size
        font = pygame.font.Font(None, 30)
        text = font.render(f"{self.health}", 1, (255, 255, 255))
        self.screen.blit(text, (self.x, self.y - self.size - 30))
        if self.troop_type == "attacker":
            pygame.draw.rect(self.screen, (00,00,255), (self.x, self.y - size, size, size))
        elif self.troop_type == "archer": 
            pygame.draw.rect(self.screen, (00,142,150), (self.x, self.y - size, size, size))
        elif self.troop_type == "tank":
            pygame.draw.rect(self.screen, (150,00,255), (self.x, self.y - size, size, size))
        elif self.troop_type == "enemy":
            pygame.draw.rect(self.screen, (245,120,40), (self.x, self.y - size, size, size))
    
    def check_bump(self, troops, enemy_troop):
        if len(troops) > 1:
            for index in range(1, len(troops)):
                if troops[index].x == self.x:
                    if self.x >= troops[index - 1].x - self.size - 100:
                        self.bumped = True
                        break
                    else:
                        self.bumped = False
        if troops[0].x >= enemy_troop.x - enemy_troop.size - 50:
            troops[0].bumped = True
            troops[0].attack(enemy_troop)
        else:
            troops[0].bumped = False
   



