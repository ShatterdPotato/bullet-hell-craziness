import pygame
import random

class Laser:
    def __init__(self):
        self.x = random.randint(0,800)
        self.y = random.randint(0,600)


    def attack(self, stage, player, screen, end_pos):
        match stage:
            case 1:
                pygame.draw.line(screen, (255,0,0), (self.x,self.y), (player.rect.centerx,player.rect.centery), 5)
                end_pos = player.rect.center 
                end_pos = (100*(end_pos[0]-self.x),100*(end_pos[1]-self.y))
                return end_pos
            case 2:
                pygame.draw.line(screen, (255,0,0), (self.x,self.y), end_pos, 5)
            case 3:
               pygame.draw.line(screen, (255,0,0), (self.x,self.y), end_pos, 25)
               pygame.draw.circle(screen, (255,0,0), (self.x,self.y), 25)

