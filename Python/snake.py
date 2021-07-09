
import pygame
import sys
import random
from pygame import draw
from pygame.display import update

WIDTH = 480
HEIGHT = 480

GRIDSIZE = 20

GRID_WIDTH = WIDTH / GRIDSIZE
GRID_HEIGHT = HEIGHT / GRIDSIZE

UP    = (0,-1)
DOWN  = (0,1)
LEFT  = (-1,0)
RIGHT = (1,0)


class Snake(object):
    def __init__(self):
        self.length = 1
        self.pos = [((WIDTH / 2),(HEIGHT / 2))]
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
        self.color = (17,24,47)
    
    def get_head_pos(self):
        return self.pos[0]
    
    def turn(self,point):
        if (self.length > 1 and (point[1] * -1) == self.direction):
            return 
        else:
            self.direction = point
    
    def move(self):
        pass
    
    def reset(self):
        pass

    def draw(self):
        pass
    
    def handle_keys(self):
        pass
  

class Food(object):
    def __init__(self):
        pass

    def random_pos(self):
        pass

    def draw(self):
        pass


def drawGrid(surface):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                draw.rect(surface,(93,216,228),r)
            else:
                rr = pygame.Rect((x*GRIDSIZE,y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                draw.rect(surface,(84,194,205),rr)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    drawGrid(surface)

    snake = Snake()
    food = Food()

    score = 0

    while True:
        clock.tick(10)

        screen.blit(surface,(0,0))
        update()

main()

