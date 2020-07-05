import turtle

window = turtle.Screen()    #make and name the window
window.title("Pong")        #title on top of window
window.bgcolor("black")     #background color
window.setup(width=800, height=600) #size of window
window.tracer(0)            #speed up the game 


# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()      #turtle object
paddle_a.speed(0)           #max speed of animation 
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)      #beginning position

# Paddle B
paddle_b = turtle.Turtle()      #turtle object
paddle_b.speed(0)           #max speed of animation 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)      #beginning position

# Ball
ball = turtle.Turtle()      #turtle object
ball.speed(0)           #max speed of animation 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)      #beginning position
ball.dx = 2         # speed on x axis 
ball.dy = 2         # speed on y axis

# Pen (score board)
pen = turtle.Turtle()
pen.speed(0)        # animation speed not movement
pen.color("white")
pen.penup()         #don't want a line ?
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()      #returns the y coordinate
    y += 20                  #moves coordinate up 20 pixels
    paddle_a.sety(y)         #set this new coordinate

def paddle_a_down():
    y = paddle_a.ycor()      #returns the y coordinate
    y -= 20                  #moves coordinate up 20 pixels
    paddle_a.sety(y)         #set this new coordinate

def paddle_b_up():
    y = paddle_b.ycor()      #returns the y coordinate
    y += 20                  #moves coordinate up 20 pixels
    paddle_b.sety(y)         #set this new coordinate

def paddle_b_down():
    y = paddle_b.ycor()      #returns the y coordinate
    y -= 20                  #moves coordinate up 20 pixels
    paddle_b.sety(y)         #set this new coordinate

# Keyboard binding
window.listen()             #tells window to listen for keyboard input
window.onkeypress(paddle_a_up, "w") # call function paddle_a_up() when w is pressed
window.onkeypress(paddle_a_down, "s") # call function paddle_a_down() when s is pressed
window.onkeypress(paddle_b_up, "Up")  # uses the up arrow key
window.onkeypress(paddle_b_down, "Down") # uses the down arrow kep

# MAIN GAME LOOP
while True:
    window.update() 
    #everytime the loop runs the screen updates

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:       #290 because height is 600 (so +300 is top border) and ball is 20 px high
        ball.sety(290)          
        ball.dy *= -1           #reverses direction
    if ball.ycor() < -290:       #290 because height is 600 (so -300 is bottom border) and ball is 20 px high
        ball.sety(-290)          
        ball.dy *= -1           #reverses direction

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1   
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1