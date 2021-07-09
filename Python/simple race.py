import tkinter
from tkinter import *
import random as r
import time as t
root=Tk()
root.title("Race")
canvas =Canvas(root,width=500,height=500,bg='pink')
button=Button(root,text="Click to Close",command=quit)

button.pack()
root.resizable(0,0)
canvas.pack()
  

class Race:
    
    def __init__(self,canvas,color):
        
        self.canvas=canvas
        
        self.rect1=self.canvas.create_rectangle(0,0,20,20,fill=color)
        self.rect2=self.canvas.create_rectangle(0,0,20,20,fill=color)
        self.rect3=self.canvas.create_rectangle(0,0,20,20,fill=color)
        self.rect4=self.canvas.create_rectangle(0,0,20,20,fill=color)
        
        
        self.start=False

        self.canvas.move(self.rect1,100,110)
        
        self.canvas.create_text(30,120,text='Player1')
        
        self.canvas.move(self.rect2,100,140)
        
        self.canvas.create_text(30,150,text='Player2')
        
        self.canvas.move(self.rect3,100,170)
        
        self.canvas.create_text(30,180,text='Player3')
        
        self.canvas.move(self.rect4,100,200)
        
        self.canvas.create_text(30,210,text='Player4')
        
        self.win_rect=False


        line=self.canvas.create_line(400,0,400,500,fill='red')
        
        self.x=[]

        for i in range(7,11):
            self.x.append(i)

        r.shuffle(self.x)
        
        self.y=0

    def moverect(self):
        
        self.canvas.move(self.rect1,self.x[0],self.y)
        self.canvas.move(self.rect2,self.x[1],self.y)
        self.canvas.move(self.rect3,self.x[2],self.y)
        self.canvas.move(self.rect4,self.x[3],self.y)

        self.big=max(self.x)

        self.small=min(self.x)
        
        self.canvas.update()
        
        r1=self.canvas.coords(self.rect1)
        r2=self.canvas.coords(self.rect2)
        r3=self.canvas.coords(self.rect3)
        r4=self.canvas.coords(self.rect4)

        self.win(r1,'Player 1')
        self.win(r2,'Player 2')
        self.win(r3,'Player 3')
        self.win(r4,'Player 4')

    def win(self,point,name):
        
        self.point=point
        self.name=name

        if self.point[2]>=400:
            self.win_rect=True
            self.winner=self.name
            

race=Race(canvas,'orange')

while(1):
    if race.win_rect==False:
        race.moverect()
    else:
        canvas.create_text(150,50,text="Winner :: "+str(race.winner),font=('Aerial',15),fill='green')
        
    t.sleep(0.1)
    root.update()
    root.update_idletasks()
        



