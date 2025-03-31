#added for group 32 project

import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, screen, sprite_collection, x, y, level):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.level = level
        self.triggered = False
        self.type = "Goal" 

        #loads the image of the flag
        self.image = pygame.image.load("./img/flag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 90))
        self.rect = self.image.get_rect() 
        self.rect.topleft = ((x * 32) +20, y * 32) 
        
    def update(self, camera):
        if not self.triggered:
            self.screen.blit(self.image,((self.x + camera.pos.x) * 32, (self.y * 32)+70))

