from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 220)
        self.write(self.l_score, align='center', font=('Courier', 40, 'normal'))
        self.goto(60, 220)
        self.write(self.r_score, align='center', font=('Courier', 40, 'normal'))

    def add_score(self, side):
        if side == 'r':
            self.r_score += 1
            self.update_scoreboard()
        elif side == 'l':
            self.l_score += 1
            self.update_scoreboard()
