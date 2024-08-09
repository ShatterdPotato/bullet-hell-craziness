import pygame
from player import Player 
from laser import Laser

pygame.init()
screen = pygame.display.set_mode((800,600))
screen_rect = pygame.Rect(0,0,800,600)
pygame.display.set_caption("bullet hell")
run = True
clock = pygame.time.Clock()
player = Player(400,300)
laser = Laser()

laser_tick = 0
end_pos = (0,0)

while run:
    clock.tick(60)
    screen.fill((255,255,255))
    keys = pygame.key.get_pressed()
    player.move(keys)
    if keys[pygame.K_l]:
        laser_tick = 1
    
    print(laser_tick)
    print(end_pos)
    if laser_tick != 0:
        laser_tick += 1
        if laser_tick <= 240:
            end_pos = laser.attack(1, player, screen, end_pos)
        elif laser_tick > 240 and laser_tick <= 360: 
            laser.attack(2, player, screen, end_pos)
        elif laser_tick > 360 and laser_tick <=540:
            laser.attack(3,player,screen,end_pos)
        else:
            laser_tick = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(player.image,player.rect)
    pygame.display.update()
