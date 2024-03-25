import turtle as gladiator
"""
    Arena is a rectangular area where gladiator's movement is simulated.
    Movement with builtin out-of-bounds detection is executed using forward() fn.
"""
class Arena:
    def __init__(self, width: float, height: float, vehicle_speed: float = 3.5/10.0):
        self._screen = gladiator.Screen()
        self._screen.setup(1.0, 1.0)
        self._arena_width = width
        self._arena_height = height
        self._arena_borders = []
        # draw arena borders
        gladiator.delay(0)
        gladiator.speed(0)
        gladiator.up()
        gladiator.setpos(-0.5*self.width(), 0.5*self.height())
        gladiator.down()
        for i in range(2):
            gladiator.forward(self.width())
            gladiator.right(90)
            gladiator.forward(self.height())
            gladiator.right(90)
            self._arena_borders.append(gladiator.pos())
        self._arena_borders.reverse()
        gladiator.up()
        gladiator.setheading(90)
        gladiator.setpos(0.0, 0.0)
        gladiator.down()
        gladiator.delay(vehicle_speed)
        gladiator.pencolor("red")
        gladiator.shapesize(3,4,1)
        gladiator.forward(10)
    def width(self):
        return self._arena_width*self._screen.window_width()
    def height(self):
        return self._arena_height*self._screen.window_height()
    def forward(self, step: float = 1) -> chr:
        gladiator.forward(step)
        return self.collision_check()
    def right(self, step: int=10) -> chr:
        gladiator.right(step)
        return 0b0000
    def collision_check(self):
        result: chr = 0b0000
        x, y = gladiator.pos()
        # borders (left = left border etc)
        left, top = self._arena_borders[0]
        right, bottom = self._arena_borders[1]
        if y >= top:
            gladiator.sety(top)
            result |= 0b1000
        elif y <= bottom:
            gladiator.sety(bottom)
            result |= 0b0010
        if x >= right:
            gladiator.setx(right)
            result |= 0b0001
        elif x <= left:
            gladiator.setx(left)
            result |= 0b0100
        return result
