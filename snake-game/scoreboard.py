from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as f:
            self.high_score = str(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}",  align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.update_score()

    def score_counter(self):
        self.score += 1
        self.update_score()

