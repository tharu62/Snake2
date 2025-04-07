from turtle import delay
import pygame
import random
from snake import Snake
from snake import Direction
from pygame.locals import *
from enum import Enum
    
def random_apple(n):
    apple_is_on_snake = True
    if n == 1:
        rand_apple = pygame.Rect(0, 0, 9, 9)
    elif n == 2:
        rand_apple = pygame.Rect(410, 0, 9, 9)        
    while apple_is_on_snake:
        if n == 1:
            rand_apple.x = 0
            rand_apple.y = 0
            rand_apple.move_ip(random.randint(1,37)*10, random.randint(1, 52)*10)
            apple_is_on_snake = False
            if rand_apple.x == green_snake.head.x and rand_apple.y == green_snake.head.y:
                apple_is_on_snake = True
            for i in green_snake.body:
                if rand_apple.x == i.x and rand_apple.y == i.y:
                    apple_is_on_snake = True
                    break
            for i in forest:
                if rand_apple.x == i.x and rand_apple.y == i.y:
                    apple_is_on_snake = True        
                    break
        elif n == 2:
            rand_apple.x = 410
            rand_apple.y = 0
            rand_apple.move_ip(random.randint(1,37)*10, random.randint(1, 52)*10)
            apple_is_on_snake = False
            if rand_apple.x == yellow_snake.head.x and rand_apple.y == yellow_snake.head.y:
                apple_is_on_snake = True
            for i in yellow_snake.body:
                if rand_apple.x == i.x and rand_apple.y == i.y:
                    apple_is_on_snake = True
                    break
            for i in rotten_forest:
                if rand_apple.x == i.x and rand_apple.y == i.y:
                    apple_is_on_snake = True        
                    break
    return rand_apple     

def random_obstacle(n):
    obstacle_is_on_snake = True
    if n == 1:
        obstacle = pygame.Rect(0, 0, 9, 9)
    elif n == 2:
        obstacle = pygame.Rect(410, 0, 9, 9)        
    while obstacle_is_on_snake:
        if n == 1:
            obstacle.x = 0
            obstacle.y = 0
            obstacle.move_ip(random.randint(1,38)*10, random.randint(1, 52)*10)
            obstacle_is_on_snake = False
            if obstacle.x == green_snake.head.x and obstacle.y == green_snake.head.y:
                obstacle_is_on_snake = True
            for i in green_snake.body:
                if obstacle.x == i.x and obstacle.y == i.y:
                    obstacle_is_on_snake = True
                    break
            for i in forest:
                if obstacle.x == i.x and obstacle.y == i.y:
                    obstacle_is_on_snake = True        
                    break
        elif n == 2:
            obstacle.x = 410
            obstacle.y = 0
            obstacle.move_ip(random.randint(1,38)*10, random.randint(1, 52)*10)
            obstacle_is_on_snake = False
            if obstacle.x == yellow_snake.head.x and obstacle.y == yellow_snake.head.y:
                obstacle_is_on_snake = True
            for i in yellow_snake.body:
                if obstacle.x == i.x and obstacle.y == i.y:
                    obstacle_is_on_snake = True
                    break
            for i in rotten_forest:
                if obstacle.x == i.x and obstacle.y == i.y:
                    obstacle_is_on_snake = True        
                    break
    # obstacle.move_ip(random.randint(1,38)*10, random.randint(1, 52)*10)
    return obstacle

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
forest = []
rotten_forest = []

# Set up the walls that trap the snakes
# muro centrale verticale
for i in range(0, 60):
    temp = pygame.Rect(400, 0, 9, 9)
    temp.move_ip(0, 10*i)
    wall.append(temp)
# muro superiore 
for i in range(60, 141):
    temp = pygame.Rect(0, 0, 9, 9)
    temp.move_ip(10*(i-61), 0)
    wall.append(temp)
# muro centrale orizzontale 
for i in range(141, 222):
    temp = pygame.Rect(0, 530, 9, 9)
    temp.move_ip(10*(i-141), 0)
    wall.append(temp)
# muro laterale sinistro   
for i in range(222, 282):
    temp = pygame.Rect(0, 0, 9, 9)
    temp.move_ip(0, 10*(i-222))
    wall.append(temp)
# muro laterale destro
for i in range(282, 342):
    temp = pygame.Rect(800, 0, 9, 9)
    temp.move_ip(0, 10*(i-282))
    wall.append(temp)
# muro inferiore orizzontale    
for i in range(342, 423):
    temp = pygame.Rect(0, 590, 9, 9)
    temp.move_ip(10*(i-342), 0)
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
CPU_SCORE = 0
GameOver = False
Pause = False
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
    
    if key[pygame.K_p] == True:
        Pause = not Pause
        pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not Pause:

        green_snake.move(dir)
        if green_snake.out_of_bound() or green_snake.bonk() or green_snake.hit_obstacle(forest):
            GameOver = True
            Pause = True
            break

        if green_snake.head.x == apple.x and green_snake.head.y == apple.y:
            green_snake.eat()
            forest.append(random_obstacle(1))
            apple = random_apple(1)
            SCORE += 1   
        
        # this is the code to visualize the path of A_Star_hunt on the map
        # pygame.draw.rect(screen, (255, 0, 255), Rect(yellow_snake.head.x-410, yellow_snake.head.y, 9, 9))
        # for i in range(0, 41):
        #     for j in range(0, 53):
        #         if yellow_snake.temp_map[i][j] == 0:
        #             pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i*10+410, j*10, 9, 9))

        # uncomment the type of hunt you want to use
        # yellow_snake.hunt(rotten_apple, wall, rotten_forest)
        # yellow_snake.Dijkstra_hunt(rotten_apple, wall, rotten_forest)
        yellow_snake.A_star_hunt(rotten_apple, wall, rotten_forest)

        if yellow_snake.head.x == rotten_apple.x and yellow_snake.head.y == rotten_apple.y:
            rotten_forest.append(random_obstacle(2))
            rotten_apple = random_apple(2)
            CPU_SCORE += 1
            
        pygame.draw.rect(screen, (255, 0, 0), apple)
        pygame.draw.rect(screen, (255, 255, 0), green_snake.head)
        for i in green_snake.body:
            pygame.draw.rect(screen, (0, 200, 0), i)
        
        pygame.draw.rect(screen, (128, 0, 128), rotten_apple)   
        pygame.draw.rect(screen, (255, 0, 255), yellow_snake.head)
        for j in yellow_snake.body:
            pygame.draw.rect(screen, (200, 200, 0), j)
        
        for i in wall:
            pygame.draw.rect(screen, (0, 0, 255), i)
        for i in rotten_forest:
            pygame.draw.rect(screen, (55, 55, 55), i)
        for i in forest:    
            pygame.draw.rect(screen, (0, 100, 0), i)

        score = font.render("SCORE : "+str(SCORE), True, (0, 255, 0), (0, 0, 0))
        cpu_score = font.render("CPU SCORE : "+str(CPU_SCORE), True, (255, 255, 0), (0, 0, 0))
        screen.blit(score, (20,555))    
        screen.blit(cpu_score, (420, 555))

        pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()

