import pygame
from pygame.locals import *
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

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

    def eat(self, direction):
        tail = Rect(self.body[len(self.body)-1].x, self.body[len(self.body)-1].y, 9 ,9)
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
        if self.head.y == 530 or self.head.y == -10:
            return True
        return False
    
    def bonk(self):
        for i in self.body:
            if self.head.x == i.x and self.head.y == i.y:
                return True
        return False