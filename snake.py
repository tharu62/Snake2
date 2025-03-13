import pygame



class box:
    def _init_(self, x, y):
        self.x = x
        self.y = y    


class snake:

    tail = 1
    body = 2

    def _init_(self,head):
        self.head = head
    
    
    def return_head(self):
        return head

    def return_tail(self):
        return tail

    def return_body(self):
        return body

def main():

    h = box(0,0)
    mySnake = snake(h)
    print(mySnake.return_head())

if __name__ == "__main__":
    main()

