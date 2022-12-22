import pygame
import time
import itertools
class Troop:
    def __init__(self, type, screen):
        self.troopsr_evolution = 0
        self.screen = screen
        self.x = 350
        self.y = screen.get_height()
        self.type = type
        self.bumped = False
        if type == "attacker":
            self.size = 50
            self.health = 120
            self.damage = 70
            self.vel = 2
        elif type == "archer":
            self.size = 30
            self.health = 80
            self.damage = 50
            self.vel = 3
        elif type == "tank":
            self.size = 100
            self.health = 200
            self.damage = 100
            self.vel = 1
        
        self.x += self.size

    def update(self):
        self.x += self.vel; 
    
    def attack(self, enemy):
        enemy.health -= self.damage
        
        
class Tower:
    def __init__(self, side, size,screen, tank_img = None, attacker_img = None, archer_img = None):
        self.tower_evolution = 0
        self.side = side
        self.size = size
        self.screen = screen
        self.color = (255, 00, 00)
        self.max_health = 1000
        self.damage = 0
        self._troops: list[Troop] = []
        self.troop_font = pygame.font.Font(None, 30)
        self.tower_font = pygame.font.Font(None, 36)
        self.tank_img = tank_img
        self.attacker_img = attacker_img
        self.archer_img = archer_img
        
    
    def add_troop(self, troop_type):
        troop = Troop(troop_type, self.screen)
        self._troops.append(troop)
        
        
    # TODO: change the drowing to use the image
    def _draw_troop(self, troop: Troop):
        
        
        size = troop.size
        text = self.troop_font.render(f"{troop.health}", 1, (255, 255, 255))
        
        if self.side == 'left':
            self.screen.blit(text, (troop.x, self.screen.get_height() - troop.size - 30))

            if troop.type == "attacker":
                pygame.draw.rect(self.screen, (00,00,255), (troop.x, self.screen.get_height() - size, size, size))
            elif troop.type == "archer": 
                pygame.draw.rect(self.screen, (00,142,150), (troop.x, self.screen.get_height() - size, size, size))
            elif troop.type == "tank":
                pygame.draw.rect(self.screen, (150,00,255), (troop.x, self.screen.get_height() - size, size, size))
                
        else:
            
            self.screen.blit(text, (self.screen.get_width() - troop.x, self.screen.get_height() - troop.size - 30))
            
            if troop.type == "attacker":
                pygame.draw.rect(self.screen, (00,00,255), (self.screen.get_width() - troop.x, self.screen.get_height() - size, size, size))
            elif troop.type == "archer": 
                pygame.draw.rect(self.screen, (00,142,150), (self.screen.get_width() - troop.x, self.screen.get_height() - size, size, size))
            elif troop.type == "tank":
                pygame.draw.rect(self.screen, (150,00,255), (self.screen.get_width() - troop.x, self.screen.get_height() - size, size, size))

    
    def draw(self):  
        if self.side == "left":
            text = self.tower_font.render(f"Health : {self.max_health - self.damage}", 1, (255, 255, 255))
            self.screen.blit(text, (0, self.screen.get_height() - self.size - 30))
            pygame.draw.rect(self.screen, self.color, (0, self.screen.get_height() - self.size,self.size, self.size))
            
        else:
            text = self.tower_font.render(f"Health : {self.max_health - self.damage}", 1, (255, 255, 255))
            self.screen.blit(text, (self.screen.get_width() - self.size, self.screen.get_height() - self.size - 30))
            pygame.draw.rect(self.screen, self.color, (self.screen.get_width() - self.size, self.screen.get_height() - self.size,self.size, self.size))
        
        for troop in self._troops:
            self._draw_troop(troop)
            
            
    def update(tower1, tower2):
        if tower1._troops:
            troop1 = tower1._troops[0]
            if tower2._troops:
                troop2 = tower2._troops[0]
                
                if tower1.screen.get_width() -  (troop1.x + troop2.x + troop1.size / 2 + troop2.size / 2 + troop1.vel + troop2.vel) > 0:
                    troop1.update()
                    troop2.update()
                else:
                    # TODO: damege
                    pass
            else:
                tower1.update()
        elif tower2._troops:
            tower2._troops[0].update()
            
        
        for troop_1, troop_2 in itertools.pairwise(tower1._troops):
            # if not bumped
            if troop_2.x < troop_1.x - troop_1.size / 2 - troop_2.size / 2 - troop2.vel - 30:
                troop_2.update()
                
        for troop_1, troop_2 in itertools.pairwise(tower2._troops):
            # if not bumped
            if troop_2.x < troop_1.x - troop_1.size / 2 - troop_2.size / 2 - troop2.vel - 30 :
                troop_2.update()
