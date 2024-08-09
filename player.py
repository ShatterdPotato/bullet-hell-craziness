import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xvelocity = 0
        self.yvelocity = 0
        self.termxvelocity = 5
        self.termyvelocity = 5 
        self.image = pygame.image.load("player.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x,self.y,self.image_size[0],self.image_size[1])

    def move(self,keys):
        moving_y = False
        moving_x = False
        if keys[pygame.K_d]:
            moving_x = True
            self.xvelocity += 1
        if keys[pygame.K_a]:
            moving_x = True
            self.xvelocity -= 1
        if keys[pygame.K_SPACE]:
            moving_y = True
            self.yvelocity -= 2

        # if self.yvelocity > self.termyvelocity:
        #     self.yvelocity = self.termyvelocity
        elif self.yvelocity < -(self.termyvelocity):
            self.yvelocity = -(self.termyvelocity)

        if self.xvelocity > self.termxvelocity:
            self.xvelocity = self.termxvelocity
        elif self.xvelocity < -(self.termxvelocity):
            self.xvelocity = -(self.termxvelocity)

        if not moving_x:
            if self.xvelocity > 0:
                self.xvelocity = round(self.xvelocity - 1, 1)
            elif self.xvelocity < 0:
                self.xvelocity = round(self.xvelocity + 1, 1) 
          
        if not moving_y:
            if self.rect.bottom < 600:
                self.yvelocity += 1
                
            if self.rect.bottom > 600:
                self.yvelocity = 0
                self.y = 600 - self.image_size[1]
                
        if self.rect.top < 0:
            self.yvelocity = 0
            self.y = 0
        if self.rect.left < 0:
            self.xvelocity = 0
            self.x = 0   
        if self.rect.right > 800:
            self.xvelocity = 0
            self.x = 800 - self.image_size[0]
 
        self.x += self.xvelocity
        self.y += self.yvelocity
        self.rect = pygame.Rect(self.x,self.y,self.image_size[0],self.image_size[1])


