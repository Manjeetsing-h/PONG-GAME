from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.high_score = self.read_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Player A: {self.l_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(104, 260)
        self.write(f"Player B: {self.r_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(0, 220)
        self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 18, "italic"))

    def l_point(self):
        self.l_score += 1
        self.check_high_score()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.check_high_score()
        self.update_scoreboard()

    def check_high_score(self):
        total = self.l_score + self.r_score
        if total > self.high_score:
            self.high_score = total
            self.save_high_score()

    def read_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))
