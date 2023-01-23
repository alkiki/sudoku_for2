import turtle
import random



def random_walker():
    for i in range(random.randint(100, 300)):
        direction1 = random.randint(0, 1)
        direciton2 = random.randint(0, 1)
        if direction1 == 0:
            turtle.forward(10)
        else:
            turtle.backward(10)
        if direciton2 == 0:
            turtle.right(90)
        else:
            turtle.left(90)


random_walker()
