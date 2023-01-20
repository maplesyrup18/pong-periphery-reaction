'''Handles the pong interface and calls upon button creation'''
import turtle
import random
from game import leaderboard
import time

class playpong():
    def __init__(this, schedule, speed, game_time):

        #intialize variables
        this.reaction_time = []
        this.positions=[]   
        
        # Initialize the score
        this.cpu_score = 0
        this.human_player = 0
        this.bonus_points = 0
        
        this.button_is_spawned = False
        this.start_time = time.time()
        this.m_game_time=60*game_time
        this.speed = speed
        this.cpu_speed = speed + 4
        this.schedule = schedule         
            
    # Move the stick
    def stick_up(this):
        movement = this.right_stick.ycor()+20
        this.right_stick.sety(movement)

    def stick_down(this):
        movement = this.right_stick.ycor()-20
        this.right_stick.sety(movement)


    #Respone reaction to buttons!
    def react(this):
        if(this.button_is_spawned):
            reacted_time = time.time() - this.button_spawn_time
            print(reacted_time)
            if(reacted_time > 2):
                print("too slow")
            else:
                this.bonus_points += 1
            this.reaction_time.append(reacted_time)
            this.cover_button(this.position)
            this.button_is_spawned = False

    #spawn the button to react to!
    def spawn_button(this, position):
        this.button = turtle.Turtle()
        this.button.speed(20)
        this.button.shape("circle")
        this.button.color("red")
        this.button.shapesize(stretch_len=3, stretch_wid=3)
        this.button.penup()

        match position:
            #center
            case 0:
                this.positions.append("center")
                this.button.goto(-1000,0)
                return False
            #right
            case 1:
                this.positions.append("right")
                this.button.goto(100, 0)
                return False
            #left
            case 2:
                this.positions.append("left")
                this.button.goto(-1800, 0)
                return False
            #left+wiggle
            case 3:
                this.positions.append("left+wiggle")
                this.button.goto(-1800, 0)
                #wiggle activation
                return True
            #center-of-game
            case 4:
                this.positions.append("center-of-game")
                this.button.goto(1200,0)
                return False
        
        return False

    #removes a button which has been reacted to
    def cover_button(this, position):
        this.button = turtle.Turtle()
        this.button.speed(20)
        this.button.shape("circle")
        this.button.color("black")
        this.button.shapesize(stretch_len=3, stretch_wid=3)
        this.button.penup()

        match position:
            #center
            case 0:
                this.button.goto(-1000,0)
            #right
            case 1:
                this.button.goto(100, 0)
            #left
            case 2:
                this.button.goto(-1800, 0)
            #left+wiggle
            case 3:
                this.button.goto(-1800, 0)
                #wiggle activation
            #center-of-game
            case 4:
                this.button.goto(1200,0)

    #final score is only used for the human leaderboard, irrelevant for experiment, rewarded em a chocolate bar
    def calc_final_score(this):
        return (this.human_player - this.cpu_score) + this.bonus_points
    
    #saves results in CSV in data folder
    def save_results(this, player_identifier, consent):
        if(consent):
            leaderboard.save_scores_txt(this.reaction_time, this.positions, this.speed, player_identifier)
    
    #main method, lets things actually work
    def play(this, player_identifier, consent):
        #setup
        this.screen = turtle.Screen()
        this.screen.title("Pong!")
        this.screen.bgcolor("black")
        this.screen.setup(width=5000, height=600)

        # Left stick
        this.left_stick = turtle.Turtle()
        this.left_stick.speed(0)
        this.left_stick.shapesize(stretch_wid=10, stretch_len=2)
        this.left_stick.shape("square")
        this.left_stick.color("white")
        this.left_stick.penup()
        this.left_stick.goto(800, 0)
        
        #Right stick
        this.right_stick = turtle.Turtle()
        this.right_stick.speed(0)
        this.right_stick.shapesize(stretch_wid=6, stretch_len=2)
        this.right_stick.shape("square")
        this.right_stick.color("white")
        this.right_stick.penup()
        #this.right_stick.goto(400, 0)
        this.right_stick.goto(1600,0)
        
        #The pingpong ball
        this.ball = turtle.Turtle()
        this.ball.speed(200) #I think this is only draw speed, so it should work even if zero...
        this.ball.penup()
        this.ball.goto(1200, 0)
        this.ball.shape("circle")
        this.ball.color("white")
        this.ball.dx = this.speed
        this.ball.dy = -this.speed

        #Heading for scores and stuff
        this.text = turtle.Turtle()
        this.text.speed(0)
        this.text.color("white")
        this.text.penup()
        this.text.hideturtle()
        this.text.goto(1200, 260)
        this.text.write("CPU : 0    Player: 0",
                    align="center", font=("Courier", 24, "normal"))

        #keyboard stuff
        this.screen.listen()
        this.screen.onkeypress(this.stick_up, "Up")
        this.screen.onkeypress(this.stick_down, "Down")
        this.screen.onkeypress(this.react, "space")

        #for movement of objects
        alternate = False
        wiggle=False
        
        while True:
            this.screen.update()

            for t in this.schedule:
                if(time.time() -(this.start_time+t)< 0.1 and time.time()-(this.start_time+t) > 0):
                    this.position = random.randint(0,4)

                    wiggle = this.spawn_button(this.position)
                    
                    this.button_is_spawned = True
                    this.button_spawn_time = time.time()

            this.ball.setx(this.ball.xcor()+this.ball.dx)
            this.ball.sety(this.ball.ycor()+this.ball.dy)

            if(this.cpu_speed > 0):
                if(this.left_stick.ycor() > 260):
                    this.cpu_speed *= -1
                this.left_stick.sety(this.left_stick.ycor()+this.cpu_speed)
            else: 
                if(this.left_stick.ycor() < -260):
                    this.cpu_speed *= -1
                this.left_stick.sety(this.left_stick.ycor()+this.cpu_speed)
            
            # Checking borders
            if this.right_stick.ycor() > 290:
                this.right_stick.sety(290)
            if this.right_stick.ycor() < -290:
                this.right_stick.sety(-290)


            if this.ball.ycor() > 280:
                this.ball.sety(280)
                this.ball.dy *= -1
        
            if this.ball.ycor() < -280:
                this.ball.sety(-280)
                this.ball.dy *= -1
        
            if this.ball.xcor() > 1650:
                this.ball.goto(1200, 0)
                this.ball.dy *= -1
                this.cpu_score += 1
                this.text.clear()
                this.text.write("CPU : {}    Player: {}".format(
                            this.cpu_score, this.human_player), align="center",
                            font=("Courier", 24, "normal"))
        
            if this.ball.xcor() < 750:
                this.ball.goto(1200, 0)
                this.ball.dy *= -1
                this.ball.dx *= -1
                this.human_player += 1
                this.text.clear()
                this.text.write("CPU : {}    Player: {}".format(
                                        this.cpu_score, this.human_player), align="center",
                                        font=("Courier", 24, "normal"))
        
            # Paddle ball collision
            if (this.ball.xcor() > 1560 and this.ball.xcor() < 1600) and (this.ball.ycor() < this.right_stick.ycor()+60 and this.ball.ycor() > this.right_stick.ycor()-60):
                this.ball.setx(1560)
                this.ball.dx*=-1
                
            if (this.ball.xcor()< 840 and this.ball.xcor()>800) and (this.ball.ycor()<this.left_stick.ycor()+100 and this.ball.ycor()>this.left_stick.ycor()-100):
                this.ball.setx(840)
                this.ball.dx*=-1
            
            #game over
            if(time.time() - this.start_time >= this.m_game_time):
                final_score=this.calc_final_score()
                this.save_results(player_identifier, consent)
                this.screen.resetscreen()
                return final_score
