import pygame
from pygame.locals import *

class box():
    def __init__(self, x, y):
        self.x = x
        self.y = y    

class snake():
    head = box
    tail = box 
    body = box

    def __init__(self, head):
        self.head = head

    def return_head(self):
        return self.head
    
    def return_tail(self):
        return self.tail
    
    def return_body(self):
        return self.body

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HIGHT))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)        

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

