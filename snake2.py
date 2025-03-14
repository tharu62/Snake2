import pygame
import time
import random
from snake import Snake
from snake import Direction
from pygame.locals import *
from enum import Enum
    
def random_apple(n):
    if n == 1:
        apple = pygame.Rect(0, 0, 9, 9)
    elif n == 2:
        apple = pygame.Rect(410, 0, 9, 9)        
    apple.move_ip(random.randint(1,39)*10, random.randint(1, 52)*10)
    return apple     

pygame.init()

timer = pygame.time.Clock()

SCREEN_WIDHT = 810
SCREEN_HIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HIGHT))

green_snake = Snake(pygame.Rect(190, 290, 9, 9))
yellow_snake = Snake(pygame.Rect(590, 290, 9, 9)) 
apple = pygame.Rect(200, 200, 9, 9)
rotten_apple = pygame.Rect(600, 200, 9, 9)
wall = []

# Set up WALLMARIA
for i in range(0, 60):
    temp = pygame.Rect(400, 0, 9, 9)
    temp.move_ip(0, 10*i)
    wall.append(temp)
for i in range(61, 143):
    temp = pygame.Rect(0, -10, 9, 9)
    temp.move_ip(10*(i-61), 10)
    wall.append(temp)
for i in range(143, 226):
    temp = pygame.Rect(0, 530, 9, 9)
    temp.move_ip(10*(i-143), 0)
    wall.append(temp)
for i in range(226, 287):
    temp = pygame.Rect(0, 0, 9, 9)
    temp.move_ip(0, 10*(i-226))
    wall.append(temp)
for i in range(287, 348):
    temp = pygame.Rect(800, 0, 9, 9)
    temp.move_ip(0, 10*(i-287))
    wall.append(temp)
for i in range(349, 430):
    temp = pygame.Rect(0, 590, 9, 9)
    temp.move_ip(10*(i-349), 0)
    wall.append(temp)    

# Set up the apples and game parameters
pygame.draw.rect(screen, (255, 0, 0), apple)
pygame.draw.rect(screen, (128, 0, 128), rotten_apple)   
dir = Direction.RIGHT
update_time = 0.05

# Set up the font for rendering the score
font = pygame.font.SysFont(None, 35)
yellow = (255, 255, 0)
black = (0, 0, 0)

# Game Loop
run = True
FRAMERATE = 20
PAUSE = 0
SCORE = 0
while run:

    timer.tick(FRAMERATE)

    screen.fill((0,0,0))
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        dir = Direction.LEFT
    elif key[pygame.K_RIGHT] == True:
        dir = Direction.RIGHT
    elif key[pygame.K_UP] == True:
        dir = Direction.UP
    elif key[pygame.K_DOWN] == True:
        dir = Direction.DOWN
    elif key[pygame.K_p] == True:
        if PAUSE == 1:
            PAUSE = 0
        else:
            PAUSE = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # green_snake.move(dir)
    # if green_snake.out_of_bound() or green_snake.bonk():
    #     run = False
    
    # if green_snake.head.x == apple.x and green_snake.head.y == apple.y:
    #     green_snake.eat(dir)
    #     apple = random_apple(1)
    #     SCORE += 1   
    
    pygame.draw.rect(screen, (255, 0, 0), apple)
    pygame.draw.rect(screen, (255, 255, 0), green_snake.head)
    for i in green_snake.body:
        pygame.draw.rect(screen, (0, 255, 0), i)
    
    pygame.draw.rect(screen, (128, 0, 128), rotten_apple)   
    pygame.draw.rect(screen, (255, 0, 255), yellow_snake.head)
    for j in yellow_snake.body:
        pygame.draw.rect(screen, (200, 200, 0), j)
    
    yellow_snake.hunt(rotten_apple)

    if yellow_snake.head.x == rotten_apple.x and yellow_snake.head.y == rotten_apple.y:
        rotten_apple = random_apple(2)
        yellow_snake.eat(dir)

    for i in range(0,428):
        pygame.draw.rect(screen, (0, 0, 255), wall[i])

    score = font.render("SCORE : "+str(SCORE), True, yellow, black)
    screen.blit(score, (20,555))        

    pygame.display.update()

pygame.quit()

