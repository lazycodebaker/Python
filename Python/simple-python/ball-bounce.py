import turtle as t

w=t.Screen()
w.title('Bounce')
w.bgcolor('black')

ball=t.Turtle()
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.speed(0)
ball.goto(0,200)

ball.dy=0
gravity=0.1
c=1


while True:

     ball.dy-=gravity
     ball.sety(ball.ycor()+ball.dy)

     if ball.ycor()<-300:

          ball.dy*=-1
          c=c+1

          def red():
               ball.color('red')
          def green():
               ball.color('green')

               

          if c%2==0:
               red()
         
          else:
               green()
          