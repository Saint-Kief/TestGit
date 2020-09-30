import turtle

#set up screen
window = turtle.Screen()
window.title("Hangman Game")
window.bgcolor("light yellow")
window.setup(height=600, width=600) #Better use window.window_height(), window.window_width()
turtle.speed(10)
msg = ("Help")

def draw_noose():
    turtle.penup()
    turtle.color("black")    
    turtle.goto(0,0) #width = 260    
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(120)
    turtle.forward(-60)

    turtle.left(90)
    turtle.width(10)
    turtle.forward(150)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(30)
    turtle.width(2)
    turtle.forward(30)
# draw_noose()

def draw_head():
    turtle.fillcolor("white") 
    # Start filling the color 
    turtle.begin_fill() 
    # Draw a circle 
    turtle.circle(15) 
    # Ending the filling of the color 
    turtle.end_fill()

    turtle.forward(30)
# draw_head()

def draw_left_leg():
    turtle.right(45) #left foot
    turtle.forward(30)
    turtle.up() 
    turtle.backward(30)
    turtle.down() 
# draw_left_leg()

def draw_right_leg():
    turtle.left(90) #right foot
    turtle.forward(30)
    turtle.up() 
    turtle.backward(30)
    turtle.down() 

    turtle.right(45)
    turtle.up() 
    turtle.backward(18)
    turtle.down()
# draw_right_leg()

def draw_left_arm():
    turtle.right(45) #left hand
    turtle.forward(25)
    turtle.up() 
    turtle.backward(25)
    turtle.down() 
# draw_left_arm()

def draw_right_arm():
    turtle.left(90) #right hand
    turtle.forward(25)

    turtle.color("black")
    turtle.circle(4,2)
# draw_right_arm()

def draw_face():
    turtle.up() 
    turtle.setpos(180, 87) 
    turtle.down() 
    turtle.write("x") 

    turtle.up() 
    turtle.setpos(169, 87) 
    turtle.down() 
    turtle.write("x")     

    turtle.penup() 
    turtle.setpos(170, 81) 
    turtle.pendown() 

    turtle.left(270) 
    turtle.circle(5, -180) 
    turtle.write("__")
    turtle.circle(3) 
    turtle.hideturtle() 

# draw_face()
def print_message(msg):
    turtle.penup() 
    turtle.setpos(20, -40) 
    turtle.pendown() 
    turtle.write(msg, font=("Arial", 16, "normal", "underline"))
    
# print_message(msg)

def hang(stage):
    draw_noose()
    if stage >= 1:
        draw_head()
    if stage >= 2:
        draw_left_leg()
    if stage >= 3:
        draw_right_leg()
    if stage >= 4:
        draw_left_arm()
    if stage >= 5:
        draw_right_arm()
    if stage == 6:
        draw_face()
   
# hang(6)
# window.mainloop() #Its gonna loop the drawing.

