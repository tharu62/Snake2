import pygame
import time
from pygame.locals import *
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

class Snake():
    head = Rect
    body = [Rect((389, 299, 9, 9)), Rect(379, 299, 9, 9), Rect((369, 299, 9, 9))]

    def __init__(self, head):
        self.head = head

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
        tail = Rect((209, 209, 9 ,9))
        tail.x = self.body[len(self.body)-1].x
        tail.y = self.body[len(self.body)-1].y
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

    # def out_of_bound(self, head):
    #     if head.x >


pygame.init()

SCREEN_WIDHT = 831
SCREEN_HIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HIGHT))

green_snake = Snake(pygame.Rect((399, 299, 9, 9))) 
apple = pygame.Rect(((209, 209, 9, 9)))
wall = []

# Set up the player and the apple on screen
for i in range(0, 59):
    temp = pygame.Rect((411, 0, 10, 10))
    temp.move_ip(0, 10*i)
    wall.append(temp)
pygame.draw.rect(screen, (255, 0, 0), apple)
pygame.draw.rect(screen, (255, 255, 0), green_snake.head)
for i in green_snake.body:
    pygame.draw.rect(screen, (0, 255, 0), i)
dir = Direction.RIGHT

# Game Loop
run = True
while run:

    screen.fill((0,0,0))
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        dir = Direction.LEFT
        green_snake.move(dir)
    elif key[pygame.K_RIGHT] == True:
        dir = Direction.RIGHT
        green_snake.move(dir)
    elif key[pygame.K_UP] == True:
        dir = Direction.UP
        green_snake.move(dir)
    elif key[pygame.K_DOWN] == True:
        dir = Direction.DOWN
        green_snake.move(dir)
    else:
        green_snake.move(dir)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # if green_snake

    if green_snake.head.x == apple.x and green_snake.head.y == apple.y:
        green_snake.eat(dir)   

    pygame.draw.rect(screen, (255, 0, 0), apple)
    pygame.draw.rect(screen, (255, 255, 0), green_snake.head)
    for i in green_snake.body:
        pygame.draw.rect(screen, (0, 255, 0), i)

    for i in range(0,59):
        pygame.draw.rect(screen, (0, 0, 255), wall[i])    

    pygame.display.update()
    time.sleep(0.05)

pygame.quit()

