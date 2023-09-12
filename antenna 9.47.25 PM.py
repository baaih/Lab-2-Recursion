"""
CSAPX Lab 2: Recursion

A program that draws fractal drawings, or antennas in response to the user's input for
the length of the initial side of the drawing and the number of levels there would be.
Once the user's input has been taken into account and the fractal drawing is done, the
total length of the drawing, perimeter, will be returned and printed.


author: Boya Li
"""

import turtle
import math


def strategy1(n: float, v: int) -> float:
    """
    This function would draw a fractal drawing with one continuous line with the given
    length, n, and level, v, which are both provided by the user.
    :param n: length of one of the sides of the fractal drawing
    :param v: the levels, or complexity, of the fractal drawing
    :return: total perimeter of the fractal drawing as a float
    """
    total = 0.0

    def draw(length: float, lvl: int) -> float:
        """
        This function would draw the basic sequence of lines, which would allow the fractal
        drawing to be drawn with one continuous line.
        :param length: length of each line segment
        :param lvl: the levels, or complexity, of the fractal drawing
        :return: total perimeter of each line segment as a float
        """
        if lvl == 1:
            turtle.forward(length)
            return length
        elif lvl > 1:
            total = 0
            third = length / 3
            total += draw(third, lvl - 1)
            turtle.left(90)
            total += draw(third, lvl - 1)
            turtle.right(90)
            total += draw(third, lvl - 1)
            turtle.right(90)
            total += draw(third, lvl - 1)
            turtle.left(90)
            total += draw(third, lvl - 1)
            return total

    half_diagonal = (n / 2) * math.sqrt(2)
    turtle.right(90)
    turtle.forward(half_diagonal)
    turtle.left(135)
    turtle.down()

    total = 0
    for i in range(0, 4):
        total += draw(n, v)
        turtle.left(90)
    return total


def strategy2(n: float, v: int, s: str) -> float:
    """
    This function would draw a fractal drawing by drawing every individual square with
    the given length, n, and level, v, which are both provided by the user. In order
    to accomplish this, the function would determine where the turtle is and move it
    accordingly using the s parameter.
    :param n: length of one of the sides of the fractal drawing
    :param v: the levels, or complexity, of the fractal drawing
    :param s: the side of the fractal drawing that the turtle is currently at
    :return: total perimeter of the fractal drawing as a float
    """

    total = 0.0

    def draw(length: float) -> float:
        """
        This function would draw the individual squares with the provided length for
        each side.
        :param length: length of each side of the square
        :return: perimeter of the square
        """
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        total = length * 4
        return total

    if v == 1:
        total = 0
        half_diagonal = (n / 2) * math.sqrt(2)
        full_diagonal = 2 * half_diagonal

        if s == 'left':
            turtle.backward(full_diagonal + half_diagonal)
        if s == 'right':
            turtle.forward(half_diagonal)
        if s == 'top':
            turtle.left(90)
            turtle.forward(full_diagonal)
            turtle.right(90)
            turtle.backward(half_diagonal)
        if s == 'bottom':
            turtle.right(90)
            turtle.forward(full_diagonal)
            turtle.left(90)
            turtle.backward(half_diagonal)
        if s == 'center':
            turtle.backward(half_diagonal)

        turtle.down()
        turtle.left(45)
        total += draw(n)
        turtle.up()
        turtle.right(135)
        if s == 'left':
            turtle.forward(full_diagonal + half_diagonal)
        if s == 'right':
            turtle.backward(half_diagonal)
        if s == 'top':
            turtle.forward(half_diagonal)
            turtle.right(90)
            turtle.forward(full_diagonal)
            turtle.left(90)
        if s == 'bottom':
            turtle.forward(half_diagonal)
            turtle.left(90)
            turtle.forward(full_diagonal)
            turtle.right(90)
        if s == 'center':
            turtle.forward(half_diagonal)

    if v > 1:
        total = 0
        third = n / 3
        diagonal = (third * math.sqrt(2)) / 3

        total += strategy2(third, v - 1, 'center')

        if v > 2:
            turtle.forward(diagonal * 3)
            total += strategy2(third, v - 1, 'right')
            turtle.backward(diagonal * 3)
        else:
            total += strategy2(third, v - 1, 'right')

        if v > 2:
            turtle.left(90)
            turtle.forward(diagonal * 3)
            turtle.right(90)
            total += strategy2(third, v - 1, 'top')
            turtle.right(90)
            turtle.forward(diagonal * 3)
            turtle.left(90)
        else:
            total += strategy2(third, v - 1, 'top')

        if v > 2:
            turtle.backward(diagonal * 3)
            total += strategy2(third, v - 1, 'left')
            turtle.forward(diagonal * 3)
        else:
            total += strategy2(third, v - 1, 'left')

        if v > 2:
            turtle.right(90)
            turtle.forward(diagonal * 3)
            turtle.left(90)
            total += strategy2(third, v - 1, 'bottom')
            turtle.left(90)
            turtle.forward(diagonal * 3)
            turtle.right(90)
        else:
            total += strategy2(third, v - 1, 'bottom')

    return total


def main():
    """
    This function would ask the user for the length and the level, the complexity, that they
    want the fractal drawing to be. If the inputted values don't match those that are
    expected, then it'll tell the user what type the value must be and prompt them to input
    another value. Then, it'll call the strategy1 function, which would draw the drawing
    and return the perimeter of the drawing. Finally, if the user presses enter once they are
    prompted to do so, the strategy2 function will be called, which would also draw the 
    drawing and return the perimeter of the drawing.
    :return: None
    """
    turtle.up()
    turtle.speed(0)

    length = ''
    while not isinstance(length, float):
        length = input('Length of initial side: ')
        try:
            length = float(length)
        except ValueError:
            print('Value must be a float. You entered ' + str(length) + '.')

    num_levels = ''
    while not isinstance(num_levels, int):
        num_levels = input('Number of levels: ')
        try:
            num_levels = int(num_levels)
        except ValueError:
            print('Value must be an integer. You entered ' + str(num_levels) + '.')

    print('Strategy 1 - Antenna’s length is ' +
          str(strategy1(float(length), int(num_levels))) + ' units.')
    input('Hit enter to continue...')
    turtle.reset()
    turtle.up()
    turtle.speed(0)

    print('Strategy 2 - Antenna’s length is ' +
          str(strategy2(float(length), int(num_levels), 'center')) + ' units.')
    print('Bye!')


if __name__ == '__main__':
    main()