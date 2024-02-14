from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def go_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def go_down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)

