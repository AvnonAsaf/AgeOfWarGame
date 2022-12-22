import pygame
import time
import random
from game_classes import *
import threading

images = {}

def seliction(screen, size):
    y_square = screen.get_height() - size - 100
    x_squere1 = 0
    x_squere2 = 100
    x_squere3 = 200
    squere_size = 50
    font = pygame.font.Font(None, 30)
    text1 = font.render("DMG", 1, (255, 255, 255))
    screen.blit(text1, (0, y_square - 50))
    pygame.draw.rect(screen, (00,00,255), (x_squere1, y_square,squere_size, squere_size))
    text2 = font.render("ARC", 1, (255, 255, 255))
    screen.blit(text2, (100, y_square - 50))
    pygame.draw.rect(screen, (00,142,150), (x_squere2, y_square,squere_size, squere_size))
    text2 = font.render("TNK", 1, (255, 255, 255))
    screen.blit(text2, (200, y_square - 50))
    # pygame.draw.rect(screen, (150,00,255), (x_squere3, y_square,squere_size, squere_size))
    screen.blit(images["tankselect"], (x_squere3, y_square))  
    



def select(screen, size, mouse_pos):
    y_square = screen.get_height() - size - 100
    x_squere1 = 0
    x_squere2 = 100
    x_squere3 = 200
    squere_size = 50
    mouse_x, mouse_y = mouse_pos
    if (mouse_x >= x_squere1 and mouse_x <= x_squere1 + squere_size and mouse_y >= y_square and mouse_y <= y_square + squere_size):
            return "attacker"
    elif (mouse_x >= x_squere2 and mouse_x <= x_squere2 + squere_size and mouse_y >= y_square and mouse_y <= y_square + squere_size):
            return "archer"
    elif (mouse_x >= x_squere3 and mouse_x <= x_squere3 + squere_size and mouse_y >= y_square and mouse_y <= y_square + squere_size):
            return "tank"
    
    
    
def load_images():
    global images
    images['archer'] = pygame.image.load("picturs_troops/archer.png")
    images['tank1'] = pygame.image.load("picturs_troops/tank1.jpeg")
    images['attacker'] = pygame.image.load("picturs_troops/attacker.png")
    tankselect = pygame.image.load("picturs_troops/tankselect.jpeg")
    images['tankselect'] = pygame.transform.scale(tankselect, (80, 80))


def main():

    pygame.init()
    load_images()
    screen = pygame.display.set_mode()
    player_tower1 = Tower("left", 300, screen, tank_img=images['tank1'], attacker_img=images['attacker'], archer_img=images['archer'])
    player_tower2 = Tower("right", 300, screen, tank_img=images['tank1'], attacker_img=images['attacker'], archer_img=images['archer'])
    player_tower2.add_troop('tank')
    # Load the image file
    # # Scale the image to a width of 200 pixels and a height of 100 pixels
    # scaled_image = pygame.transform.scale(tank1, (200, 100))
    # scaled_image = pygame.transform.scale(dmg1, (200, 100))
    running = True
    mouse_pos = (0, 0)
    i = 0
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                i += 1
                mouse_pos = pygame.mouse.get_pos()
                choise = select(screen, player_tower1.size, mouse_pos)
                if choise:
                    player_tower1.add_troop(choise)
                print(choise)   
        screen.fill((0, 0, 0))
        # Draw the image onto the window

        seliction(screen, player_tower1.size) 
        Tower.update(player_tower1, player_tower2)
        player_tower1.draw()
        player_tower2.draw()
               
                            
        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()
