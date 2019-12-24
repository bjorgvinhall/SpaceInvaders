import turtle
import os
import math
import random
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)

# Skjar ==========================================
skjar = turtle.Screen()
skjar.bgcolor("black")
skjar.title("Space invaders")
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for hlidar in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score:  %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Player turtle ==================================
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

# Movements
playerspeed = 25
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Færa bullet fyrir ofan player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y + 8)
        bullet.showturtle()

def isCollision(t1,t2):
    #distance = √(x^2 + y^2)
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Keyboard bindings ==============================
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Enemies =========================================
number_of_enemies = 7
enemies = []
#add enemies to list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(-180,250)
    enemy.setposition(x,y)

enemyspeed = 2

# Bullet =========================================
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize()
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

# Define Bullet state
# ready = ready to fire
# fire = bullet is firing
bulletstate = "ready"

# Main game loop =================================
game = True
while game:
    for enemy in enemies:
        #enemy haegri
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #enemy nidur og afturabak
        if enemy.xcor() > 280 or enemy.xcor() < -288:
            #all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change direction
            enemyspeed *=-1

        #collision milli bullet og enemy
        if isCollision(bullet,enemy):
            #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #reset enemy
            x = random.randint(-200,200)
            y = random.randint(-180,250)
            enemy.setposition(x,y)
            #update score
            score += 1
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            #increase difficulty
            if (score % 5 == 0):
                enemyspeed *= 1.05
            


        #collision milli enemy og player
        if isCollision(enemy,player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!")
            game = False
            break
            




    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #bullet upp i topp
    if bullet.ycor() > 275:
        bulletstate = "ready"
        bullet.hideturtle()
    










