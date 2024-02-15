class Ball:
    def __init__(self, direction, size = "big"):
        self.size = size
        self.direction = direction
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"
    def __str__(self):
        return "size:" + self.size + ", " + "direction:" + self.direction;
my_ball = Ball("up")

my_ball.direction = "down"
my_ball.size = "small"
my_ball.color = "green"
print(my_ball.color)
print(my_ball)

your_ball = Ball("up", "small")

print(your_ball.size)
