from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Table Tennis 3000')
screen.tracer(0)

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up, 'Up')
screen.onkey(paddle_r.go_down, 'Down')
screen.onkey(paddle_l.go_up, 'w')
screen.onkey(paddle_l.go_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 55 and 350 > ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(paddle_l) < 55 and -350 < ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 420:
        scoreboard.add_score('l')
        ball.reset_position()

    if ball.xcor() < -420:
        scoreboard.add_score('r')
        ball.reset_position()


screen.exitonclick()
