

import pygame as pyg
import random
import pygame.display as display
import sys
import pygame.draw as draw
import pygame.font as font
import pygame.time as time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

GRID_SIZE = 20

GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

UP    = (0,-1)
DOWN  = (0,1)
RIGHT = (1,0)
LEFT  = (-1,0)

class Snake(object):
    def __init__(self):
        self.length = 1
        self.pos = [((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP,DOWN,RIGHT,LEFT])
        self.color = (17,24,47)        

    def get_head_pos(self):
        return self.pos[0]

    def turn(self,point):
        if self.length > 1 and (point[0] *-1,point[1] *-1) == self.direction:
            return 
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_pos()
        x,y = self.direction
        new = (((cur[0] + (x*GRID_SIZE)) % SCREEN_WIDTH),(cur[1] +(y * GRID_SIZE)) % SCREEN_HEIGHT)

        if len(self.pos) > 2 and new in self.pos[2:]:
            self.reset()
        else : 
            self.pos.insert(0,new)
            if len(self.pos) > self.length :
                self.pos.pop()

    def reset(self):
        self.length = 1
        self.pos = [((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))]               
        self.direction = random.choice([UP,DOWN,RIGHT,LEFT])

    def draw(self,surface):
        for p in self.pos:
            r = pyg.Rect((p[0],p[1]),(GRID_SIZE,GRID_SIZE))
            draw.rect(surface,self.color,r)
            draw.rect(surface,(93,216,228),r,1)            
            
    def handle_inputs(self):
        for event in pyg.event.get():
            if (event.type == pyg.QUIT):
                pyg.quit()
                sys.exit()
            elif (event.type == pyg.KEYDOWN):
                if event.key == pyg.K_UP:
                    self.turn(UP)
                if event.key == pyg.K_DOWN:
                    self.turn(DOWN)
                if event.key == pyg.K_LEFT:
                    self.turn(LEFT)
                if event.key == pyg.K_RIGHT:
                    self.turn(RIGHT)    
            
class Food(object):
    def __init__(self):
        self.pos = (0,0)
        self.color = (223,163,49)
        self.get_random_pos()

    def get_random_pos(self):
        self.pos = ((random.randint(0,GRID_WIDTH - 1) * GRID_SIZE) , (random.randint(0,GRID_HEIGHT - 1) * GRID_SIZE))        

    def draw(self,surface):
        food = pyg.Rect((self.pos[0],self.pos[1]),(GRID_SIZE,GRID_SIZE))
        draw.rect(surface,self.color,food)

def drawGrid(surface):
    for y in range(0,int(GRID_HEIGHT)):
        for x in range(0,int(GRID_WIDTH)):
            r = pyg.Rect((x * GRID_SIZE,y * GRID_SIZE),(GRID_SIZE,GRID_SIZE))

            if((x + y) % 2 == 0):
                draw.rect(surface,(93,216,228),r)
            else : 
                draw.rect(surface,(84,194,205),r)

def main():
    pyg.init()

    clock  = time.Clock()
    screen = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
    
    surface = pyg.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    food = Food()
    snake = Snake()
    score = 0 

    while(True):
        clock.tick(10)

        snake.handle_inputs()
        drawGrid(surface)
        snake.move()

        if snake.get_head_pos() == food.pos:
            print(snake.pos,food.pos)
            snake.length += 1
            score += 1
            food.get_random_pos()
        
        snake.draw(surface)
        food.draw(surface)

        screen.blit(surface,(0,0))
        print("SCORE :: {0}".format(score))
        display.update()

main()