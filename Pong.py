import turtle

window = turtle.Screen()
window.title("Pong Tutorial Project")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #stops window from automatically updating


##################################################################################################################
#Score

scoreA = 0
scoreB = 0
##################################################################################################################
#Paddle A

"""small 't' for object name, BIG 'T' for Class name"""
paddleA = turtle.Turtle()
paddleA.speed(0) #Speed of animation 0=MAX Speed
paddleA.shape("square")
paddleA.color("red")
paddleA.shapesize(stretch_wid=5, stretch_len=1) #Default size is 20px by 20px
paddleA.penup() #By default Pen is down.
paddleA.goto(-350,0) #Middle of screen is 0,0.  Negative to the Left, Positive to the Right

#Paddle B

"""small 't' for object name, BIG 'T' for Class name"""
paddleB = turtle.Turtle()
paddleB.speed(0) #Speed of animation 0=MAX Speed
paddleB.shape("square")
paddleB.color("blue")
paddleB.shapesize(stretch_wid=5, stretch_len=1) #Default size is 20px by 20px
paddleB.penup() #By default Pen is down.
paddleB.goto(350,0) #Middle of screen is 0,0.  Negative to the Left, Positive to the Right

#Ball

"""small 't' for object name, BIG 'T' for Class name"""
ball = turtle.Turtle()
ball.speed(0) #Speed of animation 0=MAX Speed
ball.shape("square")
ball.color("white")
ball.shapesize() #Default size is 20px by 20px
ball.penup() #By default Pen is down.
ball.goto(0,0) #Middle of screen is 0,0.  Negative to the Left, Positive to the Right
ball.dx = .05 #'d' = Delta.  Moves by .05px
ball.dy = .05 #'d' = Delta.  Moves by .05px

#Draw Score

pen = turtle.Turtle()
pen.speed(0)
pen.color("DarkOrchid3")
pen.penup() #By default Pen is down.
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} | Player B: {}".format(scoreA, scoreB), align="center", font=("Curier", 24, "normal"))
##################################################################################################################
#Function for paddleA

def paddleA_up():
    y = paddleA.ycor() #name of Object and .ycor returns the y coordinate of paddleA
    y += 20
    paddleA.sety(y) #Set the y to the new y

def paddleA_down():
    y = paddleA.ycor() #name of Object and .ycor returns the y coordinate of paddleA
    y -= 20
    paddleA.sety(y) #Set the y to the new y

#Function for paddleB
def paddleB_up():
    y = paddleB.ycor() #name of Object and .ycor returns the y coordinate of paddleB
    y += 20
    paddleB.sety(y) #Set the y to the new y

def paddleB_down():
    y = paddleB.ycor() #name of Object and .ycor returns the y coordinate of paddleB
    y -= 20
    paddleB.sety(y) #Set the y to the new y
##################################################################################################################
#Keyboard Binding

window.listen()
window.onkeypress(paddleA_up, "w") #Listen for the def paddleA_up
window.onkeypress(paddleA_down, "s") #Listen for the def paddleA_down
window.onkeypress(paddleB_up, "Up") #Listen for the def paddleB_up
window.onkeypress(paddleB_down, "Down") #Listen for the def paddleB_down
##################################################################################################################
#Main Game Loop

while True:
    window.update()#Everytime game is ran, window updates

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #Reverses direction

        

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #Reverses direction
      
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(scoreA, scoreB), align="center", font=("Curier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(scoreA, scoreB), align="center", font=("Curier", 24, "normal"))

    #Paddle Hit
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

              

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

        
