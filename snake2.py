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

def main():
    h = box(0,0)
    mySnake = snake(h)
    print()

if __name__ == "__main__":
    main()

