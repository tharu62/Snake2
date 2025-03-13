import pygame
import time
import random
from pygame.locals import *
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

class Snake():
    head = Rect
    body = []

    def __init__(self, head):
        self.head = head
        self.body.append(Rect((head.x+10, head.y+10, 9, 9)))

    def move(self, direction):
        self.body[0].x = self.head.x
        self.body[0].y = self.head.y
        for i in range(0, len(self.body)-1):
            self.body[len(self.body)-1-i].x = self.body[len(self.body)-2-i].x
            self.body[len(self.body)-1-i].y = self.body[len(self.body)-2-i].y
        match direction:
            case Direction.UP:
                self.head.move_ip(0, -10)
            case Direction.DOWN:
                self.head.move_ip(0, 10)
            case Direction.LEFT:
                self.head.move_ip(-10, 0)
            case Direction.RIGHT:
                self.head.move_ip(10, 0)

    def eat(self, direction):
        tail = Rect((self.body[len(self.body)-1].x, self.body[len(self.body)-1].y, 9 ,9))
        match direction:
            case Direction.UP:
                tail.move_ip(0, 10)
            case Direction.DOWN:
                tail.move_ip(0, -10)
            case Direction.LEFT:
                tail.move_ip(10, 0)
            case Direction.RIGHT:
                tail.move_ip(-10, 0)
        self.body.append(tail)

    def out_of_bound(self):
        if self.head.x == 400 or self.head.x == 0:
            return True
        if self.head.y == 590 or self.head.y == -10:
            return True
        return False
    
    def bonk(self):
        for i in self.body:
            if self.head.x == i.x and self.head.y == i.y:
                return True
        return False
    
def random_apple():
    apple = pygame.Rect((0, 0, 9, 9))
    apple.move_ip(random.randint(1,3)*10, random.randint(1, 7)*10)
    return apple     


pygame.init()

SCREEN_WIDHT = 810
SCREEN_HIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HIGHT))

green_snake = Snake(pygame.Rect((190, 290, 9, 9))) 
apple = pygame.Rect(((200, 200, 9, 9)))
wall = []

# Set up WALLMARIA
for i in range(0, 60):
    temp = pygame.Rect((400, 0, 9, 9))
    temp.move_ip(0, 10*i)
    wall.append(temp)
for i in range(61, 143):
    temp = pygame.Rect((0, -10, 9, 9))
    temp.move_ip(10*(i-61), 10)
    wall.append(temp)
for i in range(143, 226):
    temp = pygame.Rect((0, 590, 9, 9))
    temp.move_ip(10*(i-143), 0)
    wall.append(temp)
for i in range(226, 287):
    temp = pygame.Rect((0, 0, 9, 9))
    temp.move_ip(0, 10*(i-226))
    wall.append(temp)
for i in range(287, 348):
    temp = pygame.Rect((800, 0, 9, 9))
    temp.move_ip(0, 10*(i-287))
    wall.append(temp)

# Set up the player and the apple on screen
pygame.draw.rect(screen, (255, 0, 0), apple)
pygame.draw.rect(screen, (255, 255, 0), green_snake.head)
for i in green_snake.body:
    pygame.draw.rect(screen, (0, 255, 0), i)
dir = Direction.RIGHT
update_time = 0.05

# Game Loop
run = True
FRAME_COUNT = 0
while run:

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
    elif key[pygame.K_SPACE] == True:
        update_time = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    FRAME_COUNT += 1
    if FRAME_COUNT == 500:
        green_snake.move(dir)
        if green_snake.out_of_bound() or green_snake.bonk():
            run = False
        
        if green_snake.head.x == apple.x and green_snake.head.y == apple.y:
            green_snake.eat(dir)
            apple = random_apple()   
        
        pygame.draw.rect(screen, (255, 0, 0), apple)
        pygame.draw.rect(screen, (255, 255, 0), green_snake.head)
        for i in green_snake.body:
            pygame.draw.rect(screen, (0, 255, 0), i)
        for i in range(0,347):
            pygame.draw.rect(screen, (0, 0, 255), wall[i])    

        pygame.display.update()
        FRAME_COUNT = 0

pygame.quit()

