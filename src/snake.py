from re import A
from turtle import down, update
import pygame
import src.algorithms as algorithms
from pygame.locals import *
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    NONE = 5

class Snake():

    def __init__(self, head):
        self.head = head
        self.body = []
        self.body.append(pygame.Rect(head.x+10, head.y, 9, 9))
        self.map =  [[1]*54 for i in range(41)]
        # this piece of code is for testing the A* algorithm and see the path constructed by the algorithm 
        # self.temp_map = [[1]*54 for i in range(41)]

    def move(self, direction):
        if len(self.body) > 1:
            if len(self.body) == 2:
                self.body[1].x = self.body[0].x
                self.body[1].y = self.body[0].y
            else:
                for i in reversed(range(1, len(self.body)-1)):
                    self.body[i].x = self.body[i-1].x
                    self.body[i].y = self.body[i-1].y
        self.body[0].x = self.head.x
        self.body[0].y = self.head.y 
        match direction:
            case Direction.UP:
                self.head.move_ip(0, -10)
            case Direction.DOWN:
                self.head.move_ip(0, 10)
            case Direction.LEFT:
                self.head.move_ip(-10, 0)
            case Direction.RIGHT:
                self.head.move_ip(10, 0)
            case Direction.NONE:
                pass

    def eat(self):
        tail = pygame.Rect(0, 0, 9 ,9)   
        self.body.append(tail)

    def out_of_bound(self):
        if self.head.x == 400 or self.head.x == 0:
            return True
        if self.head.y == 530 or self.head.y == -10:
            return True
        return False
    
    def bonk(self):
        for i in self.body:
            if self.head.x == i.x and self.head.y == i.y:
                return True
        return False
    
    def hit_obstacle(self, obstacle):
        for i in obstacle:
            if self.head.x == i.x and self.head.y == i.y:
                return True
        return False

    def hunt(self, apple, wall, forest):
        right = True
        left = True
        up = True
        down = True
        for i in self.body:
            if self.head.x+10 == i.x and self.head.y == i.y:
                right = False
            if self.head.x-10 == i.x and self.head.y == i.y:
                left = False
            if self.head.x == i.x and self.head.y-10 == i.y:
                up = False
            if self.head.x == i.x and self.head.y+10 == i.y:
                down = False
        for i in wall:
            if self.head.x+10 == i.x and self.head.y == i.y:
                right = False
            if self.head.x-10 == i.x and self.head.y == i.y:
                left = False
            if self.head.x == i.x and self.head.y-10 == i.y:
                up = False
            if self.head.x == i.x and self.head.y+10 == i.y:
                down = False          
        for i in forest:
            if self.head.x+10 == i.x and self.head.y == i.y:
                right = False
            if self.head.x-10 == i.x and self.head.y == i.y:
                left = False
            if self.head.x == i.x and self.head.y-10 == i.y:
                up = False
            if self.head.x == i.x and self.head.y+10 == i.y:
                down = False
        if self.is_close_to(apple):
            self.eat()              
        if apple.x > self.head.x and right:
            self.move(Direction.RIGHT)
        elif apple.x < self.head.x and left:
            self.move(Direction.LEFT)
        elif apple.y > self.head.y and down:
            self.move(Direction.DOWN)
        elif apple.y < self.head.y and up:
            self.move(Direction.UP)
        elif right:
            self.move(Direction.RIGHT)
        elif left:
            self.move(Direction.LEFT)
        elif down:
            self.move(Direction.DOWN)
        elif up:
            self.move(Direction.UP)
    
    # Implement the A* algorithm to find the shortest path to the apple
    def A_star_hunt(self, apple, wall, forest):
        src =[self.head.x//10-41, self.head.y//10]
        dest = [apple.x//10-41, apple.y//10]
        self.update_map(wall, forest)
        next_step = algorithms.a_star_search(self.map, src, dest)
        
        # this piece of code is for testing the A* algorithm and see the path constructed by the algorithm
        # for i in range(0, 41):
        #     for j in range(0, 53):
        #         self.temp_map[i][j] = 1
        # for i in next_step:
        #     self.temp_map[i[0]][i[1]] = 0

        if self.is_close_to(apple):
            self.eat()

        if next_step == None:
            # print("NONE")
            return
        if next_step[1][0]*10 == self.head.x-410 and next_step[1][1]*10 == self.head.y+10:
            self.move(Direction.DOWN)
            return
        elif next_step[1][0]*10 == self.head.x-410 and next_step[1][1]*10 == self.head.y-10:
            self.move(Direction.UP)
            return
        elif next_step[1][0]*10 == self.head.x-410+10 and next_step[1][1]*10 == self.head.y:
            self.move(Direction.RIGHT)
            return
        elif next_step[1][0]*10 == self.head.x-410-10 and next_step[1][1]*10 == self.head.y:
            self.move(Direction.LEFT)
            return
    
    # Implement the Dijkstra algorithm to find the shortest path to the apple
    def Dijkstra_hunt(self, apple, wall, forest):
        return
    
    def update_map(self, wall, forest):
        for i in range(0, 40):
            for j in range(0, 53):
                self.map[i][j] = 1
        for i in self.body:
            self.map[(i.x-410)//10][i.y//10] = 0
        for i in wall:
            if i.x > 400 and i.y < 530:
                self.map[(i.x-400)//10][i.y//10] = 0
        for i in forest:
            self.map[(i.x-410)//10][i.y//10] = 0
        return        

    def is_close_to(self, apple):
        if (self.head.x - apple.x) == 10:
            if self.head.y == apple.y:
                return True
        elif (self.head.x - apple.x) == -10:
            if self.head.y == apple.y:
                return True
        if (self.head.y - apple.y) == 10:
            if self.head.x == apple.x:
                return True
        if (self.head.y - apple.y) == -10:
            if self.head.x == apple.x:
                return True
        return False
    
    