import turtle as gladiator
"""
    Obstacle is a rectangular box which can be angled and 
    collision with it detected.
"""
class Obstacle:
    def __init__(self, x, y, width, height, absolute_angle):
        absolute_angle %= 90.0
        self._equations = []
        positions = []
        gladiator.up()
        gladiator.pencolor("black")
        gladiator.setpos(x, y)
        gladiator.setheading(absolute_angle)
        gladiator.down()
        # render
        for _ in range(4):
            positions.append(gladiator.pos())
            gladiator.forward(width)
            gladiator.right(90)
        gladiator.up()
        gladiator.setpos(0.0, 0.0)
        gladiator.setheading(0)
        gladiator.down()
        # calculate equations
        self._positons = positions
        positions.append(positions[0])
        for i in range(4):
            pos_1, pos_2 = positions[0], positions[1]
            self._equations.append(self.__generate_equation(positions[i], positions[i+1]))

    def collision_check(self):
        x, y = gladiator.pos()
        eps = 1*2
        ys = [eq(x) for eq in self._equations]
        return 0b1000 if  y <= ys[0] and y <= ys[1] and y >= ys[2] and y >= ys[3] else 0b0000


    def __generate_equation(self, pos_1, pos_2):
        a = 0
        b = 0
        # calc a
        x1, y1 = pos_1
        x2, y2 = pos_2
        a = (y2 - y1) / (x2 - x1)
        # solve for pos_1
        b = y1 - a*x1
        def equation(x: float):
            return a*x + b
        return equation
