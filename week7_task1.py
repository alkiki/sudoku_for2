import turtle
import math
#import numpy
t = turtle.Turtle()

koch = {
    'F': lambda amt: t.forward(amt),
    '+': lambda: t.left(90),
    '-': lambda: t.right(90)
    }
def draw(l_string, rule_set):
    if rule_set == 'koch':
        rule_set = koch
        t.penup()
        t.setx(-t.screen.screensize()[0]/2)
        t.pendown()
    else:
        raise Exception('Rule set {} is not defined'.format(rule_set))
    for state in l_string:
        if state == 'F':
            rule_set[state](1000/l_string.count('F'))
        else:
            rule_set[state]()
    turtle.done()


def draw_square(side_length, sides):
    for _ in range(0, sides):
        t.forward(side_length)
        t.right(180 - (sides-2) * 180 // sides)
    # t.forward(side_length)
    # t.right(90)
    # t.forward(side_length)
    # t.right(90)
    # t.forward(side_length)
    # t.right(90)
    # t.forward(side_length)

    turtle.done()


draw_square(100, 15)
