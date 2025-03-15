from turtle import down
import pygame
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

    def eat(self):
        tail = Rect(self.head.x, self.head.y, 9 ,9)   
        if len(self.body) == 1:         
            if self.body[0].x == self.head.x:
                if self.body[0].y > self.head.y:
                    tail.move_ip(0, -10)
                else:
                    tail.move_ip(0, 10)
            else:
                if self.body[0].x > self.head.x:
                    tail.move_ip(10, 0)
                else:
                    tail.move_ip(-10, 0) 
        else:
            tail.x = self.body[len(self.body)-1].x
            tail.y = self.body[len(self.body)-1].y
            if self.body[len(self.body)-1].x == self.body[len(self.body)-2].x:
                if self.body[len(self.body)-1].y > self.body[len(self.body)-2].y:
                    tail.move_ip(0, -10)
                else:
                    tail.move_ip(0, 10)
            else:
                if self.body[len(self.body)-1].x > self.body[len(self.body)-2].x:
                    tail.move_ip(10, 0)
                else:
                    tail.move_ip(-10, 0)    
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
        
        return
    
    # Implement the Dijkstra algorithm to find the shortest path to the apple
    def Dijkstra_hunt(self, apple, wall, forest):
            
        return
    